# easyocr-fastapi-app

A fastapi application that extracts text from images using easyocr.


<img src="https://user-images.githubusercontent.com/20137401/213244618-180d6fc0-3543-4f8c-b93f-e51a7be8f3f8.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/20137401/213244956-e07113cf-8e6a-432a-9b22-ebb4c08f3833.png" width="45%"></img> 


## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on deploying the project on a live system.

### Requirements

Requirements for the software and other tools to build, test and push 
- Python 3.6+
- fastapi
- easyocr
- numpy
- PIL


### Installing

A step by step series of examples that tell you how to get a development
environment running

Installation

    pip install -r requirements.txt

Usage

    uvicorn main:app --reload


## API Endpoints

  - `/`
    The root endpoint that returns a simple message "Hello World"
  - `/ocr`
    The OCR endpoint that takes an image file and returns the extracted text as an array of strings.
  - `/ocr_form`
    The OCR endpoint for handling form data that takes an image file and returns the extracted text as an array of strings.  


### Note

This app is currently setup to only recognize text in Thai language. If you want to recognize text in other languages, modify the ocr = easyocr.Reader(["th"]) in the code accordingly.
