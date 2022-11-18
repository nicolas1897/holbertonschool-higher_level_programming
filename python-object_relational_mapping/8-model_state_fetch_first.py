#!/usr/bin/python3
'''
This module lists all states from the database hbtn_0e_0_usa
sorted in ascending order by states.id
'''
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    connection = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    eng = create_engine(connection.format(user_name, password, db_name),
                        pool_pre_ping=True)
    Session = sessionmaker(bind=eng)
    session = Session()
    item = session.query(State).first()
    if item is None:
        print("Nothing")
    else:
        print("{}: {}".format(item.id, item.name))
