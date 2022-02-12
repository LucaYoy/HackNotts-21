# A single account containing both the Admin and the User

class Account:

    monthlyBudget = 0 # total budget per month
    monthlySoFar = 0

    rentBudget = 0
    rentSoFar = 0

    foodBudget = 0
    foodSoFar = 0

    billsBudget = 0 # gass, electricity, internet, phone, etc.
    billsSoFar = 0

    transportBudget = 0
    transportSoFar = 0

    miscBudget = 0 # subscriptions, etc.
    miscSoFar = 0

    warningThreshold = 0.9

    def __init__(self):
        pass