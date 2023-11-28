import logging

LOGGER = logging.getLogger(__name__)


def test_header_title(sale_page):
    sale_page.open_page()
    LOGGER.info('SOme comment')
    sale_page.check_page_header_title_is('Sale')
