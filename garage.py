
class Garage:
    def __init__(self):
        self.tickets = [1,2,3,4,5,6,7,8,9,10]
        self.parkingSpaces = [1,2,3,4,5,6,7,8,9,10]
        self.currentTickets = {}

    def takeTicket(self):
        if self.tickets:
            print(f'Your have ticket number {self.tickets[0]}')
            self.currentTickets[self.tickets[0]] = ''
            del(self.tickets[0])
            del(self.parkingSpaces[0])
        else:
            print('There are no more tickets available.')

    def payForParking(self):
        if self.currentTickets:
            
            while True:
                ticket = input("Please enter the number of your ticket: ")
                if int(ticket) in self.currentTickets:
                    break
                else:
                    print('That was not one of the currently used tickets, please try again.')

            payment = input('Please enter your payment for your ticket: ')

            if payment != '':
                print("Your ticket has been paid. You now have 15 minutes to leave the structure.")
                self.currentTickets[int(ticket)] = 'paid'
            
            else:
                print("You have not paid, please try again when you have payment ready.")
        
        else:
            print('There are no tickets in use.')

    def leaveGarage(self):
        if self.currentTickets:
            ticket = int(input('What is your ticket number'))
            if self.currentTickets[ticket] == 'paid':
                self.tickets.append(ticket)
                self.parkingSpaces.append(ticket)
                del(self.currentTickets[ticket])

                print('Your ticket has been payed for! Have a nice day')
            else:
                print('Your Ticket has not been paid. Please pay your ticket')
        else:
            print('You may leave')

    def run(self):
        while True:
            print("To take a ticket, enter 'take' \nTo pay for your ticket, enter 'pay' \nTo leave the garage, enter 'leave' \nTo exit the program, enter 'exit'")
            choice = input('What would you like to do? ')
            if choice.lower().strip() == 'take':
                print("\033c")
                self.takeTicket()
                
            elif choice.lower().strip() == 'pay':
                print("\033c")
                self.payForParking()
                
            elif choice.lower().strip() == 'leave':
                print("\033c")
                self.leaveGarage()
                
            elif choice.lower().strip() == 'exit':
                print("\033c")
                break
            else:
                print("\033c")
                print('Your input was not one of the valid options, please try again.')

g = Garage()
g.run()