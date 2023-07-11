class Message:
    def __init__(self, subject=None, body=None, email=None):
        self.subject = subject
        self.body = body
        self.email = email

    def get_subject(self):
        return self.subject

    def set_subject(self, subject):
        self.subject = subject

    def get_body(self):
        return self.body

    def set_body(self, body):
        self.body = body

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def __str__(self):
        return f"Message{{subject='{self.subject}', body='{self.body}', email='{self.email}'}}"
