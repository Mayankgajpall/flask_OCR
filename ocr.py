from flask import Flask, request, jsonify
import requests
import base64
import os

app = Flask(__name__)

@app.route('/fetch/' , methods = ['GET'])
def get_text():
    if request.method == 'GET':
        apikey = os.environ.get("OCR_KEY")
        getfile = request.files["filename"]
        image_string = base64.b64encode(getfile.read()).decode('ascii')
        image_uri = "data:"+getfile.content_type+";base64,"+image_string
        response = requests.post("https://api.ocr.space/parse/image", headers={"apikey":apikey}, data={"base64Image":image_uri}).json()
        data = {
                    "extracted_text":response["ParsedResults"][0]["ParsedText"]
                }
        return jsonify(data)


app.run(host='0.0.0.0', port=5000)