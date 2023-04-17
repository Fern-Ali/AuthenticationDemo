
from flask import Flask, request, jsonify, render_template, json, flash, session, redirect
from flask_debugtoolbar import DebugToolbarExtension

from flask_bcrypt import Bcrypt

from models import db, connect_db, User, Feedback
from forms import RegisterForm, LoginForm, FeedbackForm
bcrypt = Bcrypt()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///auth'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLAlCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "we-so-secret3242"


debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

user_id = ""

@app.route('/')
def get_home_page():
    #cupcakes = Cupcake.query.all()
    
    if "username" in session:
        username = session['username']
    return render_template('home.html', )

@app.route("/register", methods=["GET", "POST"])
def register():
    '''register user: produce form and handle form submission'''

    form = RegisterForm()

    if "username" in session:
        return redirect(f"/users/{session['username']}")

    if form.validate_on_submit():
        name = form.username.data
        pwd = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data

        user = User.register(name, pwd, first_name, last_name, email)
        db.session.add(user)
        db.session.commit()

        session["user_id"] = user.id
        session["username"] = user.username
        #on successful login, redirect to auth user pages
        flash(f"You have successfully registered!", "success")
        return redirect("/")

    else:
        return render_template("register.html", form=form)


@app.route('/users/<username>')
def show_secret(username):
    if "username" in session:
        id = session["user_id"]
        user = User.query.filter_by(id=id).all()
        feedback = Feedback.query.filter_by(username=username).all()

        username = user[0].username
        return render_template('secret.html', user=user, id=id, username=username, feedback=feedback)
    else:
        flash(f"You must be logged to view!", "error")
        return redirect("/")


@app.route('/logout')
def logout():
    session.pop("user_id")
    if "username" in session:
        session.pop("username")
    flash(f"You have successfully logged out.", "success")   
    return redirect("/")


@app.route('/login', methods=["POST", "GET"])
def login():
    


    form = LoginForm()

    if "username" in session:
        return redirect(f"/users/{session['username']}")

    if form.validate_on_submit():
        username = form.username.data
        pwd = form.password.data
        
        user = User.authenticate(username, pwd)
        if user:
            session["user_id"] = user.id
            id = user.id
            session["username"] = user.username
            userdata = User.query.filter_by(id=id).all()
            username = userdata[0].username
            flash(f"You have successfully logged in, {username}!", "success")   
            return redirect(f"/users/{username}")
        else:
            flash(f"Invalid credentials!", "error")
            return redirect("/login")
            
            
    else:
        return render_template("login.html", form=form)
    
    return render_template("login.html", form=form)


@app.route('/users/<username>/delete', methods=["GET", "POST"])
def delete_user(username):
    

    if "username" in session:
        id = session["user_id"]
        user = User.query.filter_by(id=id).all()
        username = user[0].username
    
    
    specified_user_delete = User.query.filter_by(id=id).delete()


    db.session.commit()
    session.pop("user_id")
    if "username" in session:
        session.pop("username")
    flash(f"You successfully deleted your account, {username}!", "success")


    return redirect('/')
    
    
    
@app.route('/users/<username>/feedback/add', methods=["GET", "POST"])
def add_feedback(username):
    

    if "username" in session:
        id = session["user_id"]
        user = User.query.filter_by(id=id).all()
        username = user[0].username
    
    
    form = FeedbackForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        

        new_feedback = Feedback(title=title, content=content, username=username)
        db.session.add(new_feedback)
        db.session.commit()

        flash(f"Feedback added!", "success")
        return redirect(f'/users/{username}')
    #db.session.commit()
    
    


    return render_template('feedback.html', form=form, username=username)
    
    
    
@app.route('/feedback/<int:id>/update', methods=["GET", "POST"])
def update_feedback(id):
    

    if "username" in session:
        user_id = session["user_id"]
        user = User.query.filter_by(id=user_id).all()
        username = user[0].username
        feedback = Feedback.query.filter_by(id=id).all()
    else:
        flash(f"You must log in to perform that action!", "error")
        return redirect('/')
        
    
    
    form = FeedbackForm(obj=feedback[0])
    if form.validate_on_submit():

        if form.title.data:
            feedback[0].title = form.title.data
        if form.content.data:
            feedback[0].content = form.content.data
        

        
        db.session.add(feedback[0])
        db.session.commit()

        flash(f"You updated your feedback!", "success")
        return redirect(f'/users/{username}')
    #db.session.commit()
    
    


    return render_template('feedback_edit.html', form=form, username=username, feedback=feedback)      

@app.route('/feedback/<int:id>/delete', methods=["GET", "POST"])
def delete_feedback(id):
    

    if "username" in session:
        user_id = session["user_id"]
        user = User.query.filter_by(id=user_id).all()
        username = user[0].username
        feedback = Feedback.query.filter_by(id=id).all()
    
    
    specified_feedback_delete = Feedback.query.filter_by(id=id).delete()


    db.session.commit()
    
    flash(f"You successfully deleted your feedback, {username}!", "success")


    return redirect(f'/users/{username}')