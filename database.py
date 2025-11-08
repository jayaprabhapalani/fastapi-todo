from sqlalchemy import create_engine;
from sqlalchemy.orm import sessionmaker,declarative_base;
from dotenv import load_dotenv;
import os;

'''creating database in postgresql using sqlalchemy 
 -declarative base is to make obj from sql row( just orm)
 
 in django there is an default db(sqllite) so we dont need to worry about db connection 
 but here we dont have any default db so we have to connect it with the use of sqlalchemy package
'''

load_dotenv()
DATABASE_URL=os.getenv("DATABASE_URL")
engine=create_engine(DATABASE_URL)
sessionLocal=sessionmaker(bind=engine,autoflush=False)
Base=declarative_base()
