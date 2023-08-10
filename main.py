from fastapi import FastAPI, Request

from fastapi.templating import Jinja2Templates

import firebase

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):
    kifus = firebase.get_all_kifu()
    kifus = list(kifus.items())

    return templates.TemplateResponse("index.html", {"request": request,"kifus":kifus})

@app.get("/view/{kifu_id}")
async def index(request: Request,kifu_id:str):
    kifu = firebase.get_kifu(kifu_id)
    print(kifu[1])

    image_urls = firebase.getimages(kifu_id,kifu[1]["move_count"])
    #print(image_urls)
    return templates.TemplateResponse("view.html", {"request": request,"image_urls":image_urls})

# uvicorn main:app --reload --host 0.0.0.0