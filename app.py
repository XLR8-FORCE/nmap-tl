

from fastapi import FastAPI
from fastapi import Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="home.html"
    )

@app.get("/search")
def search(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="search.html"
    )

@app.get("/statistics")
def statistics(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="statistics.html"
    )

@app.get("/watchlist")
def watchlist(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="watchlist.html"
    )
