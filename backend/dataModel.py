import re


# the model for accessing the database. access and write queries in this class
class dataModel:
    publisheValues = ["Mamad", "Arvin", "Kiarash", "Shayan", "Omid", "Alex", "Andrew", "Fransic"]

    def metaData():
        return {
            'name' : 'MySportsData',
            'version': '0.1',
            'team': "Groupe14"
        }

    def getWithKeywords(self, keyword: str):
        return list(filter(lambda x: re.search(keyword, x, re.IGNORECASE), self.publisheValues))
    
    def getUserData(id: str):
        return None
    
    def getPlayerData(id: str):
        return None
    
    def getTeamData(id: str):
        return None
    
    
