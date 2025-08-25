from typing import Optional, List

class Employee:
    def __init__(self, name: str, position:str)->None:
        self.name = name
        self.position = position
        self.reports:List['Employee'] = []
    
    def add_new_employee(self, new_employee:'Employee')->None:
        self.reports.append(new_employee)

    
class Employee_Organization:
    def __init__(self, root: Employee)->None:
        self.employee_tree = root

    def add_member(self, manager_name: str, emp_name: str, emp_pos: str)->None:
        manager = self.find_member(self.employee_tree, manager_name)
        if not manager:
            print(f"{manager_name} is not in this hierarchy")
        else:
            manager.add_new_employee(Employee(emp_name, emp_pos))
            print(f"{emp_name} added under {manager_name}.")
    
    def find_member(self, node: Employee, name: str)-> Optional['Employee']:
        if node.name == name:
            return node
        for emp in node.reports:
            found = self.find_member(emp, name)
            if found:
                return emp
        return None
    
    def find_CEO(self)->None:
        CEO = self.find_find_CEO(self.employee_tree)
        print(f"The CEO for the company is {CEO.name}")

    def find_find_CEO(self, node:Employee)-> Optional[Employee]:
        if node.position == "CEO":
            return node
        for emp in node.reports:
            found = self.find_find_CEO(emp)
            if found:
                return found
    
    def total_employees(self)->None:
        total = self.find_total_employees(self.employee_tree)
        print(f"total number of employees: {total}")
    
    def find_total_employees(self, node: Employee)->int:
        count = 1
        for emp in node.reports:
            count += self.find_total_employees(emp)
        return count
    
    def Longest_Reporting_Chain(self)->None:
        chain = self.find_Longest_Reporting_Chain(self.employee_tree)
        print(f"maximum number of levels in between is {chain}.")

    def find_Longest_Reporting_Chain(self, node: Employee)->int:
        for emp in node.reports:
            return 1
        return 1+ max(self.find_Longest_Reporting_Chain(emp) for emp in emp.reports)
        
    def print_organization_chart(self)->None:
        self.find_print_organization_chart(self.employee_tree,0)

    def find_print_organization_chart(self, node:Employee, level)-> None:
        print("    "*level + f"{node.name}  ({node.position})")
        for emp in node.reports:
            self.find_print_organization_chart(emp, level+1)