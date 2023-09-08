# flask render_template example
 
from flask import Flask, render_template, request
 
# WSGI Application
# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name
app = Flask(__name__)
 
def visualize_booth(decimal_multiplicand, decimal_multiplier):
    return render_template("visualize.html")

# @app.route('/')
# def welcome():
#     return "This is the home page of Flask Application"
 
@app.route('/', methods=["GET", "POST"])
def gtg():
    if request.method == "POST":
        decimal_multiplicand = request.form.get("multiplicand")
        decimal_multiplier = request.form.get("multiplier")
        request.form.setdefault
        return visualize_booth(decimal_multiplicand, decimal_multiplier)
    return render_template('index.html')
 
if __name__=='__main__':
    app.run(debug = True)