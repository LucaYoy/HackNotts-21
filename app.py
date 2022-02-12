from flask import Flask

from backend import Account

def main():
    app = Flask(__name__)
    account = Account()

    # login page
    @app.route("/")
    def returnLoginPage():
        return open("./login_page.html") \
                .read() \
                .format(var1="login page")

    # admin page
    @app.route("/admin")
    def returnAdminPage():
        return open("./admin_page.html") \
                .read() \
                .format(var1="admin page")

    # user page
    @app.route("/user")
    def returnUserPage():
        return open("./user_page.html") \
                .read() \
                .format(var1="user page")

    app.run()


if __name__ == "__main__":
    main()