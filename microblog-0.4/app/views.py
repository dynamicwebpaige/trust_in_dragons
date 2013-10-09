
from flask import render_template, flash, redirect
from app import app
from forms import LoginForm, StartPage, RegistrationForm, AdminForm
from newuser_db import addSingleUser
from phonequery_db import sendSms
from emailquery_db import sendMails

@app.route('/')
def home():
    #return redirect('/start')
    return render_template('intro.html')

@app.route('/success.html')
def success():
	return success('success.html')

@app.route('/admin_success.html')
def admin_success():
	return render_template('admin_success.html')

@app.route('/pyladies')
def pyladies():
    return render_template('start1.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/signup')
def signup():
        return render_template('signup1.html')

@app.route('/admin_test')
def admin_test():
        return render_template('admin_test.html')

@app.route('/admin', methods = ['GET', 'POST'])
def admin():
    form = AdminForm()
    if form.validate_on_submit():
        #flash('Login requested for OpenID="' + form.name + '", remember_me=' + str(form.remember_me.data))
        #flash('Successful')
        #return redirect('/success')
        #addSingleUser(form.name.data,form.email.data,form.phone_number.data)
        info = {'name':form.hyperlink.data, 'amount':form.amount.data, 'description':form.description.data}
        sendMails(name=form.hyperlink.data,amount=form.amount.data,desc=form.description.data)
        sendSms()
        return render_template('admin_success.html', title='Success', info = info)# name=form.name, email=form.email, phone_number=form.phone_number)


    #flash('Please check the entered data')
    return render_template('admin_test.html',
        title = 'Login',
        form = form)

    flash('Please check the entered data')
        #providers = app.config['OPENID_PROVIDERS'])


    return render_template('admin.html')


@app.route('/test2')
def test2():
    return render_template('start2.html')

@app.route('/start', methods = ['POST'])
def start2():
    form = StartPage()
    #if form.validate_on_submit():
        #flash('Login requested for OpenID="' + form.name + '", remember_me=' + str(form.remember_me.data))
        #flash('Successful')
    return redirect('/login')
    #return render_template('start.html', 
    #    title = 'Start')

@app.route('/index')
def index():
    user = { 'nickname': 'Prashant' }
    posts = [
        { 
            'author': { 'nickname': 'John' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickname': 'Susan' }, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template('index.html',
        title = 'Home',
        user = user,
        posts = posts)


@app.route('/test')
def test():
    return render_template('paypal_button.html')

@app.route('/intro')
def intro():
    return render_template('intro.html')

@app.route('/success')
def success():
    flash('Successful')
    return render_template('success.html', 
        title = 'Success')
    
@app.route('/login1')
def login1():
    return render_template('signup1.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #flash('Login requested for OpenID="' + form.name + '", remember_me=' + str(form.remember_me.data))
        #flash('Successful')
        #return redirect('/success')
 	addSingleUser(form.name.data,form.email.data,form.phone_number.data)
	user = {'name':form.name.data, 'email':form.email.data, 'phone_number':form.phone_number.data}
	return render_template('success.html', title='Success', user = user)# name=form.name, email=form.email, phone_number=form.phone_number)


    #flash('Please check the entered data')
    return render_template('login.html', 
        title = 'Login',
        form = form)
	
    flash('Please check the entered data')
        #providers = app.config['OPENID_PROVIDERS'])


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)



