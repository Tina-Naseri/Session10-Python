class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def show(self):
        print(f"{self.year}/{self.month}/{self.day}")

    def add(self, other):
        new_day = self.day + other.day
        new_month = self.month + other.month
        new_year = self.year + other.year
        if new_day > 30:
            new_month += 1
            new_day -= 30
        if new_month > 12:
            new_year += 1
            new_month -= 12
        return Date(new_day, new_month, new_year)

    def sub(self, other):
        new_day = self.day - other.day
        new_month = self.month - other.month
        new_year = self.year - other.year
        if new_day < 0:
            new_month -= 1
            new_day += 30
        if new_month < 1:
            new_year -= 1
            new_month += 12
        return Date(new_day, new_month, new_year)

    def is_valid_date(self):
        if self.day < 1 or self.day > 30:
            return False
        if self.month < 1 or self.month > 12:
            return False
        if self.year < 1 or self.year > 9999:
            return False
        return True


while True:
    user_choice = input("Enter 's' to start the program or 'e' to exit: ")
    if user_choice == "s":
        operation_choice = int(input(
            "Enter the number of the operation you want to perform:\n1. Add\n2. Sub\n3. Is valid date\n"))
        if operation_choice == 1:
            year1 = int(input("Enter the year of the first date: "))
            month1 = int(input("Enter the month of the first date: "))
            day1 = int(input("Enter the day of the first date: "))
            date1 = Date(day1, month1, year1)
            year2 = int(input("Enter the year of the second date: "))
            month2 = int(input("Enter the month of the second date: "))
            day2 = int(input("Enter the day of the second date: "))
            date2 = Date(day2, month2, year2)
            result = date1.add(date2)
            print("The result is:")
            result.show()
        elif operation_choice == 2:
            year1 = int(input("Enter the year of the first date: "))
            month1 = int(input("Enter the month of the first date: "))
            day1 = int(input("Enter the day of the first date: "))
            date1 = Date(day1, month1, year1)
            year2 = int(input("Enter the year of the second date: "))
            month2 = int(input("Enter the month of the second date: "))
            day2 = int(input("Enter the day of the second date: "))
            date2 = Date(day2, month2, year2)
            result = date1.sub(date2)
            print("The result is:")
            result.show()
        elif operation_choice == 3:
            year = int(input("Enter the year: "))
            month = int(input("Enter the month: "))
            day = int(input("Enter the day: "))
            date = Date(day, month, year)
            if date.is_valid_date():
                print("The date is valid.")
            else:
                print("The date is not valid.")
        else:
            print("Invalid choice. Please try again.")
    elif user_choice == "e":
        break
    else:
        print("Invalid choice. Please try again.")
