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
        userName = request.form.get("username")

        print("[debug] user name inputted: {}".format(userName))

        if userName == ADMIN_USER_NAME:
            return redirect("http://127.0.0.1:5000/admin", code=302)
        elif userName == USER_USER_NAME:
            return redirect("http://127.0.0.1:5000/user", code=302)

        return open("./static/home.html").read()

    # admin page
    @app.route("/admin")
    def returnAdminPage():
        return open("./static/admin.html") \
                .read() \
                .format(var1="admin page")

    # user page
    @app.route("/user")
    def returnUserPage():
        return open("./static/user.html") \
                .read() \
                .format(var1="user page")


    # login page
    @app.route("/login")
    def returnAccountPage():
        pass

    # udpate variables
    @app.route("/update")
    def updateAccountBudget():
        return open("./static/home.html").read()

    app.run()


if __name__ == "__main__":
    main()