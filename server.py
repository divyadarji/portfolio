from flask import Flask, render_template, url_for , redirect, request
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    print(url_for('static', filename='favicon.png'))
    return render_template('index.html')

@app.route('/contact.html')
def contacts():
    print(url_for('static', filename='favicon.png'))
    return render_template('contact.html')

@app.route('/about.html')
def about():
    print(url_for('static', filename='favicon.png'))
    return render_template('about.html')

@app.route('/works.html')
def works():
    print(url_for('static', filename='favicon.png'))
    return render_template('works.html')

@app.route('/index.html')
def index():
    print(url_for('static', filename='favicon.png'))
    return render_template('index.html')

@app.route('/thankyou.html')
def thank_you():
    return render_template('thankyou.html')

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email= data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email= data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer= csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message,])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method =='POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect(url_for('thank_you'))
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!!'


if __name__ == '__main__':
    app.run(debug=True)