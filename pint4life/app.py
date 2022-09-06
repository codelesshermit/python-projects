def request_donation():
    print("Hello and Welcome to Pint4life:")
    query_1 = input("Are you looking to donate or get a donor? Reply with Donate or get donor").lower()
    if query_1 == "donate":
        print("Welcome and thank you, we will redirect you to donation page")
    elif query_1 == "get donor":
        print("Welcome and thank you, we will direct you to request donation page")
    else:
        print("I dont understand your request")


request_donation()
def check_available_donors():
    pass