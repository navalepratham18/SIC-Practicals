class employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary= salary

    def __str__(self):
        return f"Name : {self.name}\nID : {self.id}\nSalary : ₹{self.salary}"
