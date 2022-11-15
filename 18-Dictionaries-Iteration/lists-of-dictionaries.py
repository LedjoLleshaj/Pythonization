concert_attendees = [
    {"name": "Rolf Smith", "age": 16, "ticket_price": 25},
    {"name": "Adam Wool", "age": 35 , "ticket_price": 50},
    {"name": "Anne Pun", "age": 19 , "ticket_price": 20},
]

for attendee in concert_attendees:
    for key,value in attendee.items():
        print (f"The {key} is {value}.")

