# Input data: List of dictionaries
employee_list = [
   {"id": 12345, "name": "John", "department": "Kitchen"},
   {"id": 12456, "name": "Paul", "department": "House Floor"},
   {"id": 12478, "name": "Sarah", "department": "Management"},
   {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
   {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
   {"id": 12419, "name": "Gill", "department": "Cashier"}
]


def mod(employee_list):
   temp = employee_list['name'] + "_" + employee_list["department"]
   return temp

def to_mod_list(employee_list):
   """ Modifies the employee list of dictionaries into list of employee-department strings"""
   """
   Args:
      employee_list: list of employee objects

   Returns:
      list - A list of strings consisting of name + department.
   """

   map_employees = map(mod, employee_list)
   map_list = list(map_employees)
   return map_list

   raise NotImplementedError()

def generate_usernames(mod_list):
   """ Generates a list of usernames """
   """ 
   Args:
      mod_list: list of employee-department strings

   Returns:
      list - A list of usernames consisting of name + department delimited by underscores.
   """

   usernames_list = [user.replace(" ","_") for user in mod_list]

   return usernames_list

   raise NotImplementedError()

def map_id_to_initial(employee_list):
   """ Maps employee id to first initial"""
   """
   Args:
      employee_list: list of employee objects

   Returns:
      dict - A dictionary mapping an employee's id (value) to their first initial (key).
   """
   dict_usernames = {user["name"][0]:user["id"] for user in employee_list}
   
   return dict_usernames

   raise NotImplementedError()

def main():
   mod_emp_list = to_mod_list(employee_list)
   print("Modified employee list: " + str(mod_emp_list) + "\n")

   print(f"List of usernames: {generate_usernames(mod_emp_list)}\n")

   print(f"Initials and ids: {map_id_to_initial(employee_list)}")

if __name__ == "__main__":
   main()