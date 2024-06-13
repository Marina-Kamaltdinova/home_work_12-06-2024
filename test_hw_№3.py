from selene import browser, have


def test_valid():
    browser.open('')
    browser.element('[name="q"]').type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_invalid():
    browser.open('')
    browser.element('[name="q"]').type('gfbddvvfsdbcthj756599').press_enter()
    browser.element('.card-section').should(have.text('По запросу gfbddvvfsdbcthj756599 ничего не найдено.'))