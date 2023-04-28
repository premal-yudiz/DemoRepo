from flask import url_for, redirect, render_template, request
from flask import Flask
app = Flask(__name__)


@app.route('/')
def admin():
    return render_template('get_post.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('userName')
        passWord = request.form.get('userPass')
        # user=request.form['userName']
        # passWord=request.form['userPass']
        if user == 'premal' and passWord == '1234':
            return 'WElcome %s' % user
        else:
            return 'Login not valid %s' % user
    else:
        # if request.method == 'POST':
        user = request.form.get['userName']
        passWord = request.form.get['userPass']
        print(user, passWord)
        if user == 'premal' and passWord == '1234':
            return 'WElcome %s' % user
        else:
            return 'Login not valid %s' % user
        # user = request.args.get('userName')
        # passWord = request.args.get('userPass')

        # if user == 'premal' and passWord == '1234':
        #     return 'WElcome %s' % user
        # else:
        #     return  'Login not valid %s' %user


if __name__ == "__main__":
    app.run(debug=True)
