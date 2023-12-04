from pydantic import BaseModel


class ImageData(BaseModel):
    prompt: str
    model: str = "runwayml/stable-diffusion-v1-5"
