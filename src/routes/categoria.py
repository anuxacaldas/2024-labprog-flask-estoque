import sqlalchemy as sa
from flask import Blueprint, render_template
from src.models.categoria import Categoria
from src.modules import db

bp = Blueprint('categoria',
               __name__,
               url_prefix='/categoria')


@bp.route('/', methods=['GET', 'POST'])
def lista():
    sentenca = sa.select(Categoria).order_by(Categoria.nome)
    rset = db.session.execute(sentenca).scalars()

    return render_template('categoria/lista.jinja2',
                           rset=rset)
