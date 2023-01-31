from flask import render_template, url_for, request, redirect, flash
from blog import app, db
from blog.models import User, Post, Comment
from blog.forms import RegistrationForm, LoginForm, AddCommentForm
from flask_login import login_user, logout_user, current_user

# Top navigation bar

@app.route("/")
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')

@app.route("/login",methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user is not None and user.verify_password(form.password.data):
      login_user(user)
      flash('You\'ve successfully logged in,'+' '+ current_user.username +'!')
      return redirect(url_for('home'))
    flash('Invalid username or password.')
  return render_template('login.html',title='Login', form=form)

@app.route("/logout")
def logout():
  logout_user()
  flash('You\'re now logged out!')
  return redirect(url_for('home'))

# Individual posts
@app.route("/post/<int:post_id>",methods=['GET','POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    form = AddCommentForm()
    if (request.method == "POST"):
       if form.validate_on_submit():
            comment = Comment(
                content=form.comment.data, post_id=post.id, author_id=current_user.id)
            comment.author_name = current_user.username
            db.session.add(comment)
            db.session.commit()
            flash("Your comment has successfully been posted!")
            return redirect(f"/post/{post.id}")
    return render_template('post.html', post=post, form=form, comments=post.comments)

# Registration
@app.route("/register",methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(username=form.username.data, password=form.password.data)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('registered', user=form.username.data))
  return render_template('register.html', title='Register', form=form)

@app.route("/registered")
def registered():
  return render_template('registered.html', login_user=request.args['user'])