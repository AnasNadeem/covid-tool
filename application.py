from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/', methods=['post', 'get'])
def index():
    if request.method == 'POST':
        place = request.form.get('place')
        needs = request.form.getlist('need')
        print(place)
        print(needs)

        return render_template('base.html')
    return render_template('index.html')