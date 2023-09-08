# flask render_template example
 
from flask import Flask, render_template, request
 
# WSGI Application
# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name
app = Flask(__name__)

def decimalToBinary(num):
    partial_binary = "{0:b}".format(int(num))
    # partial_binary_length = len(partial_binary)
    # if partial_binary_length < 3:
    #     new_binary = '0' + partial_binary
    # elif partial_binary_length > 4:
    #     print("\nYou cannot enter numbers outside of [-7,7]\n")
    # else:
    #     new_binary = partial_binary
    # if int(num) >= 0:
    #     final_binary = '0' + new_binary
    # else:
    #     final_binary = '1' + new_binary

    return partial_binary
    


def ASR(R, A, Aextra):
    pass
    

def visualize_booth(decimal_multiplicand, decimal_multiplier):
    A = int(decimal_multiplicand.strip())
    A_binary = decimalToBinary(A)
    print(A_binary)
    C = int(decimal_multiplier)
    C_binary = decimalToBinary(C)
    print(C_binary)
    Aextra=0
    Azero = 0
    R=0
    R_binary= decimalToBinary(R)
    n=4
    while (n>0):
        if (Azero != Aextra):
            if (Aextra==0):
                R=R-C
            else:
                R=R+C
        ASR(R, A, Aextra)
        n-=1
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