from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasketPageLocators:
    TOP_BASKET_BUTTON = (By.CSS_SELECTOR, "a[class='btn btn-default']")
    ITEMS_TO_BY = (By.CSS_SELECTOR, "#content_inner .col-sm-6.h3")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner p")


class LoginPageLocators:
    LOGIN_URL = ("http://selenium1py.pythonanywhere.com/en-gb/accounts/login/")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_FORM_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_FORM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_FORM_LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[name="login_submit"]')
    REGISTERED_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTERED_FORM_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTERED_FORM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTERED_FORM_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTERED_FORM_REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NOTICE_PRODUCT_ADD_SUCCESSFUL = (By.CSS_SELECTOR, '.alertinner ')
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".basket-mini ")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
