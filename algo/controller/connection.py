from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

class Connection:
    
    def __init__(self):
        self.__postgresql_url = "127.0.0.1:5432"
        self.__postgresql_user = "postgres"
        self.__postgresql_pw = "n0m3l0"
        self.__postgresql_db = "usermgmnt"

    def get_connection(self):
    
        db_url = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
            user = self.__postgresql_user,
            pw = self.__postgresql_pw,
            url = self.__postgresql_url,
            db = self.__postgresql_db        
        )
        return db_url
    
    def enable_connection(self, app):
        return SQLAlchemy(app)