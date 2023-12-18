from flask import Flask

application = Flask(__name__)

@application.route("/")
def index():
    return "Hello, this is MAIN page"

@application.route("/help")
def helppage():
    return "This is HELP page!!!"

@application.route("/user")
def usermain_page():
    return "User's main page"

@application.route("/user/<username>")
def showuser_page(username):
    return "Hello " + username.upper()

@application.route("/path/<path:subpath>")
def subpath_page(subpath):
    return "Subpath is " + subpath

@application.route("/kvadrat/<int:x>")
def calc_kvadrat(x):
    return "Kvadrat ot: " + str(x) + " = " + str(x*x)

@application.route("/htmlpage")
def show_html_page():
    myfile = open("mypage.html", mode='r')
    page = myfile.read()
    myfile.close()
    return page

#------------MAIN--------------
if __name__ == "__main__":
    application.debug = True
    application.env = "working hard"
    application.run()
# ------------EOF--------------