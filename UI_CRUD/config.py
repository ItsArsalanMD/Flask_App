# config.py

class Config:
    SECRET_KEY = '2b77ff6e5d9ebf0c40c914d6be3423af732c7eaaf85e1a32'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:123@localhost/crud'
    SQLALCHEMY_TRACK_MODIFICATIONS = False