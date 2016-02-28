from entities import Product
from connections import ConnectionDetails
import connections
import pymssql

def getData(): 
    details = ConnectionDetails()
    
    conn = pymssql.connect(details.server, details.user, details.password, details.database)

    query = ("""SELECT TOP 1 OD.ProductID, PP.Name, SUM(OD.OrderQty), CAST(YEAR(OH.DueDate) AS VARCHAR(4))+'-'+CAST(MONTH(OH.DueDate) AS VARCHAR(2))+'-1'
    FROM Sales.SalesOrderDetail OD
    INNER JOIN Production.Product PP
        ON OD.ProductID = PP.ProductID
    INNER JOIN Sales.SalesOrderHeader OH
        ON OH.SalesOrderID = OD.SalesOrderID
    WHERE OD.ProductId IN (
        SELECT TOP 15 SOD.ProductId
            FROM Sales.SalesOrderDetail SOD
            GROUP BY SOD.ProductId
            ORDER BY SUM(SOD.OrderQty) DESC
    )
    GROUP BY OD.ProductID, PP.Name, CAST(YEAR(OH.DueDate) AS VARCHAR(4))+'-'+CAST(MONTH(OH.DueDate) AS VARCHAR(2))+'-1'
    ORDER BY PP.Name, CAST(YEAR(OH.DueDate) AS VARCHAR(4))+'-'+CAST(MONTH(OH.DueDate) AS VARCHAR(2))+'-1'""")

    productList = []

    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    while row:
        p = Product()
        p.id = int(row[0])
        p.name = str(row[1])
        p.quantity = int(row[2])
        p.orderDate = str(row[3])
        productList.append(p)
        row = cursor.fetchone()
    
    return productList