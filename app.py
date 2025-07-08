from flask import Flask, request, render_template
from mmm_model import load_model, optimize_budget

app = Flask(__name__)

# Fit the model once at startup
MODEL = load_model()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        budget = float(request.form['budget'])
        periods = int(request.form['periods'])
        allocation = optimize_budget(MODEL, budget, periods)
        return render_template('result.html', allocation=allocation, budget=budget, periods=periods)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
