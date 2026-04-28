from src.controllers.generate_part import GeneratePartController
from src.models.repositories.part_repository import PartRepository
from src.service.cadquery_service import CadQueryService
from src.views.generate_part_view import GeneratePartView

def generate_part_composer():

    cad_service = CadQueryService()

    repository = PartRepository()

    controller = GeneratePartController(
      cad_service,
      repository
    )

    view = GeneratePartView(controller)

    return view