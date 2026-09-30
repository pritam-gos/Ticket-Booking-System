def book_ticket():
    p = input("Enter your name: ")
    q = int(input("Enter your age: "))
    r = input("Enter your gender: ")
    b = input("Enter your departure station: ")
    c = input("Enter your destination station: ")
    x = int(input("Enter 5 digit train number: "))
    
    s = {'name': p,
         'age': q,
         'gender': r}
         
    if x < 10000 or x > 100000:
        print("Number Invalid")
    else:
        print("1. First Class AC")
        print("2. AC Two tier")
        print("3. AC Three tier")
        print("4. Sleeper Class")
        print("5. General Class")
        e = input("Enter preferred class: ")
        
        if e == "1":
            print(s)
            print(f" Your ticket booking with train number {x} from {b} to {c} in First Class AC has been confirmed!")
        elif e == "2":
            print(s)
            print(f" Your ticket booking with train number {x} from {b} to {c} in AC Two Tier has been confirmed!")
        elif e == "3":
            print(s)
            print(f" Your ticket booking with train number {x} from {b} to {c} in AC Three Tier has been confirmed!")
        elif e == "4":
            print(s)
            print(f" Your ticket booking with train number {x} from {b} to {c} in Sleeper Class has been confirmed!")
        elif e == "5":
            print(s)
            print(f" Your ticket booking with train number {x} from {b} to {c} in General Class has been confirmed!")
        else:
            print("Choice Invalid!")