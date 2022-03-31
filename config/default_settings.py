class Config(object):
    TESTING  =  False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://postgres:password@database.crykgm0yiisn.us-east-1.rds.amazonaws.com/postgres"
    #"sqlite:///development.db"
