from fastapi import FastAPI, Request, Depends, HTTPException, status
import httpx
import json
import time
import random
import string
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

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

def verify_api_key(request: Request):
    expected_api_key = os.environ.get("API_KEY")
    provided_api_key = request.headers.get("Authorization")

    if not expected_api_key:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Server configuration error: API key not set."
        )

    if not provided_api_key or provided_api_key != expected_api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized: Invalid or missing API key."
        )
    return True

def load_language_map():
    try:
        with open("language.json", 'r', encoding='utf-8') as f:
            language_data = json.load(f)
            return {item['code']: item['name'] for item in language_data}
    except FileNotFoundError:
        print("Error: language.json not found. Language detection may not work correctly.")
    except json.JSONDecodeError:
        print("Error: Could not decode language.json. Please check its format.")
    except Exception as e:
        print(f"An unexpected error occurred while reading language.json: {e}")
    return {}

@app.post('/v1/chat/completions')
async def chat_completions(request: Request, auth: bool = Depends(verify_api_key)):
    try:
        data = await request.json()
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid request, JSON payload required.")

    if not data:
        raise HTTPException(status_code=400, detail="Invalid request, JSON payload required.")

    model = data.get('model')
    messages = data.get('messages')

    if not model or not messages:
        raise HTTPException(status_code=400, detail="Missing 'model' or 'messages' in request.")

    user_message = None
    for message in reversed(messages):
        if message.get('role') == 'user':
            user_message = message.get('content')
            break

    if not user_message:
        raise HTTPException(status_code=400, detail="No user message found in 'messages'.")

    language_map = load_language_map()

    source_lang = "自动检测"
    target_lang = "简体中文"

    if model and "-" in model:
        parts = model.lower().rsplit('-', 2)
        if len(parts) >= 3:
            source_code, target_code = parts[-2], parts[-1]

            if target_code != "auto":
                source_lang_name = language_map.get(source_code)
                target_lang_name = language_map.get(target_code)

                if source_lang_name and target_lang_name:
                    source_lang = source_lang_name
                    target_lang = target_lang_name
                else:
                    print(f"Warning: Could not find language names for codes '{source_code}' or '{target_code}'. Using defaults.")
            else:
                print("Warning: target_code cannot be 'auto'. Using defaults.")
        else:
            print(f"Warning: Invalid language format in model: '{model}'. Expected format like 'en-zh'. Using defaults.")
    else:
        print(f"Info: No language codes found in model: '{model}'. Using defaults.")

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
            raise HTTPException(status_code=500, detail="Translation process completed but no output data found.")
    else:
        raise HTTPException(status_code=500, detail="Translation request failed.")

@app.get('/v1/models')
async def get_models(auth: bool = Depends(verify_api_key)):
    try:
        with open("language.json", 'r', encoding='utf-8') as f:
            language_data = json.load(f)
            all_language_codes = [item['code'] for item in language_data]
    except Exception as e:
        print(f"An unexpected error occurred while reading language.json: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while processing language configuration."
        )

    available_models = [
        {
            "id": f"qwen3-mt-{src}-{tgt}",
            "object": "model",
            "created": int(datetime.utcnow().timestamp()),
            "owned_by": "Qwen3-MT",
            "permission": []
        }
        for src in all_language_codes
        for tgt in all_language_codes
        if src != tgt and tgt != "auto"
    ]
    available_models.sort(key=lambda m: m['id'])

    return {
        "object": "list",
        "data": available_models
    }
