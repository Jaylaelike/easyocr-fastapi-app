import io
import logging

from fastapi import FastAPI, APIRouter, Request, File, UploadFile
from fastapi.responses import FileResponse, StreamingResponse
import easyocr

import PIL
from PIL import Image, ImageOps
import numpy


description = """
ถอดข้อความรูปภาพให้เป็นข้อความอย่างสนุกสนานกันได้เลย. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

app = FastAPI(
    title="Platerecognizer",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Racksync",
        "url": "https://www.racksync.com/"
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    )



router = APIRouter()
ocr = easyocr.Reader(["th"])
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ocr")


@app.get("/")
async def root():
    return {"message": "Hello World"}


# @router.post("/ocr")
@app.post("/ocr")
async def do_ocr(request: Request, file: UploadFile = File(...)):
    if file is not None:
        # res = ocr.readtext(await file.read())
        # res = ocr.readtext(file.file)
        # via pil
        imgFile = numpy.array(PIL.Image.open(file.file).convert("RGB"))
        res = ocr.readtext(imgFile)

        # return array of strings
        return [item[1] for item in res]
        # probable_text = "\n".join((item[1] for item in res))
        # return StreamingResponse(
        #     io.BytesIO(probable_text.encode()), media_type="text/plain"
        # )

    return {"error": "missing file"}


@app.post("/ocr_form")
async def do_ocr_form(request: Request, file: UploadFile = File(...)):
    # form = await request.form()
    # file = form.get("file", None)
    if file is not None:
        # res = ocr.readtext(await file.read())
        res = ocr.readtext(file.file.read())
        return [item[1] for item in res]

    return {"error": "missing file"}


app.include_router(router)
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)


### First lab #########
# import easyocr
# import base64
# from typing import Optional
# from fastapi import FastAPI
# import numpy as np
# from pydantic import BaseModel


# class imageClass (BaseModel):
#     imgStr: str
#     lan: str = "en"

# app = FastAPI()

# @app.post("/easyocr")
# def read_root (imageClass: imageClass ):
#     if(imageClass.lan == "string"):
#        imageClass.lan = 'en'

#     base64picture = imageClass.imgStr
#     img = base64.decodebytes (str.encode(base64picture))
#     reader = easyocr.Reader([imageClass.lan])
#     result = reader. readtext(img, detail = 0)
#     return {"ocrPre": result}
#         # return {"ERROR": "An error has occured"}
