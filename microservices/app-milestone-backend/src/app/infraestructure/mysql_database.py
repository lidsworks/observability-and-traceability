from os import environ

class DataBaseConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{environ.get('MYSQL_DB_USER')}:{environ.get('MYSQL_DB_PASSWORD')}@{environ.get('MYSQL_DB_HOST')}/{environ.get('MYSQL_DB_NAME')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_TABLE_PREFIX = f"{environ.get('MYSQL_DB_TABLE_PREFIX')}"