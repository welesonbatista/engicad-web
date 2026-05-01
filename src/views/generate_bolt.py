class GenerateBoltView:

    def __init__(self, controller):
        self.__controller = controller

    async def handle(self, http_request):
        response = await self.__controller.generate_bolt(http_request.body)
        return response
