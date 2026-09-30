def cancel_ticket():
    j = int(input("Your train number: "))
    if j < 10000 or j > 100000:
        print("number invalid")
    else:
        l = int(input("Enter your 4 digit booking ID: "))
        if l < 1000 or l > 10000:
            print("Number Invalid")
        else:
            m = input("Enter your departure station: ")
            n = input("Enter your arrival station: ")
            print("1. First Class AC")
            print("2. AC Two tier")
            print("3. AC Three tier")
            print("4. Sleeper Class")
            print("5. General Class")
            o = int(input("Enter your seat class: "))
            
            if o == 1:
                print(f" Your ticket with train number {j} and booking ID {l} from {m} to {n} in First Class AC has been canceled successfully!!")
                print("Refund will be generated shortly")
                print("Thank You!")
            elif o == 2:
                print(f" Your ticket with train number {j} and booking ID {l} from {m} to {n} in AC Two tier has been canceled successfully!!")
                print("Refund will be generated shortly")
                print("Thank You!")
            elif o == 3:
                print(f" Your ticket with train number {j} and booking ID {l} from {m} to {n} in AC Three tier has been canceled successfully!!")
                print("Refund will be generated shortly")
                print("Thank You!")
            elif o == 4:
                print(f" Your ticket with train number {j} and booking ID {l} from {m} to {n} in Sleeper Class has been canceled successfully!!")
                print("Refund will be generated shortly")
                print("Thank You!")
            elif o == 5:
                print(f" Your ticket with train number {j} and booking ID {l} from {m} to {n} in General Class has been canceled successfully!!")
                print("Refund will be generated shortly")
                print("Thank You!")