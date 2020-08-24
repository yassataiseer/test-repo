import smtplib
class deliver:
    def deliver_process(id):
        print("ID",id)
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("yassataiseer@gmail.com", "FILE.exe123")
        server.sendmail(
            "yassataiseer@gmail.com",id,"thank you for signing up for Codnect we will send you daily emails of players you may want to play with")
        print("email sent")






    if password != repeat or existing_user is not None:
        return 'invalid credentials the email used may have already been in use or your repeat and original passswords are different '
    elif password==repeat:
        db.create_all()
        db.session.add(user)
        db.session.commit()
        return render_template("home.html") 
