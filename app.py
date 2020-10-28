from flask import Flask, render_template
import request

app = Flask(__name__)


def convert(decimal_num):
    roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
     90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    num_to_roman = ''
    for i in roman.keys():
        num_to_roman += roman[i] * (decimal_num // i)
        decimal_num %= i
    return num_to_roman


print('3 --', convert(3))
print('9 --', convert(9))
print('58 --', convert(59))
print('1994 --', convert(1994))

@app.route('/', methods=['GET'])    
def main_get():
    return render_template('index.html', not_valid=False, developer_name='Abdullah')

@app.route('/', methods=['POST']) 
def main_post():
    alphaNumeric = request.form['alpha']
    if not alphaNumeric.isdecimal():
        return render_template('index.html', not_valid = True, developer_name='Abdullah')
    number = int(alphaNumeric)
    if not (0 < number < 4000):
        return render_template('index.html', not_valid = True, developer_name='Abdullah')
    return render_template('result.html', number_decimal = number, number_roman = convert(number), developer_name='Abdullah')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)


