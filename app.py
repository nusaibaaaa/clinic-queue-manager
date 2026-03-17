from flask import Flask, render_template, request, redirect
from queue_manager import add_patient, next_patient, get_queue, total_seen

app = Flask(__name__)

@app.route('/')
def home():
    queue = get_queue()
    total = total_seen()
    return render_template('index.html', queue=queue, total=total)

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('patient')

    if name:
        add_patient(name)

    return redirect('/')

@app.route('/next')
def next():
    next_patient()
    return redirect('/')

if name == '__main__':
    app.run(debug=True)