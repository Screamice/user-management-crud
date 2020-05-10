from werkzeug.security import generate_password_hash, check_password_hash
from app import DB


class UserInfo(DB.Model):

    __tablename__ = "user_info"
    
    def __init__(self, DB):
        self.__id = DB.Column(DB.Integer, primary_key=True)
        self.__full_name = DB.Column(DB.String(50))
        self.__username = DB.Column(DB.String(50))
        self.__password = DB.Column(DB.String(50))
        self.__email = DB.Column(DB.String(50))
        self.__configuration_id = DB.Column(DB.Integer, DB.ForeignKey('configurarion.id'))
        self.__details = DB.relationship('UserPrivilege', backref='UserInfo', lazy=True)
    
    def set_id(self, id):
        self.__id = id
    
    def set_full_name(self, full_name):
        self.__full_name = full_name
    
    def set_username(self, username):
        self.__username = username
        
    def set_password(self, password):
        self.__password = generate_password_hash(password, method="sha256")
    
    def set_email(self, email):
        self.__email = email

    def get_id(self):
        return self.__id
    
    def get_full_name(self):
        return self.__full_name
    
    def get_username(self):
        return self.__username
        
    def get_password(self):
        return self.__password
    
    def get_email(self):
        return self.__email

    def check_password(self, password):
        return check_password_hash(self.__password, password)

    def save(self):
        if not self.__id:
            DB.session.add(self)
        DB.session.commit()

    @staticmethod
    def get_by_user(username):
        return Usuario.query.filter_by(username=username).first()

    @staticmethod
    def get_by_email(email):
        return Usuario.query.filter_by(email=email).first()