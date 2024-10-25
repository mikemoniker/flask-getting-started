from flask import Flask, request, render_template_string

app = Flask(__name__)


def show_the_login_form():
    return render_template_string('''
    <form action="/login" method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>
        
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>
        
        <button type="submit">Login</button>
    </form>
    ''')


def do_the_login():
    return 'Do the login'

@app.route("/")
def hello_world():
    return "<p>Hello, <strong>Jordan</strong>! That was fast</p>"

@app.route('/hello/')
def hello():
    return 'Hello, from Hello Route'


@app.route('/post/<int:post_id>/')
def show_post(post_id):
    result = ''
    for i in range(post_id + 1):  # Loop from 0 to post_id (inclusive)
        result += f'Post {i}\n'
    return result

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

@app.route('/search')
def search():
    # Get the 'q' query parameter
    query = request.args.get('q')
    return f'You searched for: {query}'