'''
Data models
'''

from sqlalchemy import (Column,
        String, Integer, Float, create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)

engine = create_engine('sqlite:///db.sqlite3')
db_session = scoped_session(sessionmaker(autocommit=False,
    autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    password_hash = Column(String)

def main(args):

    if len(args) > 1:
        if args[1] == 'create':
            Base.metadata.create_all(engine)
        elif args[1] == 'drop':
            Base.metadata.drop_all(engine)
        else:
            pass


if __name__=='__main__':

    from sys import argv

    main(argv)
