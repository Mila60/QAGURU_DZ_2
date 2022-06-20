import pytest
from selene import be, have
from selene.support.shared import browser


@pytest.fixture(scope='session', autouse=True)
def before_each():
    browser.open('https://google.com')


@pytest.fixture()
def size(before_each):
    browser.config.window_width = 1930
    browser.config.window_height = 1260


def test_first(before_each, size):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_second(before_each, size):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selenium - User-oriented Web UI browser tests in Python'))
