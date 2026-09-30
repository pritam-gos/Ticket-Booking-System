def check_reservation():
    g = int(input("Enter your 10 digit PNR number: "))
    if g > 9999999999 or g < 1000000000:
        print("number invalid")
    else:
        h = int(input("Enter your last waiting list number:"))
        if h <= 20:
            print(f" Your ticket with PNR {g} has confirmation rate above 90%")
        elif h > 20 or h <= 50:
            print(f" Your ticket with PNR {g} has confirmation rate above 50%")
        elif h > 50 or h <= 100:
            print(f" Your ticket with PNR {g} has confirmation rate above 20%")
        else:
            print(f" Your ticket with PNR {g} has confirmation rate below 20%")
        print("Thank You!")