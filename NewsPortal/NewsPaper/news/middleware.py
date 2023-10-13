class MobileorFullMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.moblie:
            prefix = 'mobile/'
        else:
            prefix = 'full/'
        response.template_name = prefix + response.template_name
        return response