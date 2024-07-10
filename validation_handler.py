from abc import ABC, abstractmethod
class ValidationHandler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle(self, username, password):
        if self.next_handler:
            return self.next_handler.handle(username, password)
        return True, "SUCCESS!!"