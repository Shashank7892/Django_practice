from flask import Flask,jsonify,request
import product_dao
from sqlconnection import sqlconnect

app=Flask(__name__)

connection=sqlconnect()
@app.route('/getProducts',methods=['GET'])
def get_products():
    
    products=product_dao.product_details(connection)
    response=jsonify(products)
    response.headers.add('Access-Control-Allow-Origin','*')
    
    return response

@app.route('/deleteProduct',methods=['POST'])
def delete_product():
    
    return_id=product_dao.delete_data(connection,request.form['product_id'])
    response=jsonify({'product_id':return_id}) 
    return response   


if __name__=="__main__":
    print("starting the server")
    app.run(port=5000)