from fastapi import APIRouter
from src.main.composer.generate_part_composer import generate_part_composer
from src.views.http_types.http_request import HttpRequest

generate_part = APIRouter(tags=["parts"])

@generate_part.post("/generate-part")
async def generate_part_endpoint(body: dict):

    http_request = HttpRequest(body=body)

    view = generate_part_composer()

    response = await view.handle(http_request)

    return response
