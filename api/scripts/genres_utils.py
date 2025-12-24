import logging
from sqlalchemy import distinct
from api.models.books import Books


logger = logging.getLogger('__name__')


def get_all_genres():
    '''
    Retorna todas os gêneros de livros cadastrados.

    Retorna:
        list: Uma lista de dicionários.
    '''
    try:
        categories = (
            Books.query.with_entities(distinct(Books.genre)).order_by(Books.genre.asc()).all()
        )
        results = [{'genre': c[0]} for c in categories]
        return results
    except Exception as e:
        logger.error(f'error: {e}')
        return None