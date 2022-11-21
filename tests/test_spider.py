import pytest

from src.spider import DrogaRaiaSpider
from tests.responses import fake_response

@pytest.fixture
def request_mock(mocker):
    return mocker.patch("src.spider.scrapy.Request")

def get_config(only_first_page=None):
    basic_config = {
        "start_urls":["https://www.foo.com.br/bar.html"],
        "url_file_path": "url_products.txt",
        "info_file_path": "info_products.txt"
    }
    if only_first_page is not None:
        basic_config["only_first_page"] = only_first_page
    return basic_config

def test_parse_whit_only_single_page_true(mocker, request_mock):
    
    mocker.patch("src.spider.load_config",return_value=get_config(True))
    
    spider = DrogaRaiaSpider()
    expected = [
        "https://www.foo.com.br/losartana-potassica-50mg-medley-generico-com-30-comprimidos.html",
        "https://www.foo.com.br/needs-auto-teste-rapido-antigeno-covid-1-unidade.html",
    ]
    response = fake_response("fake_products.html")
    spider.parse(response)
    assert spider.products == expected
    assert request_mock.not_called()

def test_parse_whit_only_single_page_false(mocker,request_mock):
    
    mocker.patch("src.spider.load_config",return_value=get_config(False))
    
    spider = DrogaRaiaSpider()
    
    expected = [
        "https://www.foo.com.br/losartana-potassica-50mg-medley-generico-com-30-comprimidos.html",
        "https://www.foo.com.br/needs-auto-teste-rapido-antigeno-covid-1-unidade.html",
    ]
    response = fake_response("fake_products.html")
    spider.parse(response)
    assert spider.products == expected
    assert request_mock.called_once()


def test_parse_whithout_only_single_page(mocker,request_mock):
    
    mocker.patch("src.spider.load_config",return_value=get_config())
    
    spider = DrogaRaiaSpider()
    expected = [
        "https://www.foo.com.br/losartana-potassica-50mg-medley-generico-com-30-comprimidos.html",
        "https://www.foo.com.br/needs-auto-teste-rapido-antigeno-covid-1-unidade.html",
    ]
    response = fake_response("fake_products.html")
    spider.parse(response)
    assert spider.products == expected
    assert request_mock.called_once()

def test_parse_whit_no_products(mocker,request_mock):
    
    spider = DrogaRaiaSpider()
    expected = []
    response = fake_response("fake_products_with_no_product.html")
    spider.parse(response)
    assert spider.products == expected
    assert request_mock.called_once()

def test_parse_whithout_next_page(mocker,request_mock):
    
    spider = DrogaRaiaSpider()
    expected = [
        "https://www.foo.com.br/losartana-potassica-50mg-medley-generico-com-30-comprimidos.html",
        "https://www.foo.com.br/needs-auto-teste-rapido-antigeno-covid-1-unidade.html",
    ]
    response = fake_response("fake_products_without_next_page.html")
    spider.parse(response)
    assert spider.products == expected
    assert request_mock.not_called()