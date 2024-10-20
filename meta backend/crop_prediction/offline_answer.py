from transformers import pipeline

pipe = pipeline("text-generation", model="AnuradhaPoddar/AgriLlama_1B")
def get_offlone_rep(query):
    messages = [
        {"role": "user", "content": "give reponse in 50 words "+query},
    ]
    ans=pipe(messages,max_length=200)
    return ans[0]["generated_text"][1]["content"]

import requests
import json
def convert_to_hindi(text):
    
    getDescriptionPrompt = f"convert in hindi: {text}"
    stream = False
    url = "https://proxy.tune.app/chat/completions"
    headers = {
        "Authorization": "",
        "Content-Type": "application/json",
    }
    data = {
    "temperature": 0.0,
        "messages":  [
        {
            "role": "system",
            "content": "you are a agricultural expert"
        },
        {
            "role": "user",
                "content": [
                    {"type": "text", "text": getDescriptionPrompt},
                    
                ],
        }
        ],
        "model": "meta/llama-3.2-90b-vision",
        "stream": stream,
        "frequency_penalty":  0.2,
        "max_tokens": 1000
    }
    response = requests.post(url, headers=headers, json=data)
    result=""
    if stream:
        for line in response.iter_lines():
            if line:
                l = line[6:]
                if l != b'[DONE]':
                    result=result+(json.loads(l))
    else:
        result=(response.json()["choices"][0]["message"]["content"])
    return result