from sqlconnection import sqlconnect
def product_details(cnx):
    cursor=cnx.cursor()
    query=("select * from products")
    
    cursor.execute(query)
    response=[]
    for (producr_id,p_name,um_id,price) in cursor:
        response.append(
            {
               'producr_id':producr_id,
               'p_name':p_name,
               'um_id':um_id,
               'price':price 
            }
        ) 
    
    return(response)

def insert_products(cnx,product):
    cursor=cnx.cursor()
    query=("insert into products"
           "(p_name,um_id,price)"
           "values (%s,%s,%s)")
    
    data=(product['p_name'],product['um_id'],product['price'])
    
    cursor.execute(query,data)
    cnx.commit()
    return cursor.lastrowid

def delete_data(cnx,product_id):
    cursor=cnx.cursor()
    
    query=("delete from products where producr_id="+str(product_id))
    
    cursor.execute(query)
    cnx.commit()
    
if __name__=="__main__":
    connection=sqlconnect()
    print(product_details(connection))
    print(insert_products(connection,{
        'p_name':'rice',
        'um_id':'2',
        'price':'30'}))
    delete_data(connection,3)
