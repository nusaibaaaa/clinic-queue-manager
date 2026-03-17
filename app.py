from flask import Flask, render_template, request, redirect
from queue_manager import add_patient, next_patient, get_queue, total_seen

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    queue = get_queue()      # get current queue
    total = total_seen()     # get total served patients
    return render_template('index.html', queue=queue, total=total)


# Register patient
@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('patient')

    if name:   # simple validation
        add_patient(name)

    return redirect('/')


# Call next patient
@app.route('/next')
def next():
    next_patient()
    return redirect('/')


# Run the app
if name == '__main__':
    app.run(debug=True)