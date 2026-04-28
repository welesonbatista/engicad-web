from fastapi import APIRouter
from src.main.composer.generate_part_composer import generate_part_composer
from src.views.http_types.http_request import HttpRequest

router = APIRouter(tags=["parts"])

@router.post("/generate-part")
async def generate_part(body: dict):

    http_request = HttpRequest(body)

    view = generate_part_composer()

    response = view.handle(http_request)

    return response