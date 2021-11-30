from config import Json_keys;
class Helper:
    def get_a_ticket_string(ticket_details):

        # Reference : https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python/17303428
        BOLD= '\033[1m'
        END = '\033[0m'
        GREEN = '\033[92m'
        return f"{GREEN}TicketId :{END}{ticket_details[Json_keys.ID]}  {GREEN}Subject :{END}{ticket_details[Json_keys.SUBJECT]}"