from datetime import datetime
from flask import Flask, render_template, redirect, url_for

from Tools.DB import get_stored_solutions

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('solutions'))

@app.route('/solutions')
def solutions():
    solutions = get_stored_solutions()
    return render_template(
        'index.html',
        time= str(datetime.now())[11:-7], # Cut miliseconds
        length= 7 + len(solutions) if len(solutions) > 0 else 0, # Offset solutions starting @ 8
        solutions= solutions
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 443, debug= True)