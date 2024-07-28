from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/laba_1')
def laba_1():
    return render_template('laba_1.html')

@app.route('/laba_2')
def laba_2():
    return render_template('laba_2.html')

@app.route('/laba_3')
def laba_3():
    return render_template('laba_3.html')

@app.route('/laba_4')
def laba_4():
    return render_template('laba_4.html')

@app.route('/project')
def project():
    return render_template('project.html')

if __name__ == '__main__':
    app.run(debug=True)
