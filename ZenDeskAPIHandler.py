import requests, base64;
from config import config_Obj, Json_keys
class APIHandler:
    def get_twentyfive_tickets(url =None):
        try:
            url = config_Obj.BASE_URL + "/api/v2/tickets?page[size]=25" if url is None else url
            response = requests.get(url, headers = config_Obj.HEADERS)   
            if(response.status_code == 200):
                response_json  = response.json()
                tickets = response_json[Json_keys.TICKETS]
                prev = response_json[Json_keys.LINKS][Json_keys.PREV]
                next =  response_json[Json_keys.LINKS][Json_keys.NEXT]          
                return tickets, prev, next
            else:
                print(f"Bad request {response.json()}"            )
        except (RuntimeError, TypeError, NameError, requests.RequestException) as e:
            print( f"Error in application {e}")
        return None        
            

    def get_a_ticket_details(ticketId):    
        try:
            url = config_Obj.BASE_URL + "/api/v2/tickets/"+ str(ticketId)
            response = requests.get(url, headers = config_Obj.HEADERS)   
            if(response.status_code == 200):
                response_json = (response.json())
                ticket_details  = response_json[Json_keys.TICKET]           
                return ticket_details;
            else:
                message = f"Record not found" if response.status_code == 404 else f"Error while connecting API. HTTPStatusCode{response.status_code}"
                print(message)              
        except (RuntimeError, TypeError, NameError,requests.RequestException) as e:
            return f"Error in 'get_a_ticket_details' {e}"
        return None  

    
    def authenticate_user(emailId, password):    
        try:
            url = config_Obj.BASE_URL + "/api/v2/users.json"       

            usrPass = f"{emailId}:{password}"
            bytes  = usrPass.encode("utf-8")
            b64Val = base64.b64encode(bytes)                       
            config_Obj.edit_header(b64Val.decode("utf-8"))          
            response = requests.get(url, headers = config_Obj.HEADERS)              
            if(response.status_code == 200):                                        
                return "User successfully authenticates";  
                
            else:
                return "Cannot authenticate user" 
        except (RuntimeError, TypeError, NameError,requests.RequestException) as e:
            return f"Error in 'authenticate_user' {e}"
                  
                                          
