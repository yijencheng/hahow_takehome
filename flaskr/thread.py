from concurrent.futures import ThreadPoolExecutor


class ThreadRequests:
    def __init__(self, func, input_list, max_worker=10):
        self.func = func
        self.input_list = input_list

        self.responses = []
        self.max_worker = max_worker

    def responses(self):
        return self.responses

    def run(self):
        with ThreadPoolExecutor(max_workers=self.max_worker) as executor:
            self.responses = executor.map(self.func, self.input_list)
