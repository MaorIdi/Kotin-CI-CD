import pytest
from pages.main_page import MainPage


@pytest.fixture
def page(driver):
    return MainPage(driver)


class TestMainScreenLaunch:
    def test_app_launches(self, page):
        button = page.get_button()
        assert button.is_displayed()

    def test_button_text(self, page):
        button = page.get_button()
        assert button.text == "Click me!"

    def test_greeting_hidden_on_launch(self, page):
        assert page.is_greeting_hidden()


class TestClickMeButton:
    def test_click_reveals_greeting(self, page):
        page.click_button()
        assert page.is_greeting_visible()

    def test_greeting_text_contains_hello(self, page):
        page.click_button()
        text = page.get_greeting_text()
        assert "Hello" in text

    def test_greeting_text_starts_with_compose(self, page):
        page.click_button()
        text = page.get_greeting_text()
        assert text.startswith("Compose: ")

    def test_greeting_text_android_platform(self, page):
        page.click_button()
        text = page.get_greeting_text()
        assert "Android" in text

    def test_click_reveals_image(self, page):
        page.click_button()
        assert page.is_image_visible()


class TestToggleBehavior:
    def test_second_click_hides_greeting(self, page):
        page.click_button()
        assert page.is_greeting_visible()
        page.click_button()
        assert page.is_greeting_hidden()

    def test_third_click_shows_greeting_again(self, page):
        page.click_button()
        page.click_button()
        page.click_button()
        assert page.is_greeting_visible()

    def test_button_always_visible_after_toggle(self, page):
        page.click_button()
        page.click_button()
        assert page.get_button().is_displayed()
