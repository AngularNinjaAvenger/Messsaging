from bs4 import BeautifulSoup
from Connections import Connections as Conss
from Authentication import Authentication as auth
class main:
    def __init__(self):
        self.b = "browser" 
    def main():
        auth.auth(self.b,self.selector)
        cons = Conss()
        if cons.toBeMessaged():
            cons.getConnection(self.b,self.selector,self.soup)
        
        cons.loadConnections()
        
        # get list of connections
                # send message
    def selector(self,selector,name):
        if selector == "tag":
			return self.b.find_element_by_tag_name(name)
			pass
		elif selector == "id":
			return self.b.find_element_by_id(name)
		elif selector == "class":
			return self.b.find_element_by_class_name(name)
			pass
		else:
			return False
    def soup(self):
        t_soup = BeautifulSoup(self.browser.page_source, "lxml")
		return t_soup