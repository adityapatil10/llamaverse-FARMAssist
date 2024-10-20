from flask import Flask, request, jsonify
import numpy as np
from crop_prediction.crop_prediction import process_inputs
from crop_prediction.offline_answer import get_offlone_rep,convert_to_hindi
from crop_prediction.disease_detection import give_crop_pred
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form.get("location")
    month = request.form.get("month")
    image_file = request.files['image']
    # image = Image.open(image_file)
    data=process_inputs(location,month,image_file)
    return jsonify({'prediction': data})

@app.route('/offline_answer', methods=['POST'])
def offline_answer():
    query = request.form.get("query")
    # image = Image.open(image_file)
    data=get_offlone_rep(query)
    return jsonify({'prediction': data})

@app.route('/disease_detection', methods=['POST'])
def disease_detection():
    # crop = request.form.get("crop")
    crop="rice"
    image_file = request.files['image']
    # image = Image.open(image_file)
    data=give_crop_pred(image_file,crop)
    return jsonify({'prediction': data})

@app.route('/hindi_conversation', methods=['POST'])
def hindi_conversation():
    text = request.form.get("text")
    data=convert_to_hindi(text)
    return jsonify({'prediction': data})

if __name__ == '__main__':
    app.run(debug=False)
