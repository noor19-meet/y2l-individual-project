from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

def add_user(name, password):
	
	session = session_factory()
	print("Added a user!")
	user = User(name = name, password = password)
	session.add(user)
	session.commit()



def query_all_users():
	session = session_factory()
	return session.query(User).all()

def query_by_name(name):
	session = session_factory()
	return session.query(User).filter_by(name = name).first