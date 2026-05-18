from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    _BUTTON_SELECTOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Click me!")')
    _GREETING_SELECTOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textStartsWith("Compose: ")')
    _IMAGE_SELECTOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Image")')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_button(self):
        self.wait.until(EC.element_to_be_clickable(self._BUTTON_SELECTOR)).click()

    def get_button(self):
        return self.wait.until(EC.presence_of_element_located(self._BUTTON_SELECTOR))

    def get_greeting_text(self):
        return self.wait.until(EC.presence_of_element_located(self._GREETING_SELECTOR)).text

    def is_greeting_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self._GREETING_SELECTOR))
            return True
        except Exception:
            return False

    def is_greeting_hidden(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element_located(self._GREETING_SELECTOR)
            )
            return True
        except Exception:
            return False

    def is_image_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self._IMAGE_SELECTOR))
            return True
        except Exception:
            return False
