from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('new_ticket_form.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        application_name = request.form['application_name']
        issue_description = request.form['issue_description']
        category = request.form['category']
        urgency = request.form['urgency']
        sid = request.form['sid']
        # Process form data as needed
        return f"Form submitted with Application Name: {application_name}, Issue Description: {issue_description}, Category: {category}, Urgency: {urgency}, SID: {sid}"

if __name__ == '__main__':
    app.run(debug=True)

