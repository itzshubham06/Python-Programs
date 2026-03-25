import pandas as pd
import openpyxl as ox
df = pd.read_excel("employee.xlsx")

print("Employees in Automotive domain:")
auto_emp = df[df['Department'] == 'Automotive']
print(auto_emp)

emp_id = int(input("Enter Employee ID: "))
emp_details = df[df['Employee ID'] == emp_id]

print("\nEmployee Details:")
print(emp_details)

print("\nList of Developers:")
developers = df[df['Designation'] == 'Developer']
print(developers)