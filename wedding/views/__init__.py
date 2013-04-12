from wedding import app

@app.route('/')
def hello():
    return 'Hello'
