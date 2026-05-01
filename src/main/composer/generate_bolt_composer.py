from src.controllers.generate_bolt import GenerateBoltController
from src.models.repositories.bolt_repository import BoltRepository
from src.service.cadquery_service import CadQueryService
from src.views.generate_bolt import GenerateBoltView


def generate_bolt_composer():
    cad_service = CadQueryService()
    repository = BoltRepository()
    controller = GenerateBoltController(cad_service, repository)
    view = GenerateBoltView(controller)
    return view
