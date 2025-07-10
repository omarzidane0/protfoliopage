from extintion import db
class message(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(80))
    msg = db.Column(db.Text(80))
    
    def __init__(self , username , email , msg):
        self.username = username
        self.email = email
        self.msg = msg
        

if __name__ == "__main__":
    ...