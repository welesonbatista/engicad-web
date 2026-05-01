from fastapi import APIRouter
from src.main.composer.generate_bolt_composer import generate_bolt_composer
from src.views.http_types.http_request import HttpRequest

generate_bolt = APIRouter(tags=["bolts"])

@generate_bolt.post("/generate-bolt")
async def generate_bolt_endpoint(body: dict):
    http_request = HttpRequest(body=body)
    view = generate_bolt_composer()
    response = await view.handle(http_request)
    return response
