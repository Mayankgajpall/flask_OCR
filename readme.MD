This is a simple OCR project which has an API endpoint. Send an image to that API endpoint and it will return the extracted text.

Send image file as a form-data with key value "filename"<br />
API endpoint: /fetch/

Sample response:
{
    "extracted_text" : "Text extracted from the image"
}

To run this project:
1) Create a free account in OCR Space and put the API key in .env file as mentioned in .env_example
2) Install all dependencies from requirements.txt file and run the ocr.py file with command python ocr.py
3) Application is running now, send request to the endpoint mentioned above and receive the respone.

#### This project is a part of demonstrating implementation of kubernetes. This application will be considered as a microservice and will be deployed using kubernetes.
