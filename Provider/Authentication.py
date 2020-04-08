from Login import LoginInfo

class Authentication
    def auth(browser,selector):
        browser.get(LoginInfo.LOGIN_URL)
		emailElement = selector("id",LoginInfo.EMAIL_SELECTOR) 
		emailElement.send_keys(LoginInfo.EMAIL)
		passElement = selector("id",LoginInfo.PASSWORD_SELECTOR)
		passElement.send_keys(LoginInfo.PASSWORD)
		passElement.submit()
		time.sleep(3)