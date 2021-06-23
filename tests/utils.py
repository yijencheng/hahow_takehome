class MockResponse:
    def __init__(self, data: dict, status_code: int):
        self.data = data
        self.status_code = status_code

    def json(self):
        return self.data