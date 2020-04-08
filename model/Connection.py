from credentials import LINKEDIN_URL
from time import sleep
class Connection:

    def __init__(self,name,profile):
        self.name = name
        self.profile = profile
        
    def sendMessage(self,browser,selector,message):
        browser.get(LINKEDIN_URL+self.profile)
        sleep(5)
        selector("class","pv-s-profile-actions--message").click()
        selector("class","msg-form__contenteditable").click()
        selector("class","msg-form__contenteditable").sendkeys(message)
        last_person = open(cons.LAST_CONNECTION_SENT,"w")
        last_person.write(f"{self.name} {self.name}")
        last_person.close()
