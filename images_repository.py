from image_info import ImageInfo

class InMemoryImageRepository:
    def __init__(self):
        self.images = {}  # task_id -> ImageInfo(model, prompt, task_id)
        self.tasks = {}  # task_id -> Image

    def save_task(self, model, prompt):
        info = ImageInfo(model, prompt)
        self.tasks[info.id] = info
        return info.id

    def get_task(self, task_id):
        return self.tasks.get(task_id, None)

    def save_image(self, task_id, image):
        self.images[task_id] = image
        return task_id

    def get_image(self, task_id):
        return self.images.get(task_id, None)
