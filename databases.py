from model import Base, User, Post

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

def add_user(name, password):
	
	session = session_factory()
	print("Added a user!")
	user = User(name = name, password = password)
	session.add(user)
	session.commit()