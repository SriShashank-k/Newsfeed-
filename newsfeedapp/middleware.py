import logging

logger = logging.getLogger(_name_)

class RequestLoggingMiddleware:
    def _init_(self, get_response):
        self.get_response = get_response

    def _call_(self, request):
        # Log information about the incoming request
        logger.info(f"Incoming request: {request.method} {request.path}")

        response = self.get_response(request)

        # Log information about the outgoing response
        logger.info(f"Outgoing response: {response.status_code}")

        return response