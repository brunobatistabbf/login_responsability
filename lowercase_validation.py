from validation_handler import  ValidationHandler

class LowercaseValidationHandler(ValidationHandler):
    def handle(self, username, password):
        if not any(char.islower() for char in password):
            return False, "Password needs a lowercase letter"
        return super().handle(username, password)

