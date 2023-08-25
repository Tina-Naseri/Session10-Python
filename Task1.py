class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def show(self):
        print(self.numerator, "/", self.denominator)

    def add(self, f):
        result = Fraction(None, None)
        result.numerator = (self.numerator * f.denominator) + \
            (f.numerator * self.denominator)
        result.denominator = self.denominator * f.denominator
        return result

    def sub(self, f):
        result = Fraction(None, None)
        result.numerator = (self.numerator * f.denominator) - \
            (f.numerator * self.denominator)
        result.denominator = self.denominator * f.denominator
        return result

    def mul(self, f):
        result = Fraction(None, None)
        result.numerator = self.numerator * f.numerator
        result.denominator = self.denominator * f.denominator
        return result

    def div(self, f):
        result = Fraction(None, None)
        result.numerator = self.numerator * f.denominator
        result.denominator = self.denominator * f.numerator
        return result


def separator():
    print("----------------------------")


while True:
    user_choice = input("Enter 's' to start the program or 'e' to exit: ")
    if user_choice == "s":
        f1 = Fraction(int(input("Please enter the numerator of fraction1: ")),
                      int(input("Please enter the denominator of fraction1: ")))
        print(f"---> Your fraction1 is: {f1.numerator}/{f1.denominator}")
        f2 = Fraction(int(input("Please enter the numerator of fraction2: ")),
                      int(input("Please enter the denominator of fraction2: ")))
        print(f"---> Your fraction2 is: {f2.numerator}/{f2.denominator}")
        separator()
        result_add = f1.add(f2)
        print("Addition Result:")
        result_add.show()
        separator()
        result_sub = f1.sub(f2)
        print("Subtraction Result:")
        result_sub.show()
        separator()
        result_mul = f1.mul(f2)
        print("Multiplication Result:")
        result_mul.show()
        separator()
        result_div = f1.div(f2)
        print("Division Result:")
        result_div.show()
        separator()
    elif user_choice == "e":
        break
