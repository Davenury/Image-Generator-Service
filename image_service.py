from images_repository import InMemoryImageRepository
from redis_task_queue import RedisTaskQueue
from tasks import GENERATE_IMAGE_TASK, IMAGE_RESPONSE_TASK
import json


class ImageService:
    def __init__(self, tasks_queue):
        self.repository = InMemoryImageRepository()
        self.task_queue = tasks_queue
        self.task_queue.subscribe_to_tasks(IMAGE_RESPONSE_TASK, self.handle_image_delivery)

    def request_image(self, model, prompt):
        task_id = self.repository.save_task(model, prompt)
        
        self.task_queue.depute_task(task_id, GENERATE_IMAGE_TASK, { "model": model, "prompt": prompt })

        return task_id

    def get_image(self, task_id):
        return self.repository.get_image(task_id)

    def handle_image_delivery(self, result):
        data = json.loads(result["data"].replace("'", '"'))
        url = f"imgur.com/{data['task_info']['image']}.jpeg"
        self.repository.save_image(data["task_id"], url)
