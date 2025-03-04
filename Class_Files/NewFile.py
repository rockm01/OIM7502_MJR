import hashlib
import datetime as dt
import dateutil as util
import dateutil.parser


class User:


    def __init__(self, username=None, password=None, email=None, dob=None):
        self.username = username
        self.password = self.encrypt_password(password)
        self.email = email
        self.dob = dob


    def __str__(self):
        return f"{self.username}, {self.password}, {self.email}, {self.dob}"


    def __repr__(self):
        return f"User{self.__dict__}"


    def __eq__(self, other):
        return self.username == other.username


    def encrypt_password(self, password):
        password = password.encode('utf-8')
        return hashlib.sha256(password).hexdigest()


    def check_password(self, password):
        password = self.encrypt_password(password)
        return password == self.password


    def get_age(self):
        bday = util.parser.parse(self.dob)
        return dt.datetime.now().year - bday.year




if __name__ == '__main__':
    parker = User("Parker", "1234", "parker@email.com", "5/18/1953")
    print(parker)
    print(parker.get_age())
