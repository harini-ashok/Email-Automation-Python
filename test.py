from flask import Flask, render_template, request
app = Flask(__name__,template_folder='template')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/', methods=['POST'])

def getvalue():
    name = request.form['name']
    print(name)
    return name
if __name__ == '__main__':
    app.run(debug=True)
          
