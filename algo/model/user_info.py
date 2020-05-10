from werkzeug.security import generate_password_hash, check_password_hash
from app import DB


class UserInfo(DB.Model):

    tablename = "user_info"
    
    id = DB.Column(DB.Integer, primary_key=True)
    full_name = DB.Column(DB.String(50))
    username = DB.Column(DB.String(50))
    password = DB.Column(DB.String(50))
    email = DB.Column(DB.String(50))
    configuration_id = DB.Column(DB.Integer, DB.ForeignKey('configurarion.id'))
    details = DB.relationship('UserPrivilege', backref='UserInfo', lazy=True)
    
    def set_id(self, id):
        self.id = id
    
    def set_full_name(self, full_name):
        self.full_name = full_name
    
    def set_username(self, username):
        self.username = username
        
    def set_password(self, password):
        self.password = generate_password_hash(password, method="sha256")
    
    def set_email(self, email):
        self.email = email

    def get_id(self):
        return self.id
    
    def get_full_name(self):
        return self.full_name
    
    def get_username(self):
        return self.username
        
    def get_password(self):
        return self.password
    
    def get_email(self):
        return self.email

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        if not self.id:
            DB.session.add(self)
        DB.session.commit()

    @staticmethod
    def get_by_user(username):
        return UserInfo.query.filter_by(username=username).first()

    @staticmethod
    def get_by_email(email):
        return UserInfo.query.filter_by(email=email).first()