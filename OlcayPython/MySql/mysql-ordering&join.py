import mysql.connector

def insertProduct(name,price,imageURL,description):
    connection = mysql.connector.connect(host ="localhost",user="root",password="****",database="node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO products(name,price,imageURL,description) VALUES (%s,%s,%s,%s)"
    values = (name,price,imageURL,description) #kendi elimizle de veri girebilirdik fakat bu veriyi kullancıdan aldırır

    cursor.execute(sql,values)
    
    try:
        connection.commit()  #Sorguladığımız bilgileri database'e gönderiyor
        print(f"{cursor.rowcount} tane kayıt eklendi") 
        print(f"son eklenen kaydın id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata:",err)
    
    finally:
        connection.close()
        print("database bağlantısı kapandı.")

def insertProducts(list):
    connection = mysql.connector.connect(host ="localhost",user="root",password="****",database="node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO products(name,price,imageURL,description) VALUES (%s,%s,%s,%s)"
    values = list

    cursor.executemany(sql,values)
    
    try:
        connection.commit()  #Sorguladığımız bilgileri database'e gönderiyor
        print(f"{cursor.rowcount} tane kayıt eklendi") 
        print(f"son eklenen kaydın id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata:",err)
    
    finally:
        connection.close()
        print("database bağlantısı kapandı.")

def getProducts():
    connection = mysql.connector.connect(host="localhost",user = "root",password ="mysql123",database ="node-app")
    cursor = connection.cursor()
    
    # cursor.execute("Select * From products Where id = 1")  # * işaretiyle bütün kolonları kastediyoruz ve where ile filtreleme yaparız
    # cursor.execute("Select * From products Where name = 'Samsung s8'and price=3000")
    # cursor.execute("Select * From products Where name LIKE '%Samsung%'")  #samsung geçenleri getirme
    # cursor.execute("Select * From products Where name LIKE '%Samsung%' and price =3000") 
    # cursor.execute("Select * From products Order By name")  #sıralama işlemi isme göre fiyata göre vs ne istersek
    # cursor.execute("Select * From products Order By price DESC")  #azalan bir şekilde sıralama için
    
    #### join konusu için yapılacaklar aşağıda###
    # sql = "Select * From Products"
    # sql = "Select * from products inner join categories on categories.id=products.categoryid"
    # sql = "Select products.name,products.price,categories.name from products inner join categories on categories.id=products.categoryid"
    # sql = "Select products.name,products.price,categories.name from products inner join categories on categories.id=products.categoryid where Categories.name = 'Telefon'"
    # sql = "Select products.name,products.price,categories.name from products inner join categories on categories.id=products.categoryid where Products.name = 'Samsung s8'"
    sql = "Select p.name,p.price,c.name from products as p inner join categories as c on c.id=p.categoryid where p.name = 'Samsung s8'" #böyle kısaltarak da yazabiliriz

    cursor.execute(sql)
    try:
        result = cursor.fetchall()  #birden fazla kayıt almak istediğimiz zaman kullanılan metot
        for product in result:
         print(product)
    except mysql.connector.Error as err:
        print("hata:", err)
    finally:
        connection.close()
        print("data bağlantısı kapandı")


getProducts()

# def getProductsId(id):
#     connection = mysql.connector.connect(host="localhost",user = "root",password ="***",database ="node-app")
#     cursor = connection.cursor()

#     sql = "Select * From Products Where id=%s"
#     params=(id,)

#     cursor.execute(sql,params)

#     result = cursor.fetchone()

#     print(f"id: {result[0]} name:{result[1]} price: {result[2]}")
# getProductsId(3)


