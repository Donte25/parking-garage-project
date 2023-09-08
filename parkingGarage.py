class ParkingGarage():

    def __init__(self):
        pass

    def takeTicket(self):
        """This should decrease the amount of tickets available by 1
           This should decrease the amount of parkingSpaces available by 1"""
        pass

    def payForParking(self):
        """Display an input that waits for an amount from the user and store it in a variable.
           If the payment variable is not empty then (meaning the ticket has been paid) ->  display 
           a message to the user that their ticket has been paid and they have 15mins to leave
           This should update the "currentTicket" dictionary key "paid" to True"""
        pass

    def leaveGarage(self):
        """If the ticket has been paid, display a message of "Thank You, have a nice day"
           If the ticket has not been paid, display an input prompt for payment
           Once paid, display message "Thank you, have a nice day!"
           Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
           Update tickets list to increase by 1 (meaning add to the tickets list)"""
        pass



#main
pg = ParkingGarage()

print("PARKING GARAGE".center(50, '-'))