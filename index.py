from flask import *
app = Flask(__name__);

import json;

@app.route('/index',methods = ['post','get'])
@app.route('/',methods = ['post','get'])
def index():
    if (request.method == 'POST'):
        mydata= dict(request.form);
    elif(request.method == 'GET'):
        mydata = dict(request.args);
    return render_template("index.html",mydata=mydata);

#*************************************************************

@app.route('/json',methods = ['post','get'])
def myjson():
    if(request.method == 'GET'):
        mydata = dict(request.args);
        return jsonify(mydata);
        
#*************************************************************

@app.route('/otra',methods=['GET'])
def Truck_Details():
    Details= {'id':2,'year':2019,'model':'nuevo'}
    return Details

if __name__ == '__main__':
   app.run(debug = True);