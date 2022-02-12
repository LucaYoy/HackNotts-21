# A single account containing both the Admin and the User

class Account:

    monthlyBudget = 1000 # total budget per month
    monthlySoFar = 0

    rentBudget = 0.2 * monthlyBudget
    rentSoFar = 0

    foodBudget = 0.2 * monthlyBudget
    foodSoFar = 0

    billsBudget = 0.2 * monthlyBudget # gas, electricity, internet, phone, etc.
    billsSoFar = 0

    transportBudget = 0.2 * monthlyBudget
    transportSoFar = 0

    miscBudget = 0.2 * monthlyBudget # subscriptions, etc.
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

    def getMonthlySoFar(self):
        return self.monthlyBudget - self.rentSoFar - self.foodSoFar - self.billsSoFar - self.transportSoFar - self.miscSoFar
    