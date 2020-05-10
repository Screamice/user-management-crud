from app import DB

class Privilege(DB.Model):

    __tablename__ = "privilege"
    
    def __init__(self, DB):
        self.__id = DB.Column(DB.Integer, primary_key=True)
        self.__description = DB.Column(DB.String(20), nullable=False)
        self__detail = DB.relationship('UserPrivilege', backref='Privilege', lazy=True)
    
    def set_description(self, description):
        self.__description = description
    
    def get_state(self):
        return self.__description

    def save(self):
        if not self.__id:
            DB.session.add(self)
        DB.session.commit()