import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_setup():
    browser.config.window_height = 1080  # задает высоту окна браузера
    browser.config.window_width = 1920  # задает ширину окна браузера
    browser.config.base_url = "https://google.com"
    yield
    browser.quit()
