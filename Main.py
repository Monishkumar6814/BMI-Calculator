from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('bmi.html')


@app.route('/calculate', methods=['POST'])
def calculate():

    weight = float(request.form['weight'])
    height = float(request.form['height'])

    # Convert height from cm to meter
    height_m = height / 100

    # Calculate BMI
    bmi = weight / (height_m * height_m)

    # Find category
    if bmi < 18.5:
        category = "Underweight"

    elif bmi < 25:
        category = "Normal weight"

    elif bmi < 30:
        category = "Overweight"

    else:
        category = "Obesity"

    return render_template(
        'bmi.html',
        bmi=round(bmi, 2),
        category=category
    )


if __name__ == '__main__':
    app.run(debug=True)