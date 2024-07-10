from validation_handler import ValidationHandler
class SpecialCharValidationHandler(ValidationHandler):
    def handle(self, username, password):
        if not any(char in '@#$%&' for char in password):
            return False, "Password needs a special character (@ $ # % & *)"
        return super().handle(username, password)