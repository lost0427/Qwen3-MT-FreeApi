from fastapi import FastAPI, Request
import httpx
import json
import time
import random
import string
import os
from dotenv import load_dotenv

load_dotenv()

def generate_random_session_hash(length=11):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

async def send_translation_request(text: str, source_lang: str = "自动检测", target_lang: str = "简体中文"):
    session_hash = generate_random_session_hash()
    
    post_url = "https://qwen-qwen3-mt-demo.ms.show/gradio_api/queue/join"
    post_payload = {
        "data": [
            text,
            source_lang,
            target_lang
        ],
        "event_data": None,
        "fn_index": 2,
        "trigger_id": 11,
        "dataType": [
            "textbox",
            "dropdown",
            "dropdown"
        ],
        "session_hash": session_hash
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        async with httpx.AsyncClient() as client:
            post_response = await client.post(post_url, json=post_payload, headers=headers)
            post_response.raise_for_status()
            print(f"POST request status code: {post_response.status_code}")
            
            get_url = f"https://qwen-qwen3-mt-demo.ms.show/gradio_api/queue/data?session_hash={session_hash}&studio_token="
            
            get_response = await client.get(get_url, headers=headers)
            get_response.raise_for_status()
            print(f"GET request status code: {get_response.status_code}")
            
            result_data = []
            async for line in get_response.aiter_lines():
                if line:
                    try:
                        if line.startswith('data: '):
                            json_data = json.loads(line[6:])
                            result_data.append(json_data)
                    except Exception as e:
                        print(f"Error decoding line: {e}")
                        continue
            
            return result_data
            
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e}")
        return None
    except httpx.RequestError as e:
        print(f"An error occurred while requesting {e.request.url!r}: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return None

app = FastAPI()

@app.post('/v1/chat/completions')
async def chat_completions(request: Request):
    expected_api_key = os.environ.get("API_KEY")
    provided_api_key = request.headers.get("Authorization")

    if not expected_api_key:
        print("Error: API_KEY environment variable not set.")
        return {"error": "Server configuration error: API key not set."}, 500

    if not provided_api_key or provided_api_key != expected_api_key:
        return {"error": "Unauthorized: Invalid or missing API key."}, 401
    
    try:
        data = await request.json()
    except json.JSONDecodeError:
        return {"error": "Invalid request, JSON payload required."}, 400
    
    if not data:
        return {"error": "Invalid request, JSON payload required."}, 400

    model = data.get('model')
    messages = data.get('messages')

    if not model or not messages:
        return {"error": "Missing 'model' or 'messages' in request."}, 400

    user_message = None
    for message in reversed(messages):
        if message.get('role') == 'user':
            user_message = message.get('content')
            break
    
    if not user_message:
        return {"error": "No user message found in 'messages'."}, 400

    source_lang = "自动检测"
    target_lang = "简体中文"

    if "zh-cn" in model.lower():
        source_lang = "简体中文"
        target_lang = "英语"
    elif "en-zh" in model.lower():
        source_lang = "英语"
        target_lang = "简体中文"
    else:
        source_lang = "简体中文"
        target_lang = "英语"
        print(f"Warning: Unrecognized model name '{model}'. Defaulting to Chinese to English translation.")

    translation_result_data = await send_translation_request(user_message, source_lang=source_lang, target_lang=target_lang)

    if translation_result_data:
        translated_text = ""
        for item in translation_result_data:
            if 'msg' in item and item['msg'] == 'process_completed':
                if 'output' in item and 'data' in item['output']:
                    translated_text = item['output']['data']
                    break

        if translated_text:
            if isinstance(translated_text, list):
                translated_text = ''.join(str(item) for item in translated_text)
            elif not isinstance(translated_text, str):
                translated_text = str(translated_text)
            
            response_payload = {
                "id": f"chatcmpl-{random.randint(10000000, 99999999)}",
                "object": "chat.completion",
                "created": int(time.time()),
                "model": model,
                "choices": [
                    {
                        "index": 0,
                        "message": {
                            "role": "assistant",
                            "content": translated_text
                        },
                        "finish_reason": "stop"
                    }
                ]
            }
            return response_payload
        else:
            return {"error": "Translation process completed but no output data found."}, 500
    else:
        return {"error": "Translation request failed."}, 500