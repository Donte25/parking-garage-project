import datetime

class ParkingGarage():


    def __init__(self):
        # Donte 
        self.existing_users = {}
        self.tickets = [1,1,1,1,1]
        self.parkingSpaces = [1,1,1,1,1]
        self.currentTicket = {}
        

    def takeTicket(self, name, time):
        """This should decrease the amount of tickets available by 1
           This should decrease the amount of parkingSpaces available by 1"""
        # Donte
        del self.tickets[-1]
        del self.parkingSpaces[-1]
        self.currentTicket['paid'] = False 
        self.existing_users[name] = time
        print("NEW USER".center(50, '-'))
        print(f"NAME: {name}\nTIME: {time}\n")
       

    def payForParking(self):
        """Display an input that waits for an amount from the user and store it in a variable.
           If the payment variable is not empty then (meaning the ticket has been paid) ->  display 
           a message to the user that their ticket has been paid and they have 15mins to leave
           This should update the "currentTicket" dictionary key "paid" to True"""
        # David 
        ticketCost = 50
        while self.currentTicket["paid"] == False:
            payment = input("Enter payment amount ($50): ")
            if payment.isdigit() and int(payment) == ticketCost:
                print("\nTicket PAID. You have 15 min to leave the garage.\nThank you!")
                self.currentTicket["paid"] = True
            else:
                print(f"\nINVALID PAYMENT AMOUNT")


    def leaveGarage(self, name):
        """If the ticket has been paid, display a message of "Thank You, have a nice day"
           If the ticket has not been paid, display an input prompt for payment
           Once paid, display message "Thank you, have a nice day!"
           Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
           Update tickets list to increase by 1 (meaning add to the tickets list)"""
        # Donte
        if self.currentTicket['paid'] == True:
            print('Have a nice day!\n')
            self.tickets.append(1)
            self.parkingSpaces.append(1)
            del self.existing_users[name]
        else:
            self.payForParking()



#main - David 
pg = ParkingGarage()

flag = True

while flag:
    print("PARKING GARAGE".center(50, '-'))
    print(f"AVAILABLE SPOTS: {len(pg.parkingSpaces)}")
    user_type = input("\nEnter 'Q' to Quit\nEnter 'P' to Print Existing Users\nEnter 'N' for New User 'E' for Existing Parking User: ")
    user_type = user_type.upper()
    
    while user_type not in ['Q','P','N','E']:
        print("\nEnter 'Q' to Quit\nEnter 'P' to Print Existing Users\nEnter 'N' for New User 'E' for Existing Parking User")
        user_type = input("Enter choice:  ")
        user_type = user_type.upper()

    if user_type == 'Q':
        print("\nProgram TERMINATED")
        break

    elif user_type == 'P':
        if pg.existing_users:
            i = 1
            print("EXISTING USERS".center(50, '-'))
            for name in pg.existing_users.keys():
                print(f"USER {i}: {name}")
                i += 1
        else:
            print("\n>>> NO EXISTING USERS <<<\n")

    elif user_type == 'N':
        if len(pg.parkingSpaces) > 0:
            user_name = input("Please enter your name: ")
            while user_name.isdigit():
                print("\nERROR: Invalid Input")
                user_name = input("Please enter your name: ")
            user_name = user_name.title()
            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime("%I:%M %p %m/%d/%Y")
            pg.takeTicket(user_name, formatted_time)
        else:
            print("\n>>> NO AVAILABLE PARKING SPACES <<<\n".center(50))
        
    elif user_type == 'E':
        if pg.existing_users:
            user_name = input("Please enter your name: ")
            user_name = user_name.title()
            
            while user_name.isdigit():
                print("\nERROR: Enter a valid name...")
                user_name = input("Please enter your name: ")
            
            if user_name not in pg.existing_users:
                not_found = input("\n>> USER NOT FOUND <<\nEnter 'N' to park, 'Q' to quit, or 'R' to retry: ")
                not_found = not_found.upper()
                while not_found not in ['N','Q','R']:
                    print("ERROR: Invalid Input")
                    not_found = ("Enter 'N' to park, 'Q' to quit, or 'R' to retry: ")
                if not_found == 'N':
                    current_time = datetime.datetime.now()
                    formatted_time = current_time.strftime("%I:%M %p %m/%d/%Y")
                    pg.takeTicket(user_name, formatted_time)
                elif not_found == 'Q':
                    break
                else:
                    continue

            else:
                found = input("\n>> USER FOUND <<\nWould you like to leave? (Y/N): ")
                found = found.upper()
                while found not in ['Y','N']:
                    print("\nERROR: Invalid Input")
                    found = input("Enter Y or N: ")
                if found == 'Y':
                    pg.currentTicket["paid"] = False
                    pg.payForParking()
                    pg.leaveGarage(user_name)
                else:
                    pass
        else:
            print("\n>>> NO EXISTING USERS <<<\n")