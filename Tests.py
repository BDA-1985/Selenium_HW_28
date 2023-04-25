import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import settings


# UI/AU/RT-001
def test_open_page_auth(browser):
    auth = browser.find_element(By.CLASS_NAME, 'card-container__title')
    assert auth.text == 'Авторизация', 'Fail'


# UI/AU/RT-002
def test_change_tab_on_email(browser):
    browser.find_element(By.ID, 'username').send_keys(settings.mail)
    browser.find_element(By.ID, 'password').click()
    assert browser.find_element(By.XPATH, '//div[contains(@class, "rt-tab--active")]').text == 'Почта'


# UI/AU/RT-003
def test_change_tab_on_login(browser):
    browser.find_element(By.ID, 'username').send_keys(settings.login)
    browser.find_element(By.ID, 'password').click()
    assert browser.find_element(By.XPATH, '//div[contains(@class, "rt-tab--active")]').text == 'Логин'


# UI/AU/RT-004
def test_change_tab_on_personal_account(browser):
    browser.find_element(By.ID, 'username').send_keys(settings.lc_id)
    browser.find_element(By.ID, 'password').click()
    assert browser.find_element(By.XPATH, '//div[contains(@class, "rt-tab--active")]').text == 'Лицевой счёт', 'FAIL'


# UI/AU/RT-005
def test_change_from_personal_account_to_phone_number(browser):
    browser.find_element(By.ID, 't-btn-tab-ls').click()
    browser.find_element(By.ID, 'username').send_keys(settings.phone)
    browser.find_element(By.ID, 'password').click()
    assert browser.find_element(By.XPATH, '//div[contains(@class, "rt-tab--active")]').text == 'Телефон'


# UI/AU/RT-006
def test_change_from_email_to_phone_number(browser):
    browser.find_element(By.ID, 't-btn-tab-mail').click()
    browser.find_element(By.ID, 'username').send_keys(settings.phone)
    browser.find_element(By.ID, 'password').click()
    assert browser.find_element(By.XPATH, '//div[contains(@class, "rt-tab--active")]').text == 'Телефон'


# UI/AU/RT-007
def test_change_from_login_to_email(browser):
    browser.find_element(By.ID, 't-btn-tab-login').click()
    browser.find_element(By.ID, 'username').send_keys(settings.phone)
    browser.find_element(By.ID, 'password').click()
    assert browser.find_element(By.XPATH, '//div[contains(@class, "rt-tab--active")]').text == 'Почта'


# UI/AU/RT-008
def test_change_tab_on_personal_account(browser):
    browser.find_element(By.ID, 'forgot_password').click()
    assert browser.find_element(By.CLASS_NAME, 'card-container__title').text == 'Восстановление пароля'


# UI/AU/RT-009
def test_agreement(browser):
    browser.find_element(By.XPATH, '//div[@class="auth-policy"]/a').click()
    browser.switch_to.window(browser.window_handles[1])
    title = browser.find_element(By.XPATH, '//div[@id="title"]/h1').text
    assert title.startswith('Публичная оферта'), 'FAIL'


# UI/AU/RT-010
def test_auth_vk(browser):
    browser.find_element(By.ID, 'oidc_vk').click()
    assert 'vk.com' in browser.find_element(By.XPATH, '//div[@class="oauth_head"]/a').get_attribute('href')
    assert 'vk' in browser.current_url


# UI/AU/RT-011
def test_auth_ok(browser):
    browser.find_element(By.ID, 'oidc_ok').click()
    assert 'Одноклассники' == browser.find_element(By.XPATH, '//div[@class="ext-widget_h_tx"]').text
    assert 'ok' in browser.current_url


# UI/AU/RT-012
def test_auth_google(browser):
    browser.find_element(By.ID, 'oidc_google').click()
    assert 'google' in browser.current_url


# UI/AU/RT-013
def test_auth_mail(browser):
    browser.find_element(By.ID, 'oidc_mail').click()
    assert 'mail.ru' in browser.find_element(By.XPATH, '//span[@class="header__logo"]').text.lower()
    assert 'mail' in browser.current_url


# UI/AU/RT-014
def test_auth_yandex(browser):
    browser.find_element(By.ID, 'oidc_ya').click()
    WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.ID, 'passp:sign-in')))
    assert 'yandex' in browser.current_url


# UI/AU/RT-015
def test_redirect_cookie(browser):
    browser.find_element(By.ID, 'cookies-tip-open').click()
    assert browser.find_element(By.XPATH, '//span[@class="rt-tooltip__title"]').text == 'Мы используем Cookie'


# UI/AU/RT-016
def test_redirect_registration(browser):
    browser.find_element(By.ID, 'kc-register').click()
    assert browser.find_element(By.XPATH, '//h1[@class="card-container__title"]').text == 'Регистрация'


# UI/AU/RT-017
def test_privacy_policy_footer(browser):
    browser.find_elements(By.XPATH, '//a[@id="rt-footer-agreement-link"]/span')[0].click()
    browser.switch_to.window(browser.window_handles[1])
    title = browser.find_element(By.XPATH, '//div[@id="title"]/h1').text
    assert title.startswith('Публичная оферта'), 'FAIL'


# UI/AU/RT-018
def test_agreements_footer(browser):
    browser.find_elements(By.XPATH, '//a[@id="rt-footer-agreement-link"]/span')[1].click()
    browser.switch_to.window(browser.window_handles[1])
    title = browser.find_element(By.XPATH, '//div[@id="title"]/h1').text
    assert title.startswith('Публичная оферта'), 'FAIL'


# UI/AU/RT-019
def test_auth_incorrect_mail(browser):
    inputs = browser.find_elements(By.XPATH, '//input[contains(@class, "rt-input__input")]')
    inputs[0].send_keys(settings.mail)
    inputs[1].send_keys(settings.password)
    browser.find_element(By.ID, 'kc-login').click()
    assert browser.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль'


def test_auth_incorrect_password_for_phone(browser):
    inputs = browser.find_elements(By.XPATH, '//input[contains(@class, "rt-input__input")]')
    inputs[0].send_keys(settings.phone)
    browser.find_element(By.ID, 'kc-login').click()
    assert browser.find_element(By.ID, 'form-error-message').text == 'Неверный пароль'
