from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session, sessionmaker

class Base(DeclarativeBase):
    pass

class Users(Base):  # Estrutura para criar uma tabela
    __tablename__ = "mailling"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def __repr__(self):
        return f"Client {self.name}, CNPJ: {self.email}"

    def return_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
        }

# Cria banco de dados caso ele não exista e estabelece conexão
engine = create_engine('sqlite+pysqlite:///app.db', echo=True)

# Estabelece sessão
Session = sessionmaker(bind=engine)
session = Session()

# Cria tabelas caso elas não existam
Base.metadata.create_all(engine)

# creating a user
user = Users(name='João', email='henrique@gmail.com')
session.add(user)
session.commit()

# editing a user
user = session.query(Users).filter_by(name='João').first()
user.email = "joaobobao@gmail.com"
session.commit()

# deleting a user
user = session.query(Users).filter_by(name='João').first()
session.delete(user)
session.commit()

# getting user
user = session.query(Users).filter_by(name='João').first()
print(user)
