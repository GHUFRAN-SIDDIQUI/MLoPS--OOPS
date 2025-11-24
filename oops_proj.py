#initiate a class
class Chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu (self):
        user_input = input("""Welcome to the Chatbook!! How would you like to proceed?
                           1. Press 1 to Sign Up
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press 5 to exit""")

        if user_input == '1':
            self.sign_up()
        elif user_input == '2':
            self.sigin()
        elif user_input == '3':
            self.write_post()
        elif user_input == '4':
            self.message_friend()    
        else:
            exit()





    def sign_up(self):
        email = input ("enter your email here-->")
        pwd = input ("setup your password-->")
        self.username = email
        self.password = pwd
        print ("you have successfully signed up!!")
        print( "\n")
        self.menu()

    def sigin(self):
        if self.username == '' and self.password == '':
            print("You need to sign up first!!")
        else:
            uname = input("Enter your email here --> ")
            pwd = input("Enter your password here --> ")
        
            if uname == self.username and pwd == self.password:
                print("You have successfully signed in!!")
                self.loggedin = True
            else:
                print("Invalid credentials, please try again")
                print("\n")
            self.menu()

    def write_post(self):
        if self.loggedin == True:
            post = input("What's on your mind?")
            print("Your post has been published")
        else:
            print("You need to sign in first to write a post")
            self.menu()

    def message_friend(self):
        if loggedin == True:
            friend = input("Enter your friend's name")
            msg = input("Enter your message")
            print("Your message has been sent")
        else:
            print("You need to sign in first to write a post")
            self.menu()
#obj = Chatbook()
