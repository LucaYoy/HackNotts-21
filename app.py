from flask import Flask

from backend import Account

def main():
    app = Flask(__name__)
    account = Account()

    @app.route("/")
    def returnHTML():
        return open("./frontend.html") \
                .read() \
                .format(var1=11313)

    app.run()


if __name__ == "__main__":
    main()