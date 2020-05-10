from app import DB

class UserPrivilege(DB.Model):

    __tablename__ = "user_privilege"
    
    def __init__(self, DB):
        self.__user_id = DB.Column(DB.Integer, DB.ForeignKey('UserInfo.id'))
        self.__privilege_id = DB.Column(DB.Integer, DB.ForeignKey('Privilege.id'))
    
    def set_user_id(self, user_id):
        self.__user_id = user_id
    
    def privilege(self, privilege_id):
        self.__privilege_id = privilege_id

    def get_user_id(self):
        return self.__user_id

    def get_privilege_id(self):
        return self.__privilege_id

    def save(self):
        if not self.__id:
            DB.session.add(self)
        DB.session.commit()