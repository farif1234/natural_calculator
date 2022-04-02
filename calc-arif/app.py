from flask import *
from math import *

app = Flask(__name__)

def calculate(exp):
    exp = exp.replace(' ', '')
    exp = exp.lower()
    exp_dict = {'squared':'**2', 'plus':'+', 'times':'*', 'minus':'-', 'tothe':'**', 'x':'*', '^':'**'}
    for expr, num_expr in exp_dict.items():
        if expr in exp:
            exp = exp.replace(expr, num_expr)
    try:
        return eval(exp)
    except:
        return 'ERROR'

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        exp = request.form['inp']
        if exp != '':
            return render_template('calc.html', new_text = calculate(exp), first_time = False, exp = exp)
    return render_template('calc.html', new_text = 'Waiting...', first_time = True)

@app.route('/about', methods = ['POST', 'GET'])
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
