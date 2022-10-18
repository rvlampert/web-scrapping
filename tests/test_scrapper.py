from unittest.mock import mock_open, patch
from src.scrapper import DrogaRaiaScrapper, get_products_urls, string_to_dict
from tests.responses import fake_response


import unittest.mock as um

def test_parse(mocker):
    basic_config = {
        "url_file_path": "url_products.txt",
        "info_file_path": "info_products.txt"
    }
    mocker.patch("src.scrapper.load_config",return_value=basic_config)

    with patch('builtins.open', mock_open(read_data='url from a certain product')):
        scrapper = DrogaRaiaScrapper()

    expected = ['Nome="Losartana Potássica 50mg 30 comprimidos Medley Genérico" Preco=R$6.45 SKU=81741',]
    response = fake_response("fake_single_product.html")
    scrapper.parse(response)
    assert scrapper.products == expected

def test_get_products_url():
    basic_config = {
        "url_file_path": "url_products.txt",
        "info_file_path": "info_products.txt"
    }
    url = 'url from a certain product'
    with patch('builtins.open', mock_open(read_data='url from a certain product')):
        result = get_products_urls(basic_config)
        assert [url] == result

def test_string_to_dict():
    info = '<script type="application/ld+json">{"nome":"foo","preco":100}</script>'
    expected = {"nome":"foo","preco":100}
    result = string_to_dict(info)
    assert expected == result