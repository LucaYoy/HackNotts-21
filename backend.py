# A single account containing both the Admin and the User

class Account:

    monthlyBudget = 0.1 # total budget per month
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
        return int(100 * self.rentSoFar / self.rentBudget)

    def getFoodPercent(self):
        return int(100 * self.foodSoFar / self.foodBudget)

    def getBillsPercent(self):
        return int(100 * self.billsSoFar / self.billsBudget)

    def getTransportPercent(self):
        return int(100 * self.transportSoFar / self.transportBudget)

    def getMiscPercent(self):
        return int(100 * self.miscSoFar / self.miscBudget)

    def getMonthlySoFar(self):
        return self.monthlyBudget - self.rentSoFar - self.foodSoFar - self.billsSoFar - self.transportSoFar - self.miscSoFar

    def resetEachBudget(self):
        self.rentBudget = 0.2 * self.monthlyBudget
        self.foodBudget = 0.2 * self.monthlyBudget
        self.billsBudget = 0.2 * self.monthlyBudget
        self.transportBudget = 0.2 * self.monthlyBudget
        self.miscBudget = 0.2 * self.monthlyBudget
    