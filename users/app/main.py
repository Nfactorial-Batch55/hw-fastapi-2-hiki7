from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates

from .users import create_users

users = create_users(100)  # Здесь хранятся список пользователей
app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# (сюда писать решение)
@app.get("/users")
def get_users(request: Request):
    return templates.TemplateResponse("users/index.html", {
        "request": request,
        "users": users
    })


# (конец решения)
