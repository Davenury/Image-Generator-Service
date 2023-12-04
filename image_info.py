import uuid

class ImageInfo:
    def __init__(self, model, prompt):
        self.model = model
        self.prompt = prompt
        self.id = str(uuid.uuid4())
