class GeneratePartView:

    def __init__(self, controller):
        self.__controller = controller

    def handle(self, http_request):

        response = self.__controller.handle(http_request)

        return response