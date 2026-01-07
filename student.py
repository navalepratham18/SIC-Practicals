class student:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display(self):
        print(f"name : {self.name}\nemail: {self.email}")
