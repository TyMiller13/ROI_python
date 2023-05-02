import time

class ReturnOnInvestment:

    def __init__(self, monthly_income=0, monthly_expenses=0, monthly_cashflow=0, annual_cashflow=0, investments=0, roi=0):
        self.monthly_income = monthly_income
        self.monthly_expenses = monthly_expenses
        self.monthly_cashflow = monthly_cashflow
        self.annual_cashflow = annual_cashflow
        self.investments = investments
        self.roi = roi

        
# Method for income
    # get income from all sources
    def income(self):
        rental = float(input("What is your total monthly income from rentals? "))
        laundry = float(input("What is your total monthly income from laundry? "))
        storage = float(input("What is your total monthly income from storage? "))
        misc = float(input("Please enter the total monthly income from all other sources: "))
        self.monthly_income = rental + laundry + storage + misc
        print(f"You're total monthly income: ${self.monthly_income:.2f}")
        
    # Method for expenses
    # get expenses from all sources
    def expenses(self):
        tax = float(input("Taxes: "))
        insurance = float(input("Insurance: "))
        electric = float(input("Electric: "))
        water = float(input("Water: "))
        sewer = float(input("Sewer: "))
        garbage = float(input("Garbage: "))
        gas = float(input("Gas: "))
        HOA = float(input("HOA: "))
        lawn_snow = float(input("Lawn and Snow: "))
        vacancy = float(input("Vacancy: "))
        repairs = float(input("Repairs: "))
        cap_ex = float(input("Capital Expenditures: "))
        prop_management = float(input("Property Management: "))
        mortgage = float(input("Mortgage: "))
        
        self.monthly_expenses = tax+insurance+electric+water+sewer+garbage+gas+HOA+lawn_snow+vacancy+repairs+cap_ex+prop_management+mortgage # add all expenses 
        print(f"You're total monthly expense: ${self.monthly_expenses:.2f}")
        
    # Method for cashflow
    # get cash flow from income subtracting the expenses
    def cashflow(self):
        self.monthly_cashflow = self.monthly_income - self.monthly_expenses
        print(f"You're monthly cashflow is ${self.monthly_cashflow:.2f}")
        
    # Method for cash on cash ROI
    # get ROI by dividing your annual cash flow by the total amount invested and return
    def cash_on_cash_roi(self):
        self.annual_cashflow = self.monthly_cashflow * 12
        downpayment = float(input("downpayment: "))
        closing_cost = float(input("closing cost: "))
        rehab = float(input("rehab: "))
        misc = float(input("total of everything else: "))
        self.investments = downpayment + closing_cost + rehab + misc
        self.roi = self.annual_cashflow / self.investments
        self.roi_percent = self.roi * 100
        return self.roi_percent
    
    
    def summary(self):
        print("-"*50)
        print(
f"""
    Your Summary and Results
    ========================
Total Income: ${self.monthly_income:.2f}
Total Expenses: ${self.monthly_expenses:.2f}
Monthly Cash Flow: ${self.monthly_cashflow:.2f}
Annual Cash Flow: ${self.annual_cashflow:.2f}
Total Investment: ${self.investments:.2f}
------------------------------------------------
Return On Investments: {self.roi_percent:.2f}%
"""
        )

def run_roi():
    print("Welcome to your Return On Investment calculator, please enter all information needed, and we'll handle the number crunching!")
    my_roi = ReturnOnInvestment()
    print("="*100)
    print("Let's go over your monthly income.")
    my_roi.income()
    print("Great! lets move onto expenses. Enter the amount to each expense.")
    my_roi.expenses()
    print("Calculating cash flow...")
    time.sleep(2)
    my_roi.cashflow()
    print("Just a few more questions! enter the amount. ")
    my_roi.cash_on_cash_roi()
    print("Loading your results!")
    time.sleep(2)
    my_roi.summary()

run_roi()
