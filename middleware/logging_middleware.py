import logging
from flask import request

logging.basicConfig(level=logging.INFO)


def request_logger():
    logging.info(f'{request.method} {request.path}')
    logging.info(f'Body: {request.get_json()}')
