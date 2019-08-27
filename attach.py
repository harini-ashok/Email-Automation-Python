from flask import Flask, render_template, request
app = Flask(__name__,template_folder='template')

@app.route('/')
def student():
   return render_template('radio.html')

@app.route('/',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form.get['male']
      print(result)
      return result

if __name__ == '__main__':
   app.run(debug = True)
