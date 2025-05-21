import allure
import allure_commons.model2
from allure_commons.types import Severity
import selene
from selene import  browser, by, be
from selene.support.shared.jquery_style import s

@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "ErmilovaDV")
@allure.feature("Decorators_step")
@allure.story("Try_use_derocators")
@allure.link("https://github.com", name="Testing")

def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-integration-example")
    go_to_repository("eroshenkoam/allure-integration-example")
    open_issues_tab()
    should_see_text("No result")


@allure.step("Opening main page")
def open_main_page():
    browser.open("https://github.com")
    browser.driver.fullscreen_window()


@allure.step("Repository searching {repo}")
def search_for_repository(repo):
    browser.element('.search-input').click()
    browser.element('#query-builder-test').send_keys(repo).press_enter()


@allure.step("Goto repo-link {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Open Issuses Tab")
def open_issues_tab():
    browser.element("#issues-tab").click()


@allure.step("Check for text appears {text}")
def should_see_text(text):
    s(by.text("No results")).should(be.visible)

