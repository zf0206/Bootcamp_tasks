# Create a class named Email, with four variables
class Email(object):
    def __init__(self, title, contents, from_address = 'sender@gmail.com', has_been_read = False,  is_spam = False):
        self.title = title
        self.has_been_read = has_been_read
        self.contents = contents
        self.is_spam = is_spam
        self.from_address = from_address
    # Creat a function to change has_been_read to true
    def mark_as_read(self):
        self.has_been_read = True
    # Creat a function to change is_spam to true
    def mark_as_spam(self):
        self.is_spam = True

# Define add_email, takes contents and email address from the received email
# Make a new Email object
def add_email(title, contents, email_address):
    email = Email(title, contents, email_address)
    inbox.append(email)

# Define get_count to return the number of messages in the store
def get_count():
    return len(inbox)

# Define get_email to return contents of an email from the list
def get_email(index):
    email = inbox[index]
    contents = email.contents
    email.has_been_read = True
    return contents

# Define get_unread_emails to return list of all the emails that haven't been read
def get_unread_emails():
    unread_emails = []
    for i in inbox:
        if i.has_been_read == False:
            unread_emails.append(i)
    return unread_emails

# Define get_spam_emails to return a list of all the emails that have been marked as spam
def get_spam_emails():
    spam_emails = []
    for i in inbox:
        if i.is_spam == True:
            spam_emails.append(i)
    return spam_emails

# Define delet_email function to delet an email in the inbox
def delete_email(index):
    del inbox[index]

# Creat inbox list
# Save some initial value in the index
inbox = []
test_email = Email('title 1', 'content 1', '1@mail.com')
inbox.append(test_email)

user_choice = ''
# Use a while loop to allow user to select their choices
while user_choice != "quit":
    # Ask user to input which function they want to select
    user_choice = input("What would you like to do - read/mark spam/send/number of spam/list unread/delete/quit?\n")
    # If user select 'read', call get_count and get_email functions
    if user_choice == "read":
        print(f"Total number of emails is {get_count()}.")
        index = int(input("Which email would you like to read? Please type a number.\n"))
        if index > len(inbox):
            print("Sorry, we do not have this email.")
        else:
            print(get_email(index-1))
    # If user select 'mark spam', call .mark_as_spam method
    elif user_choice == "mark spam":
        index = int(input("Which email would you like to mark as spam? Please type a number.\n"))
        if index > len(inbox):
            print("Sorry, we do not have this email.")
        else:
            inbox[index-1].mark_as_spam
            print(f"Marked email {index} as spam.")
    # If user select 'send', call add_email function
    elif user_choice == "send":
        title = input("Please enter title of the email:\n")
        contents = input("Please enter contents of the email:\n")
        email_address = input("Please enter email address:\n")             
        add_email(title, contents, email_address)
        print("Email has been sent!")
    # If user select 'number fo spam', call get_spam_emails function
    elif user_choice == "number of spam":
        spam_emails = get_spam_emails()
        print(f"You have {len(spam_emails)} spam emails in your inbox.")
    # If user select 'list unread', call get_unread_emails function
    elif user_choice == "list unread":
        unread_emails = get_unread_emails()
        print(f"You have the following unread emails:")
        for email in unread_emails:
            print(f"{email.title}\n")
    # If user select 'delete', call delete_email function
    elif user_choice == "delete":
        index = int(input("Which email would you like to delete? Please type a number.\n"))
        if index > len(inbox):
            print("Sorry, we do not have this email.")
        else:
            delete_email[index-1]
            print("This email has been deleted")
    # if user select'quit', quit the loop
    elif user_choice == "quit":
        print("Goodbye")
        exit()
    else:
        print("Oops - incorrect input")