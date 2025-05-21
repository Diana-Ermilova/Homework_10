import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s

def test_open_browser():

    with allure.step("GitHub main page open"):
        browser.open("https://github.com")
        browser.driver.fullscreen_window()

    with allure.step("Search repository eroshenkoam/allure-example"):
        browser.element('.search-input').click()
        browser.element('#query-builder-test').send_keys("eroshenkoam/allure-integration-example").press_enter()

    with allure.step("Go to repo-link"):
        browser.element(by.link_text("eroshenkoam/allure-integration-example")).press_enter()

    with allure.step("Open 'Issues' Tab"):
        browser.element("#issues-tab").click()

    with allure.step("Check that label 'No results' appears"):
        s(by.text("No results")).should(be.visible)

#def test_void():
#    return


