import unittest
from ZenDeskAPIHandler import APIHandler;
class TestStringMethods(unittest.TestCase):
    def test_Authenticate_user(self):
        message = APIHandler.authenticate_user("","")
        self.assertEqual(message, "User successfully authenticates")

    def test_Get_Valid_Ticket_Detail(self):
        ticket = APIHandler.get_a_ticket_details("23")
        self.assertIsNotNone(ticket)

    def test_Get_InValidID_Ticket_Detail(self):
        ticket = APIHandler.get_a_ticket_details("-1")
        self.assertIsNone(ticket)        

    def test_Get_InValidURL_TwentyFiveTickets(self):
        ticket = APIHandler.get_twentyfive_tickets("-1")
        self.assertIsNone(ticket)    

    def test_Get_ValidURL_TwentyFiveTickets(self):
        ticket = APIHandler.get_twentyfive_tickets()
        self.assertEqual(len(ticket),  25)     

    def test_Get_ValidURL_NoTickets_TwentyFiveTickets(self):
        ticket, prev, next = APIHandler.get_twentyfive_tickets("https://zccnetraamrale.zendesk.com/api/v2/tickets?page%5Bbefore%5D=eyJvIjoibmljZV9pZCIsInYiOiJhUUVBQUFBQUFBQUEifQ%3D%3D&page%5Bsize%5D=25")
        self.assertIsNotNone(ticket)  
        self.assertEqual(len(ticket),0 , msg=f"Length of tickets is {len(ticket)}")  
        self.assertIsNone(prev)       
        self.assertIsNone(next)


if __name__ == '__main__':
    unittest.main()