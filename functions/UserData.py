import names
import random, string


class UserData:
    def __init__(self):
        self.first_name = names.get_first_name().lower()
        self.letters = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

    def name(self):
        return self.first_name

    def email(self):
        return f'{self.first_name}@{self.first_name}.test'

    def password(self):
        return self.letters
