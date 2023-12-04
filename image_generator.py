from diffusers import DiffusionPipeline
import torch
from tasks import GENERATE_IMAGE_TASK, IMAGE_RESPONSE_TASK
import json
import io
import base64
import requests
from PIL import Image


def upload_image(image):

    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    buffered.seek(0)

    files = { "image": buffered }
    response = requests.post("https://api.imgur.com/3/image", headers={"Authorization": "Client-ID 5d6743069cf5458"}, files=files)
    return response.json()["data"]["id"]


class ImageGenerator:
    def __init__(self, task_queue):
        self.task_queue = task_queue
        self.task_queue.subscribe_to_tasks(GENERATE_IMAGE_TASK, self.generate_image)


    def generate_image(self, task_info):
        data = task_info["data"].replace("'", '"')
        data = json.loads(data)
        task_id = data["task_id"]
        model = data["task_info"]["model"]
        prompt = data["task_info"]["prompt"]

        pipeline = DiffusionPipeline.from_pretrained(model)
        image = pipeline(prompt).images[0]
        
        result = upload_image(image)

        self.task_queue.depute_task(task_id, IMAGE_RESPONSE_TASK, { "image": result })
