class UserData:
    registered_users = {
        'jorge123': 'Password1@',
        'amsterda13': 'Password2#',
        'alfablogoficial': 'Password3$',
    }

    @staticmethod
    def registered(username):
        return username in UserData.registered_users
    