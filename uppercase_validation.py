from validation_handler import ValidationHandler

class UppercaseValidationHandler(ValidationHandler):
    def handle(self, username, password):
        if not any(char.isupper() for char in password):
            return False, "Password needs an uppercase letter"
        return super().handle(username, password)