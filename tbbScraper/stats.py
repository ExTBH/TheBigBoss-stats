import imp
from typing import  List, Union
from requests import get, Response
from bs4 import BeautifulSoup
class Stats:
    url: str = "http://apt.thebigboss.org/stats.php?dev="
    def statsForDev(self, developer_id : str) -> Union[List[List], bool]:

        r: Response = get(self.url + developer_id)
        soup = BeautifulSoup(r.text,"html.parser")
        infoTable = soup.find("table","information")
        if infoTable == None:
            return False

        infoRow = infoTable.find_all("tr")
        tmpList: List = []
        for outterRow in infoRow:
            for innerRow in outterRow.find_all("td"):
                #Get rid of first tr Tag children > they'r garbage
                if innerRow.find("em") or len(innerRow.contents) == 0:
                    continue
                tmpList += innerRow.contents

        listCount = (len(infoRow)) - 1

        packages: List[List[str, str, int]] = []
        for _ in range(listCount):
            packages += [[tmpList[0], tmpList[1], int(tmpList[2])]]
            del tmpList[:3]
            
        return(packages)