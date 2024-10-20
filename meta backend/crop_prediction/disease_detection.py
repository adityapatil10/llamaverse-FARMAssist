import base64
import json
import os
import requests
def give_crop_pred(image,crop):
    image_path = os.path.join("data/temp.jpg")
    image.save(image_path)
    imageUrl = image_path

    with open(imageUrl, 'rb') as image_file:
        base64_string = base64.b64encode(image_file.read()).decode('utf-8')
    with open("data/ricedis1_1.png", 'rb') as image_file:
        base64_string1 = base64.b64encode(image_file.read()).decode('utf-8')
    with open("data/ricedis2_1.png", 'rb') as image_file:
        base64_string2 = base64.b64encode(image_file.read()).decode('utf-8')
    with open("data/ricedis3_1.png", 'rb') as image_file:
        base64_string3 = base64.b64encode(image_file.read()).decode('utf-8')
    with open("data/ricedis3_2.png", 'rb') as image_file:
        base64_string4 = base64.b64encode(image_file.read()).decode('utf-8')    

    getDescriptionPrompt = f"Based on the image of {crop} crop provided predict which crop disease is possibly present in the image take into account the other images to give explainations and suggestions for betterment of the {crop} plants"
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
                    {
                        "type": "image_url",
                        "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_string}",
                        "detail": "low"
                    },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_string1}",
                        "detail": "low"
                    },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_string2}",
                        "detail": "low"
                    },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_string3}",
                        "detail": "low"
                    },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_string4}",
                        "detail": "low"
                    },
                    },

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