# Image Generator Service

## Part of RPGLife

Side project meant to be used as a server for image generation using Diffusers library.

### Requirements
Aside from python requirements (`pip install -r requirements.txt`), there's a need for working Redis instance (for now on localhost on 6739 port, run e.g. by `docker run -d -p 6379:6379 redis`).

### Endpoints
#### POST /image
Creates an image generation job. Request body:
```json
{
    "prompt": <str>,
    "model": <str>
}
```
Model defaults to `runwayml/stable-diffusion-v1-5`. List of available models (most popular) is available at /models endpoint.
Returns body with id of the job.
```json
{
    "id": <job id>
}
```

#### GET /image/<job id>
Returns the image url (if the job completed) or null (if the job hasn't completed successfully).

#### GET /models
Returns the list of available models (most popular). Takes an optional parameter `type` - is used for limiting the models only to interesting. For now 
the only available model type is `text-to-image`.
```json
[
    {
        "model_name": "Linaqruf/anything-v3.0",
        "model_type": "text-to-image",
        "avatar_url": "https://aeiljuispo.cloudimg.io/v7/https://cdn-uploads.huggingface.co/production/uploads/6365c8dbf31ef76df4042821/WUeQo7JcoMfrjz80XI-FN.png?w=200&h=200&f=face"
    },
    ...
]
```

### To be done
* Make configuration independent from code.
* Possibility to use image-to-image pipelines.
* Organize code in packages.
* Dependency Injection, tests.
