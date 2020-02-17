# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import scoped_session, sessionmaker, relationship
#
# engine = create_engine('sqlite:///atividade.db', convert_unicode=True)
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          binds=engine))
# Base = declarative_base()
# Base.query = db_session.query_property()


from app import db


class Pessoas(db.Model):
    __tablename__ = 'pessoas'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), index=True)
    idade = db.Column(db.Integer)

    def __repr__(self):
        return '<Pessoa {}>'.format(self.nome)


class Atividades(db.Model):
    __tablename__ = 'atividades'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoas.id'))

    pessoa = db.relationship("Pessoas")

    def __repr__(self):
        return '<Atividade {}>'.format(self.nome)

# class Pessoas(Base):
#     __tablename__ = 'pessoas'
#     id = Column(Integer, primary_key=True)
#     nome = Column(String(40), index=True)
#     idade = Column(Integer)
#
#     def __repr__(self):
#         return '<Pessoa {}>'.format(self.nome)
#
#
# class Atividades(Base):
#     __tablename__ = 'atividades'
#     id = Column(Integer, primary_key=True)
#     nome = Column(String(80))
#     pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
#
#     pessoa = relationship("Pessoas")
#
#
# def init_db():
#     Base.metadata.create_all(bind=engine)
#
#
# if __name__ == '__main__':
#     init_db()
