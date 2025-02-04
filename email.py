from tabulate import tabulate

# --- Email Class --- #
class Email:
    """A class to represent an email."""

    def __init__(self, email_address, subject_line, email_content):
        """
        Constructor to initialize email attributes:
        - email_address: Sender's email address.
        - subject_line: Subject of the email.
        - email_content: Content/body of the email.
        - has_been_read: Boolean to track if the email has been read (default: False).
        """
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        """Marks the email as read."""
        self.has_been_read = True

    def __repr__(self):
        """String representation of the email."""
        return f"Email(from={self.email_address}, subject={self.subject_line}, read={self.has_been_read})"


# --- Functions --- #
def populate_inbox():
    """Populates the inbox with sample emails."""
    sample_emails = [
        ("noreply@cogrammar.com", "Welcome to Hyperion Dev", "Thank you for joining us"),
        ("noreply@cogrammar.com", "Great work on the bootcamp!", "Keep up the fantastic progress"),
        ("noreply@cogrammar.com", "Your excellent marks!", "You scored excellently on your last project!"),
    ]
    for email_address, subject_line, email_content in sample_emails:
        inbox.append(Email(email_address, subject_line, email_content))


def list_emails():
    """Lists all emails with their index, subject line, and read status."""
    if not inbox:
        print("\nInbox is empty.")
        return

    table = [
        [i, email.subject_line, "Read" if email.has_been_read else "Unread"]
        for i, email in enumerate(inbox)
    ]
    print("\nInbox:")
    print(tabulate(table, headers=["Index", "Subject Line", "Status"], tablefmt="grid"))


def read_email():
    """Allows the user to read a selected email."""
    if not inbox:
        print("\nInbox is empty.")
        return

    try:
        list_emails()
        index = int(input("\nEnter the index of the email you want to read: "))
        if 0 <= index < len(inbox):
            email = inbox[index]
            email.mark_as_read()
            print("\nEmail Details:")
            print(f"From: {email.email_address}")
            print(f"Subject: {email.subject_line}")
            print(f"\nContent: {email.email_content}")
        else:
            raise ValueError("Invalid index. Please enter a valid email index.")
    except ValueError as e:
        print(f"\nError: {e}")


def view_unread_emails():
    """Displays unread emails with their index and subject line."""
    unread_emails = [email for email in inbox if not email.has_been_read]
    if unread_emails:
        table = [
            [i, email.subject_line]
            for i, email in enumerate(inbox)
            if not email.has_been_read
        ]
        print("\nUnread Emails:")
        print(tabulate(table, headers=["Index", "Subject Line"], tablefmt="grid"))
    else:
        print("\nNo unread emails.")


def delete_email():
    """Allows the user to delete a selected email."""
    if not inbox:
        print("\nInbox is empty.")
        return

    try:
        list_emails()
        index = int(input("\nEnter the index of the email you want to delete: "))
        if 0 <= index < len(inbox):
            deleted_email = inbox.pop(index)
            print(f"\nDeleted email: {deleted_email.subject_line}")
        else:
            raise ValueError("Invalid index. Please enter a valid email index.")
    except ValueError as e:
        print(f"\nError: {e}")


def email_statistics():
    """Displays statistics about the inbox."""
    total_emails = len(inbox)
    unread_emails = sum(1 for email in inbox if not email.has_been_read)
    read_emails = total_emails - unread_emails

    print("\nEmail Statistics:")
    print(f"Total Emails: {total_emails}")
    print(f"Unread Emails: {unread_emails}")
    print(f"Read Emails: {read_emails}")


# --- Lists --- #
inbox = []  # Stores the email objects.

# --- Email Program --- #
populate_inbox()  # Populate inbox with sample emails.

# Display menu options.
while True:
    print(
        """
Would you like to:
    1. Read an email
    2. View unread emails
    3. Delete an email
    4. View email statistics
    5. Quit application
"""
    )

    try:
        user_choice = int(input("\nEnter your choice: "))

        if user_choice == 1:
            read_email()
        elif user_choice == 2:
            view_unread_emails()
        elif user_choice == 3:
            delete_email()
        elif user_choice == 4:
            email_statistics()
        elif user_choice == 5:
            print("\nExiting Program. Goodbye!\n")
            break
        else:
            raise ValueError("Invalid choice. Please enter a number between 1 and 5.")

    except ValueError as e:
        print(f"\nError: {e}")
