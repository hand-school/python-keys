class PasswordValidationMixin:
    def is_password_valid(self):
        return self.password == 'simple123456'


class LogInRequest(PasswordValidationMixin):
    def __init__(self, login, password):
        self.login = login
        self.password = password


class ChangePasswordRequest(PasswordValidationMixin):
    def __init__(self, password):
        self.password = password


logInReq = LogInRequest('login', 'simple123456')
changePasswordReq = ChangePasswordRequest('simple123456')

print(logInReq.is_password_valid())
print(changePasswordReq.is_password_valid())
