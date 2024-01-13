from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def calculator_form():
    return render_template('calculator.html')

@app.route('/', methods=['POST'])
def calculate():
    try:
        operation = request.form['operation']
        operand1 = float(request.form['operand1'])
        operand2 = float(request.form['operand2'])
        result = evaluate_expression(operation, operand1, operand2)
        return render_template('calculator.html', result=result)
    except Exception as e:
        return render_template('calculator.html', result='Error')

def evaluate_expression(operation, operand1, operand2):
    if operation == "ADD":
        return operand1 + operand2
    elif operation == "SUBTRACT":
        return operand1 - operand2
    elif operation == "MULTIPLY":
        return operand1 * operand2
    elif operation == "DIVIDE":
        if operand2 != 0:
            return operand1 / operand2
        else:
            raise ValueError("Division by zero is not allowed")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
