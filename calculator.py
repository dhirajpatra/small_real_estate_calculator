
class Calculator():
    tot = 0.0
    # for bonus calculation
    buy = 0
    rent = 0

    # calculate addition
    def add(self, c):
        price = self.switch(c)
        self.tot += price
        self.rules()

    def rules(self):
        if self.buy > 5:
            self.tot += 10
            self.buy -= 6
        elif self.rent > 8:
            self.tot += (self.tot * 10 / 100)
            self.rent -= 9

    # switch case for lead codes
    def switch(self, lead_code):
        switcher = {
            'B': 10,
            'R': 5,
            'ST': 2.5
        }
        code = switcher.get(lead_code.upper(), "invalid lead code")
        if lead_code == 'b':
            self.buy += 1
        elif lead_code == 'r':
            self.rent += 1

        return code

    # return total
    def total(self):
        return self.tot


calculator = Calculator()
codes = ['b', 'r', 'st']

while True:
    lead_code = input(
        "Enter lead code [b/r/st] or any other character to break the loop: ")
    if any(lead_code in code for code in codes):
        calculator.add(lead_code)
    else:
        break

total = calculator.total()

print(f"£{total}")
