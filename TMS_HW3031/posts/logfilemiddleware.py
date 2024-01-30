import requests
#from django.core.handlers.wsgi import WSGIRequest
from django.conf import settings
from datetime import datetime

# def get_information(request: WSGIRequest):
#     print(request.user)
#     c = datetime.now()
#     current_time = c.strftime('%H:%M:%S')
#     print(current_time)
#     print(request.get_full_path())


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        
        #print(request.user)
        #c = datetime.now()
        
        #current_time = c.strftime('%d:%m:%Y %H:%M')
        #print(current_time)
        #print("custom full path: ",request.get_full_path())
        
        log_string = datetime.now().strftime('%d:%m:%Y %H:%M') + " | " + str(request.user) + " | " + "URL=" + request.get_full_path() + "\n"
        
        with open("usersActivity.log", "a", encoding="utf-8") as file:
            file.write(log_string)

        return response