from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return 'Hello, World! This is a basic Flask app.'

# Define another route
@app.route('/about')
def about():
    return 'This is the about page.'

# Run the Flask app if this script is executed
if __name__ == '__main__':
    app.run(debug=True)

# Test commit
