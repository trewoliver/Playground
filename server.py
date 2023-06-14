from flask import Flask, render_template # added render_template!

app = Flask(__name__)                     
    
@app.route('/')
@app.route('/play')                           
def showpage():
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html')  

@app.route('/play/<int:num>')
def moreboxes(num):
    return render_template('index2.html', num=num)

@app.route('/play/<int:num>/<color>')
def changecolor(num,color):
    # color=color
    return render_template('index3.html',num=num,color=color)






if __name__=="__main__":
    app.run(debug=True, port=5001)                   

