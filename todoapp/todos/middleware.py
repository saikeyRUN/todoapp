import time
from django.utils.deprecation import MiddlewareMixin

class log_middleware_class(MiddlewareMixin):
    """
    Middleware that logs user data.
    """

    def process_request(self, request):

        with open("log_data.txt", "a") as f:
            f.write(request.path + ' ' + str(time.ctime()) + '\n')