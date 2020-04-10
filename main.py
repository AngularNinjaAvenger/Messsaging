from bs4 import BeautifulSoup
from selenium import webdriver
import credentials
import sys

sys.path.insert(1,credentials.PROVIDER_PATH)
sys.path.insert(2,credentials.MODEL_PATH)

from Authentication import Authentication as auth
from Connections import Connections as Conss


class main:
    def __init__(self):
        self.b = webdriver.Chrome(credentials.CHROME_DRIVE_PATH)
        		
    def main():
        auth.auth(self.b,self.selector)
        cons = Conss()
        if cons.toBeMessaged():
            cons.getConnection(self.b,self.selector,self.soup)
        message_file = open(credentials.MESSAGE_FILE_PATH,"r")
        message = message.read()
        
        lastPresent = False
        last = open(credentials.LAST_CONNECTION_SENT_MESSAGE_FILE_PATH,"r")
        if last == "":
            lastPresent = True
            
        for connection in cons.loadConnections():
            if not lastPresent:
                if f"{connection.name} {connection.profile}" == last:
                    lastPresent = True
                else:
                    continue
            connection.sendMessage(browser,selector,message)
        message_file.close()
        
    def selector(self,selector,name):
        if selector == "tag":
            return self.b.find_element_by_tag_name(name)
        elif selector == "id":
            return self.b.find_element_by_id(name)
        elif selector == "class":
            return self.b.find_element_by_class_name(name)
        else:
            return False
    def soup(self):
        t_soup = BeautifulSoup(self.browser.page_source, "lxml")
        return t_soup

main().main()
