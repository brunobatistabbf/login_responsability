from validation_handler import ValidationHandler

class LengthValidationHandler(ValidationHandler):
    def handle(self, username, password):
        if len(password) < 8:
            return False, "Password needs more 8 characteres long"
        if len(password) > 16:
            return False, "Password not accept more than 16 characters long"
        return super().handle(username, password)