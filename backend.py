# A single account containing both the Admin and the User

class Account:

    monthlyBudget = 1000 # total budget per month
    monthlySoFar = 0

    rentBudget = 0
    rentSoFar = 0

    foodBudget = 0
    foodSoFar = 0

    billsBudget = 0 # gas, electricity, internet, phone, etc.
    billsSoFar = 0

    transportBudget = 0
    transportSoFar = 0

    miscBudget = 0 # subscriptions, etc.
    miscSoFar = 0

    warningThreshold = 0.9

    def __init__(self):
        pass

    def getRentPercent(self):
        return self.rentSoFar / self.rentBudget * 100

    def getFoodPercent(self):
        return self.foodSoFar / self.foodBudget * 100

    def getBillsPercent(self):
        return self.billsSoFar / self.billsBudget * 100

    def getTransportPercent(self):
        return self.transportSoFar / self.transportBudget * 100

    def getMiscPercent(self):
        return self.miscSoFar / self.miscBudget * 100
    