import re

class dataModel:
    publisheValues = ["Mamad", "Arvin", "Kiarash", "Shayan", "Omid", "Alex", "Andrew", "Fransic"]

    def getWithKeywords(self, keyword: str):
        return list(filter(lambda x: re.search(keyword, x, re.IGNORECASE), self.publisheValues))
    
    def getUserData(id: str):
        return None
    
    def getPlayerData(id: str):
        return None
    
    def getTeamData(id: str):
        return None
    
    
