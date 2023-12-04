import time
from image_service import ImageService
from redis_task_queue import RedisTaskQueue
from image_generator import ImageGenerator
from fastapi import FastAPI
from models_service import ModelService
from image_types import ImageData


# dependencies
task_queue = RedisTaskQueue()
service = ImageService(task_queue)
generator = ImageGenerator(task_queue)
model_service = ModelService()


app = FastAPI()


@app.post("/image")
async def root(data: ImageData):
    image_id = service.request_image(data.model, data.prompt)
    return {"id": image_id}


@app.get("/image/{task_id}")
async def get_image(task_id):
    return {"image": service.get_image(task_id)}


@app.get("/models")
async def get_models(type: str | None = None):
    return model_service.get_models(type)
