from datetime import datetime

class Company:
    
    def can_book_days(self, days, employee_object):
        '''Books days off for a given employee, depending on days of leave 
        remaining.'''
        
        new_leave_total = employee_object.leave_remaining - days 

        if new_leave_total >= 0:
            employee_object.leave_remaining = new_leave_total
            return True
        
        return False

class Employee:
    
    def __init__(self, first_name, last_name, d_o_b, email, start_date, leave):
        
        self.first_name = first_name
        self.last_name = last_name
        self.d_o_b = datetime.strptime(d_o_b, '%d-%m-%y').date()
        self.email = email
        self.start_date = datetime.strptime(start_date, '%d-%m-%y').date()
        self.leave_remaining = leave
        
    def request_leave(self, company_object, days):
        '''Requests leave, calling company.can_book_days.'''
        
        if company_object.can_book_days(days, self):
            return f"You have successfully booked {days} days off. You now " \
                   f"have {self.leave_remaining} days of leave remaining."
        else:
            return f"!!Request denied!!\nYou can only book a maximum of " \
                   f"{self.leave_remaining} days leave."
        

if __name__ == "__main__":
    
    new_employee = Employee("Todd", "Edge", "12-03-85", "tedge7888@company.com", "04-05-24", 21)
    new_company = Company()
    print(new_employee.request_leave(new_company, 21))
    

