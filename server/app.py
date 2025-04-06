from flask import Flask,request,render_template,jsonify
from flask_cors import CORS
from fileinput import filename
import os
from pathlib import Path
from werkzeug.utils import secure_filename
import numpy as np
import tensorflow as tf    
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pathlib import Path
from werkzeug.utils import secure_filename
import cv2
import numpy as np
import os
import tensorflow as tf
from tensorflow.keras.models import load_model
from temp import getData
from prompt import generate
from dotenv import load_dotenv
import requests

UPLOAD_FOLDER = Path('use')
UPLOAD_FOLDER.mkdir(exist_ok=True)  # Make sure the folder exists

app = Flask(__name__)
CORS(app)

@app.route("/")
def data():
    return "MobileNet Model Api developed by Hustle Hulk"

@app.route("/predictions", methods=['GET'])
def info():
    return render_template('index.html')

@app.route("/predictions", methods=['POST'])
def prediction():
    try:
        file = request.files['file_from_react']
        if file.filename != '':
            fn = secure_filename(file.filename)
            filepath = UPLOAD_FOLDER / fn

            if fn not in os.listdir(UPLOAD_FOLDER):
                file.save(str(filepath))

            img = cv2.imread(str(filepath))
            resize = tf.image.resize(img, (256, 256))
            model = load_model('model.h5')
            yhat = model.predict(np.expand_dims(resize / 255, 0))

            data = getData(np.argmax(yhat))
            if len(data) < 2:
                return jsonify({"error": "Incomplete data returned from getData"}), 500

            flag = 1
            text = ["Not applicable", "Not applicable", "Not applicable"]

            if data[1] != "Healthy":
                text = generate(c=data[0], d=data[1])
                flag = 0

            return jsonify({
                "Crop": data[0].capitalize(),
                "Disease": data[1].capitalize(),
                "flag": flag,
                "cause": text[0],
                "sym": text[1],
                "cure": text[2]
            })

        return jsonify({"error": "No file uploaded"}), 400

    except Exception as e:
        print(f"[ERROR] {e}")
        return jsonify({"Crop": "error", "Disease": "error", "message": str(e)}), 500

             

load_dotenv()
GOOGLE_TRANSLATE_API_KEY = os.getenv("GOOGLE_TRANSLATE_API_KEY")

@app.route("/translation",methods=['GET','POST'])
def translate_text():
    if request.method == "POST":
        try:
            data = request.get_json()
            plant_data = data.get("plantData", {})
            target_lang = data.get("targetLanguage", "en")

            translated_data = {}
            for key, value in plant_data.items():
                if value.strip():
                    response = requests.post(
                        "https://translation.googleapis.com/language/translate/v2",
                        data={
                            "q": value,
                            "target": target_lang,
                            "format": "text",
                            "key": GOOGLE_TRANSLATE_API_KEY
                        }
                    )
                    response_data = response.json()
                    translated_text = response_data["data"]["translations"][0]["translatedText"]
                    translated_data[key] = translated_text
                else:
                    translated_data[key] = value
            return jsonify({"translations": translated_data})
        except requests.exceptions.RequestException as e:
            return jsonify({"error": f"Request error: {str(e)}"}), 500
        except KeyError as e:
            return jsonify({"error": f"Key error: {str(e)}"}), 500
        except Exception as e:
            return jsonify({"error": f"Internal error: {str(e)}"}), 500
if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=8000)