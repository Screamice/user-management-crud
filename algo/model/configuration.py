from app import DB


class Configuration(DB.Model):

    __tablename__ = "configuration"
    
    def __init__(self, DB):
        self.__id = DB.Column(DB.Integer, primary_key=True)
        self.__lang = DB.Column(DB.String(5), nullable=False)
        self.__country = DB.Column(DB.String(50), nullable=False)
        self.__state = DB.Column(DB.String(50), nullable=False)
        sef.__users = DB.relationship('UserInfo', backref='Configuration', lazy=True)
    
    def set_lang(self, lang):
        self.__lang = lang
    
    def set_country(self, country):
        self.__country = country
    
    def set_state(self, state):
        self.__state = state

    def get_lang(self):
        return self.__lang
    
    def get_country(self):
        return self.__country
    
    def get_state(self):
        return self.__state

    def save(self):
        if not self.__id:
            DB.session.add(self)
        DB.session.commit()