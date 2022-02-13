from flask import Flask
from flask import request, redirect

from backend import Account

def main():

    ADMIN_USER_NAME = "admin1"
    USER_USER_NAME = "user1"

    app = Flask(__name__)
    account = Account()

    # login page
    @app.route("/", methods=['GET', 'POST'])
    def returnLoginPage():
        username = request.form.get("username")
        password = request.form.get("password")

        # a quick implementation of the login system for the demo
        if username == ADMIN_USER_NAME:
            return redirect("http://127.0.0.1:5000/admin", code=302) # local host for the demo
        elif username == USER_USER_NAME:
            return redirect("http://127.0.0.1:5000/user", code=302)

        return open("./static/home.html").read()

    # admin page
    @app.route("/admin")
    def returnAdminPage():
        return open("./static/admin.html") \
                .read() \
                .format(monthlySoFar=account.getMonthlySoFar())

    # user page
    @app.route("/user")
    def returnUserPage():
        return open("./static/user.html") \
                .read() \
                .format(monthlyBudget=account.monthlyBudget, \
                        monthlySoFar=account.getMonthlySoFar(), \
                        rentPercent=account.getRentPercent(), \
                        foodPercent=account.getFoodPercent(), \
                        billsPercent=account.getBillsPercent(), \
                        transportPercent=account.getTransportPercent(), \
                        miscPercent=account.getMiscPercent())

    # udpate budgets
    @app.route("/update")
    def updateAccountBudget():
        if request.args.get("monthly-budget") != "":
            account.monthlyBudget = float(request.args.get("monthly-budget"))
            account.resetEachBudget()

        if request.args.get("rent") != "":
            account.rentSoFar += float(request.args.get("rent"))
        
        if request.args.get("food") != "":
            account.foodSoFar += float(request.args.get("food"))
        
        if request.args.get("bills") != "":
            account.billsSoFar += float(request.args.get("bills"))
        
        if request.args.get("transport") != "":
            account.transportSoFar += float(request.args.get("transport"))
        
        if request.args.get("misc") != "":
            account.miscSoFar += float(request.args.get("misc"))

        return redirect("http://127.0.0.1:5000/", code=302)

    # take the user back to the login page
    @app.route("/goToLogin", methods=['GET', 'POST'])
    def goToLoginPage():
        return redirect("http://127.0.0.1:5000/", code=302)

    # progress bar test
    @app.route("/test")
    def progressBar():
        return open("./static/progress_bar.html") \
                .read() \
                .format(var2=80)

    app.run()


if __name__ == "__main__":
    main()
