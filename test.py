from bs4 import BeautifulSoup
from testT import g

soup = BeautifulSoup(g,"lxml")
x = soup.findAll("a", {"class": "search-result__result-link"})

new_connection = []
ctr = 0
for i in x:
    connectionName = i.find("img")
    if ctr % 2 == 0:
        if connectionName:
            print(connectionName["alt"])
            print(i["href"])    
            new_connection.append(Connection(connectionName["alt"],i["href"]))
        else:
            new_connection.append(Connection(None,i["href"]))
            
            
    ctr+=1
print(new_links)

# with open() as file_in:
#              test = " "
#              for line in file_in:
#                  test = line.split()
#                  if not test == []:
#                      self.push("".join(test))


