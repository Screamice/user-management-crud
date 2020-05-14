from sqlalchemy import create_engine
import os

URL = os.environ["POSTGRESQL_URL"]
USER = os.environ["POSTGRESQL_USER"]
PW = os.environ["POSTGRESQL_PW"]
DATABASE = "simpleComments"

DB_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=USER, pw=PW, url=URL, db=DATABASE)