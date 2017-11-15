import requests


class Request:
    def __init__(self, url, method, **kwargs):
        self.url = url
        self.method = method
        self.kwargs = kwargs

        if method in ["get", "options", ]:
            self.kwargs.setdefault('allow_redirects', True)
        elif method in ["head"]:
            self.kwargs.setdefault('allow_redirects', False)

    def run(self):
        return requests.request(method=self.method, url=self.url, **self.kwargs)
