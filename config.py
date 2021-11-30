


class Config:
    def __init__(self):                  
        self.BASE_URL = "https://zccnetraamrale.zendesk.com"
        self.CREDENTIALS = ""
        self.HEADERS = {'Authorization' : f"Basic {self.CREDENTIALS}" , "Content-Type" : "application/json"}       
   
    def edit_header(self, credentials):
         self.CREDENTIALS = credentials
         self.HEADERS = {'Authorization' : f"Basic {self.CREDENTIALS}" , "Content-Type" : "application/json"}       
   
class Json_keys:
        SUBJECT = "subject"
        TICKETS = "tickets"
        TICKET = "ticket"
        ID = "id"
        LINKS = "links"
        PREV = "prev"
        NEXT = "next"

config_Obj = Config()        


    
