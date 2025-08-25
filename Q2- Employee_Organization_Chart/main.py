from utils import Employee_Organization, Employee

Emp = Employee("Alice", "CEO")
Emp_tree = Employee_Organization(Emp)
Emp_tree.add_member("Alice", "Bob", "CTO")
Emp_tree.add_member("Bob", "Karen", "Manager")
Emp_tree.add_member("Alice", "Claire", "CFO")
Emp_tree.find_CEO()
Emp_tree.total_employees()
Emp_tree.Longest_Reporting_Chain()
Emp_tree.print_organization_chart()