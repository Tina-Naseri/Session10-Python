class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def show(self):
        print(f"{self.hour}:{self.minute}:{self.second}")

    def from_seconds(self, seconds):
        self.hour = seconds // 3600
        seconds %= 3600
        self.minute = seconds // 60
        self.second = seconds % 60

    def to_seconds(self):
        return (self.hour * 3600) + (self.minute * 60) + self.second


while True:
    user_choice = input("Enter 's' to start the program or 'e' to exit: ")
    if user_choice == "s":
        operation_choice = int(input(
            "Enter the number of the operation you want to perform:\n1. Convert seconds to time\n2. Convert time to seconds\n"))
        if operation_choice == 1:
            seconds = int(input("Enter the number of seconds: "))
            t = Time(None, None, None)
            t.from_seconds(seconds)
            print("The time is:")
            t.show()
        elif operation_choice == 2:
            hour = int(input("Enter the number of hours: "))
            minute = int(input("Enter the number of minutes: "))
            second = int(input("Enter the number of seconds: "))
            t = Time(hour, minute, second)
            print("The total number of seconds is:")
            print(t.to_seconds())
        else:
            print("Invalid choice. Please try again.")
    elif user_choice == "e":
        break
    else:
        print("Invalid choice. Please try again.")
