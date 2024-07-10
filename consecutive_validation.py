from validation_handler import ValidationHandler
import re
class ConsecutiveValidationHandler(ValidationHandler):
    def handle(self, username, password):
        if re.search(r'\d{3}', password):
            return False, "Passowrd contain three consecutive digits"
        return super().handle(username, password)