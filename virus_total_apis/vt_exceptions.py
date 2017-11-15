class ApiError(Exception):
    pass


class ApiRequestError(ApiError):
    def __init__(self, status_code, data, message=None):
        ApiError.__init__(message)
        self.status_code = status_code
        self.data = data

class NoPermissionError(ApiRequestError):
    def __init__(self, data):
        ApiRequestError.__init__(self, 403, data, "You have no permissions for this request. Maybe you need a private API key?")


class ExceededRateLimit(ApiRequestError):
    def __init__(self, data):
        ApiRequestError.__init__(self, 204, data, "You have exceeded your request rate limit (usually 4 in a minute)")
