from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import PlainTextResponse

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


@app.get("/users/{id}")
def get_user(request: Request, id: int):
    my_user = None
    for user in users:
        if user['id'] == id:
            my_user = user
            break
    if my_user is None:
        return PlainTextResponse("Not found", status_code=404)
    return templates.TemplateResponse("users/user.html", {
        "request": request,
        "my_user": my_user
    })
# (конец решения)
