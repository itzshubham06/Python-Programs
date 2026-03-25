class Employee:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.salary = 0
        self.address = ""

    def get_data(self):
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.salary = float(input("Enter Salary: "))
        self.address = input("Enter Address: ")

    def display_data(self):
        print("\nEmployee Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)


class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.department = ""

    def get_data(self):
        super().get_data()
        self.department = input("Enter Department: ")

    def display_data(self):
        super().display_data()
        print("Department:", self.department)


# Processing 10 managers
managers = []

for i in range(10):
    print(f"\nEnter details for Manager {i+1}")
    m = Manager()
    m.get_data()
    managers.append(m)

print("\n--- Manager Details ---")
for i, m in enumerate(managers):
    print(f"\nManager {i+1}")
    m.display_data()