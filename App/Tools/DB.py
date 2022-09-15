from sqlalchemy import create_engine, Column, Integer, Unicode, BigInteger
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from Models.Solution import Solution

def init_db(user, pwd, host, port, db):
    connection_string = f'postgresql://{user}:{pwd}@{host}:{port}/{db}'
    if not database_exists(connection_string):
        create_database(connection_string)

    # Start engine
    engine = create_engine(connection_string)
    return engine

def get_default_engine():
    engine = init_db(
        user= 'postgres',
        pwd= 'postgres',
        host= 'db',
        port= '5432',
        db= 'queens'
    )
    return engine

Base = declarative_base(bind= get_default_engine())

class SolutionTableModel(Base):
    __tablename__ = 'Solutions'
    id = Column(Integer, primary_key= True,  autoincrement=True)
    total = Column(BigInteger)
    n_queens = Column(Integer)
    method = Column(Unicode(12))
    runtime = Column(Unicode(32))

    def __init__(self, solution: Solution):
        self.total = solution.total
        self.n_queens = solution.n_queens
        self.method = solution.method
        self.runtime = solution.timestamp

    def __repr__(self):
        return f'<Solution(id={self.id}, n={self.n_queens}, total={self.total}, runtime={self.runtime})>'

def get_session(engine= None) -> sessionmaker:
    if not engine:
        engine = get_default_engine()
    session = sessionmaker(bind= engine)
    return session

def create_model() -> bool:
    engine = get_default_engine()

    try:
        Base.metadata.create_all()
        engine.dispose()
        print('Model created successfully')
        return True
    except Exception as e:
        print('Model creation error:', e)
        return False

def add_solution(data: Solution) -> None:
    Session = get_session()

    solution = SolutionTableModel(data)

    current_session = Session()
    current_session.add(solution)
    current_session.commit()

    print('Added to DB!')

    current_session.close()

def get_stored_solutions() -> list:
    Session = get_session()
    current_session = Session()

    result = current_session.query(SolutionTableModel).all()

    # print('Q solutions:')
    # for entry in result:
    #     print(entry)
    
    current_session.close()
    return result

if __name__ == "__main__":
    create_model()