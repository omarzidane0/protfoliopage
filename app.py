from flask import Flask , render_template , request , redirect , Response , url_for
from flask_wtf import  CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from model import message
from extintion import db , csrf
app = Flask(__name__)
app.config["SECRET_KEY"] = "TESTING"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

db.init_app(app=app)
csrf.init_app(app=app)
@app.route("/" , methods=['GET' , 'POST'])
def home():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        msg = request.form.get("msg")
        if username == "" or email == "" or msg == "":
            return render_template("index.html" , alert="Allert : Please Fill All Fields")
        print(username +"\n" + email +"\n"+msg+"\n")
        msg = message(username , email , msg)
        db.session.add(msg)
        db.session.commit()

        return redirect("/")       
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)