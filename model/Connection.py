from credentials import LINKEDIN_URL
from time import sleep
class Connection:

    def __init__(self,name,profile):
        self.name = name
        self.profile = profile
        
    def sendMessage(self,browser,selector,message,webDriver):
            print(self.profile,self.name)
            browser.get("https://www.linkedin.com" + self.profile)
            sleep(5)
        try:
            selector("class","pv-s-profile-actions--message").click()
            selector("class","msg-form__placeholder").click()
            action = webDriver.ActionChains(browser)
            action.move_to_element(selector("class","msg-form__contenteditable"))
            sleep(2)
            action.click()
            action.send_keys("what popiang")
            action.perform()
        except:
            self.sendMessage()
        # selector("class","msg-form__contenteditable").sendkeys(message)
        # selector("class","msg-form__send-button").click()
        # last_person = open(cons.LAST_CONNECTION_SENT,"w")
        # last_person.write(f"{self.name} {self.name}")
        # last_person.close()
