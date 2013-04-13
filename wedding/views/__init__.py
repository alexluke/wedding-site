from wedding import app
from helpers import templated

@app.route('/')
@templated()
def home():
    pass
