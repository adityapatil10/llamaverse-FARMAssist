import json
import requests
import numpy as np
import tensorflow as tf
import base64

def get_soil_description(image):
    imageUrl = image

    with open(imageUrl, 'rb') as image_file:
        base64_string = base64.b64encode(image_file.read()).decode('utf-8')

    getDescriptionPrompt = f"what is the type of the soil from Red, aluvial, black, clay, Laterite, sand"
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


def predict_weather(text1, text2):
    getDescriptionPrompt = f"what will be the whether in {text1} for {text2} in terms of rainfall,temperature and humidity"
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
            "content": "you are from whether forecast department"
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

def give_crop_pred(soilname,weatherreport,image):
    imageUrl = image

    with open(imageUrl, 'rb') as image_file:
        base64_string = base64.b64encode(image_file.read()).decode('utf-8')

    getDescriptionPrompt = f"This is a picture of soil with some details as follows:'{soilname}' you will be given information about the weather report which will be given below. suggest 3 crops with explaination that can be grown in 200-300 words in response give answer as a assistant. weather report:{weatherreport}"
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

def process_inputs(text1, text2, image):
    # Example processing (you can customize this)
    import os
    image_path = os.path.join("data/temp.jpg")
    image.save(image_path)
    soil=get_soil_description(image_path)
    temp=predict_weather(text1, text2)
    return give_crop_pred(soil,temp,image_path)
    # temp,hum,rain=get_temp_detail(text1,text2)
    # array=[[prop['N'],prop['P'],prop['K'],temp,prop['pH'],rain]]
    # # return val
    # crop=predict_crop(array)[0]
    # completion_response=remotely_run.complete(f"<|begin_of_text|><|start_header_id|>user<|end_header_id|>justify growing {crop} in black soil with pH:{prop['pH']},N:{prop['N']},K:{prop['K']},P:{prop['P']} in temperature {temp}, humidity {hum} and rainfall {rain} also give alternate options.instruction:do not mention any of the provided features in option,start respone with 'you should grow {crop} because' give response in 200 words <|eot_id|><|start_header_id|>assistant<|end_header_id|>")
    # return(completion_response)