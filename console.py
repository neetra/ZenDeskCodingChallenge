from ZenDeskAPIHandler import APIHandler;
import logging
from helper import Helper;
from Constants import MAIN_MENU, GET_MAIN_MENU_INPUT, MENU_GET_ALL_TICKET_DETAILS

def get_ticket_details_menu():
    try:
        ticketID = input("Enter Ticket Id : ")
        ticket_details = APIHandler.get_a_ticket_details(ticketID)
        tds = Helper.get_a_ticket_string(ticket_details)
        print(tds)
    except (RuntimeError, TypeError, NameError) as e:
        logging.error(f" Error occured in 'get_ticket_details_menu' :  {e}")            

def authenticate_user():
    try:      
        emailId = input("Enter the email id : ")
        password = input("Enter the password : ")
        messsage = APIHandler.authenticate_user(emailId, password)  
        print(messsage)
    except (RuntimeError, TypeError, NameError) as e:
        logging.error(f" Error occured in 'authenticate_user' :  {e}")  

def print_multiple_tickets(tickets):   
    for ticket in tickets:
        tsd = Helper.get_a_ticket_string(ticket)
        print(tsd + "\n")

def get_all_tickets_menu()    :
    try:          
       
        input_option = "" 
        url =None

        while(input_option != 'q'):
            tickets, prev, next = APIHandler.get_twentyfive_tickets(url)
            
            print_multiple_tickets(tickets)           
            input_option = input(MENU_GET_ALL_TICKET_DETAILS)
            if(input_option == 'n' and next != None)        :
                    url =next
            elif(input_option == 'p' and prev != None)        :
                    url =prev  
            else:
                if(input_option != 'q'):                    
                   input_option= print("No new tickets found. Enter 'q' to quit")                            

    except (RuntimeError, TypeError, NameError) as e:
        logging.error(f" Error occured in 'get_all_tickets_menu' :  {e}")        
 

def default():
    return "Invalid option, enter 'q' to quit"   

switcher = {  
    '1':authenticate_user,
    '2': get_ticket_details_menu,
    '3' : get_all_tickets_menu
    }

def switch(day):
    return switcher.get(day, default)()

def main_menu(menu_id=""):         
    while(menu_id != 'q'):    
        print(MAIN_MENU)
        menu_id = input(GET_MAIN_MENU_INPUT)
        switch(menu_id)

main_menu()        


  
