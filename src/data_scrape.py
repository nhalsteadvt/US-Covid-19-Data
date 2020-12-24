import requests
import lxml.html as lh
import pandas as pd

class State:
    def __init__(self, name, cases, deaths, recovered, tests, population):
        self.name = (name[:7] + '.') if len(name) > 8 else name
        self.cases = int(cases.replace(',',''))
        self.deaths = int(deaths.replace(',',''))
        if(recovered == "N/A "):
            self.recovered = 0
        else:
            self.recovered = int(recovered.replace(',',''))
        self.tests = int(tests.replace(',',''))
        self.population = int(population.replace(',',''))
        self.active = self.cases - self.deaths - self.recovered
    
    def format(self):
        ans = "State: "+self.name+"\t|\tcases: "+str(self.cases)+" |\tdeaths: "+str(self.deaths)
        ans+=" |\trecovered: "+str(self.recovered)+" |\tactive: "+str(self.active)
        ans+=" |\ttests: "+str(self.tests)+" |\tpopulation: "+str(self.population)
        return ans


def parseData(str):
    #print("in: "+str)
    split = str.splitlines()
    #for i in split:
        #print("printing: "+i)
    return State(split[3], split[4], split[8], split[11], split[17], split[20])



url='https://www.worldometers.info/coronavirus/country/us/'

#Create a handle, page, to handle the contents of the website
page = requests.get(url)
#Store the contents of the website under doc
doc = lh.fromstring(page.content)
#Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath("//tr")


#Check the length of the first 65 rows
for T in tr_elements[2:53]:
    #print(str(tr_elements.index(T))+" - "+T.text_content())
    abc = parseData(T.text_content())
    print(abc.format())
    #print("thing: " + str(T.text_content()))

