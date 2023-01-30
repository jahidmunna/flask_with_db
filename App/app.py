from flask import Flask, render_template, request, redirect, url_for

from model import db, Users

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@db/postgres'
db.init_app(app)


@app.route('/')
def index():
    users = Users.query.all()
    return render_template('index.html', users=users)


@app.route('/input', methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        user = Users(username=username, email=email)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('input.html')


if __name__ == '__main__':
    with app.app_context():
        try:
            db.create_all()
            print("created!")
        except Exception as e:
            print("Error: ", e, flush=True)
    app.run()
