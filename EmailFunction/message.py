class Message:
    # We use email_body to distinguish it from the body of the http packet, which will contain the message.
    def __init__(self, subject, email_body, email):
        self.subject = subject
        self.email_body = email_body
        self.email = email


    def __str__(self):
        return f"Message{{subject='{self.subject}', body='{self.email_body}', email='{self.email}'}}"
