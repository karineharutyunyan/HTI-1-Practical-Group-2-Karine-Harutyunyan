import datetime


class Employee:
    def __init__(self, first_name, last_name, phone_number, work_email, trial_passed, join_date, leave_date, salary,
                 gender):
        self._first_name = first_name
        self._last_name = last_name
        self._phone_number = phone_number
        self._work_email = work_email
        self._trial_passed = trial_passed
        self._join_date = join_date
        self._leave_date = leave_date
        self._salary = salary
        self._gender = gender

    def get_first_name(self):
        return 'First Name: ' + self._first_name

    def get_last_name(self):
        return 'Last Name: ' + self._last_name

    def get_full_name(self):
        return 'Full Name: ' + f'{self._first_name} {self._last_name}'

    def get_phone_number(self):
        if len(self._phone_number) != 0:
            return 'Phone Number: ' + self._phone_number
        else:
            return 'Phone Number: ' + ''

    def get_work_email(self):
        if len(self._work_email) != 0:
            return 'Work Email: ' + self._work_email
        else:
            return 'Work Email: ' + ''

    def get_trial_passed(self):
        if self._trial_passed == 'Yes':
            return 'Trial Passed: ' + 'Yes'
        else:
            return 'Trial Passed: ' + 'No'

    def get_join_date(self):
        j_date = self._join_date
        j_date = datetime.datetime.strptime(j_date, '%d.%m.%Y')
        start_date = datetime.date.strftime(j_date, '%d.%m.%Y')
        return 'Join Date: ' + start_date

    def get_leave_date(self):
        l_date = self._leave_date
        if len(l_date) != 0:
            l_date = datetime.datetime.strptime(l_date, '%d.%m.%Y')
            end_date = datetime.date.strftime(l_date, '%d.%m.%Y')
            return 'Leave Date: ' + end_date
        else:
            return 'Leave Date: ' + ''

    def get_salary(self):
        return 'Salary: ' + self._salary

    def get_gender(self):
        return 'Gender: ' + self._gender


e1 = Employee('Davit', 'Tovmasyan', '077 12 34 56', 'davit.tovmasyan@company.com', 'No', '22.02.2018', '', '600$', 'M')
e2 = Employee('Tovmas', 'Davtyan', '', 'tovmas.davtyan@company.com', 'Yes', '11.01.2020', '25.07.2020', '45000֏', 'M')
e1.get_first_name(), e1.get_last_name(), e1.get_full_name(), e1.get_phone_number(), e1.get_work_email(), e1.get_trial_passed(), e1.get_join_date(), e1.get_leave_date(), e1.get_salary(), e1.get_gender()
e2.get_first_name(), e2.get_last_name(), e2.get_full_name(), e2.get_phone_number(), e2.get_work_email(), e2.get_trial_passed(), e2.get_join_date(), e2.get_leave_date(), e2.get_salary(), e2.get_gender()
