from app import db


def transacao(objeto):
    db.session.add(objeto)
    db.session.commit()
    db.session.close()


def excluir(objeto):
    db.session.delete(objeto)
    db.session.commit()
    db.session.close()


def listar(table, *order_by):
    return table.query.order_by(*order_by).all()
