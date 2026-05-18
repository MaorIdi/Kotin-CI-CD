import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from pages.main_page import MainPage

os.environ["ANDROID_HOME"] = r"C:\Users\Maor\AppData\Local\Android\Sdk"
os.environ["ANDROID_SDK_ROOT"] = r"C:\Users\Maor\AppData\Local\Android\Sdk"

APPIUM_SERVER = "http://127.0.0.1:4723"
APP_PACKAGE = "com.example.kmp_ci_cd"
APP_ACTIVITY = "com.example.kmp_ci_cd.MainActivity"


def pytest_addoption(parser):
    parser.addoption("--apk", action="store", default=None, help="Path to APK file")
    parser.addoption("--device", action="store", default=None, help="Device UDID")
    parser.addoption("--appium-url", action="store", default=APPIUM_SERVER)


@pytest.fixture(scope="session")
def driver(request):
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.android_sdk_root = r"C:\Users\Maor\AppData\Local\Android\Sdk"
    options.app_package = APP_PACKAGE
    options.app_activity = APP_ACTIVITY
    options.no_reset = False
    options.auto_grant_permissions = True

    apk = r"C:\Users\Maor\AndroidStudioProjects\KMPCICD\androidApp\build\intermediates\apk\debug\androidApp-debug.apk"
    if apk:
        options.app = apk

    device = request.config.getoption("--device")
    if device:
        options.udid = device

    server_url = request.config.getoption("--appium-url")

    d = webdriver.Remote(server_url, options=options)
    d.implicitly_wait(10)
    yield d
    d.quit()


@pytest.fixture(autouse=True)
def reset_app(driver):
    try:
        driver.implicitly_wait(0)
        elems = driver.find_elements(*MainPage._GREETING_SELECTOR)
        is_visible = bool(elems and elems[0].is_displayed())
        driver.implicitly_wait(10)
        if is_visible:
            MainPage(driver).click_button()
    except Exception:
        driver.implicitly_wait(10)
        driver.terminate_app(APP_PACKAGE)
        driver.activate_app(APP_PACKAGE)
    yield
