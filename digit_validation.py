from validation_handler import  ValidationHandler

class DigitValidationHandler(ValidationHandler):
    def handle(self, username, password):
        if not any(char.isdigit() for char in password):
            return False, "Password needs a digit"
        return super().handle(username, password)