from entities import Product
import repository

productList = repository.getData()

file = open("report.txt", "w")

file.write("Name|Quantity|Date\n")

for i in productList:
    file.write(i.name + "|" + str(i.quantity) + "|" + i.orderDate + "\n")

file.close()

print ("Finished")