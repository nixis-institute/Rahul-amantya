from flask import Flask, redirect, url_for
app = Flask(__name__)

# @app.route('/home/<name>')
# def hellow_world(name):
#     return 'This is home page and %s '%name
# # @app.add_url_rule('/','/list','/detail')

# @app.route('/list/<int:p_id>')
# def list_page(p_id):
#     return 'This is list page %d'%p_id


@app.route('/admin')
def hello_admin():
    return 'Hello Admin'
    
@app.route('/guest/<guest>')
def hello_guest():
    return 'Hello %s as Guest'


@app.route('/user/<name>')
def hellow_user(name):
    if(name == 'Admin'):
        return redirect(url_for('Hello admin'))
    else:
        return redirect(url_for('Hello_guest', guest=name))




if(__name__=='__main__'):
    app.run()