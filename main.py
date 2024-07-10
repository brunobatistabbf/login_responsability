from login_validation import LoginValidationHandler
from uppercase_validation import UppercaseValidationHandler
from lowercase_validation import LowercaseValidationHandler
from specialchar_validation import SpecialCharValidationHandler
from digit_validation import DigitValidationHandler
from consecutive_validation import ConsecutiveValidationHandler
from length_validation import LengthValidationHandler

def main():
    login_handler = LoginValidationHandler()
    login_handler.set_next(UppercaseValidationHandler()).set_next(LowercaseValidationHandler()).set_next(SpecialCharValidationHandler()).set_next(DigitValidationHandler()).set_next(ConsecutiveValidationHandler()).set_next(LengthValidationHandler())

    username = input("Enter username: ")
    password = input("Enter password: ")

    result, message = login_handler.handle(username, password)
    if result:
        print("Login Sucessful")
    else:
        print(f"Login failed: {message}")

if __name__ == '__main__':
    main()

