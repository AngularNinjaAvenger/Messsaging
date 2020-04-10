from authenticationCredentials import authCred
from time import sleep
class Authentication:
    def auth(browser,selector):
        browser.get(authCred.LOGIN_URL)
        emailElement = selector("id",authCred.EMAIL_SELECTOR) 
        emailElement.send_keys(authCred.EMAIL)
        passElement = selector("id",authCred.PASSWORD_SELECTOR)
        passElement.send_keys(authCred.PASSWORD)
        passElement.submit()
        sleep(3)