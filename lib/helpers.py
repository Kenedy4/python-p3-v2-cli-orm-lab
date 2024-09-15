from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.query.all()
    for employee in employees:
         print(f"<Employee {employee.id}: {employee.name}, {employee.job_title}, Department ID: {employee.department_id}>")


def find_employee_by_name():
   name = input("Enter the employee's name: ")
   employee = Employee.query.filter_by(name=name).first()
   if employee:
        print(f"<Employee {employee.id}: {employee.name}, {employee.job_title}, Department ID: {employee.department_id}>")
   else:
        print(f"Employee {name} not found")


def find_employee_by_id():
    try:
        employee_id = int(input("Enter the employee's id: "))
        employee = Employee.query.get(employee_id)
        if employee:
            print(f"<Employee {employee.id}: {employee.name}, {employee.job_title}, Department ID: {employee.department_id}>")
        else:
            print(f"Employee {employee_id} not found")
    except ValueError:
        print("Invalid ID entered.")
    


# def create_employee():
    # try:
        # name = input("Enter the employee's name: ")
        # job_title = input("Enter the employee's job title: ")
        # department_id = int(input("Enter the employee's department id: "))
        # new_employee = Employee(name=name, job_title=job_title, department_id=department_id)
        # new_employee.save()
        # print(f"Success: <Employee {new_employee.id}: {new_employee.name}, {new_employee.job_title}, Department ID: {new_employee.department_id}>")
    # except Exception as e:
# print(f"Error creating employee: {str(e)}")
def create_employee():
    try:
        name = input("Enter the employee's name: ")
        job_title = input("Enter the employee's job title: ")
        department_id = int(input("Enter the employee's department id: "))
        new_employee = Employee(name=name, job_title=job_title, department_id=department_id)
        new_employee.save()
        print(f"Success: <Employee {new_employee.id}: {new_employee.name}, {new_employee.job_title}, Department ID: {new_employee.department_id}>")
    except Exception as e:
        print(f"Error creating employee: {str(e)}")


def update_employee():
    try:
        employee_id = int(input("Enter the employee's id: "))
        employee = Employee.query.get(employee_id)
        if not employee:
            print(f"Employee {employee_id} not found")
            return
        name = input("Enter the employees's new name: ")
        job_title = input("Enter the employee's new job title: ")
        department_id = int(input("Enter the employees's new department id: "))
        
        employee.name = name
        employee.job_title = job_title
        employee.department_id = department_id
        employee.save()
        print(f"Success: <Employee {employee.id}: {employee.name}, {employee.job_title}, Department ID: {employee.department_id}>")
    except Exception as e:
        print(f"Error updating employee: {str(e)}")

def delete_employee():
    try:
        employee_id = int(input("Enter the employee's id: "))
        employee = Employee.query.get(employee_id)
        if employee:
            employee.delete()
            print(f"Employee {employee_id} deleted")
        else:
            print(f"Employee {employee_id} not found")
    except Exception as e:
        print(f"Error deleting employee: {str(e)}")


def list_department_employees():
    try:
        department_id = int(input("Enter the department's id: "))
        department = Department.query.get(department_id)
        if department:
            employees = department.employees()  # Assuming a relationship is defined
            for employee in employees:
                print(f"<Employee {employee.id}: {employee.name}, {employee.job_title}, Department ID: {employee.department_id}>")
        else:
            print(f"Department {department_id} not found")
    except Exception as e:
        print(f"Error: {str(e)}")