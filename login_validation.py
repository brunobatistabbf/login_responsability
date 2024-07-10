from validation_handler import ValidationHandler
from user import UserData

class LoginValidationHandler(ValidationHandler):
    def handle(self, username, password):
        if not UserData.registered(username):
            return False, "Not Registered"
        return super().handle(username, password)
    