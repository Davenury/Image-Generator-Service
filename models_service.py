import requests


class ModelService:

    def get_models(self, model_type):
        url = "https://huggingface.co/models-json?library=diffusers&sort=likes"
        if model_type is not None:
            url += f"&pipeline_tag={model_type}"
        response = requests.get(url).json()
        return [{"model_name": it["id"], "model_type": it.get("pipeline_tag", None), "avatar_url": it.get("authorData", {"avatarUrl", None}).get("avatarUrl") } for it in response["models"]]

