from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import PlainTextResponse

from .cars import create_cars

cars = create_cars(100)  # Здесь хранятся список машин
app = FastAPI()


@app.get("/")
def index():
    return Response("<a href='/cars'>Cars</a>")


# (сюда писать решение)
@app.get("/cars")
def get_cars(page: int = 1, limit: int = 10):
    start = (page - 1) * limit
    end = start + limit
    if start > len(cars):
        raise HTTPException(status_code=404, detail="No cars found")
    return cars[start:end]


@app.get("/cars/{id}")
def get_car(id: int):
    for car in cars:
        if car["id"] == id:
            return car
    return PlainTextResponse("Not found", status_code=404)
# (конец решения)
