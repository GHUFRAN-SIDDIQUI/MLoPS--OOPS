#initiate a class
class Chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu (slef):
        user_input = input("""Welcome to the Chatbook!! How would you like to proceed?
                           1. Press 1 to Sign Up
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press 5 to exit""")

        if user_input == '1':
            pass
        elif user_input == '2':
            pass
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass        
        else:
            exit()


obj = Chatbook()