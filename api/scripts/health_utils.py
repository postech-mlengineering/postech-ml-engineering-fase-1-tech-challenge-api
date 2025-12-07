import logging
from api.models.books import Books


logger = logging.getLogger('api.scripts.health_utils')


def check_db_connection():
    '''
    Executa uma consulta simples para verificar a conexão e o status do banco de dados.

    Return:
        bool: True se a consulta for bem-sucedida, False caso contrário.
    '''
    try:
        Books.query.limit(1).all()
        return True
    except Exception as e:
        logger.error(f'error: {e}')
        return False
    