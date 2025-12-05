
import pandas as pd
from io import StringIO

csv_text = """
OrderID,OrderDate,ShipDate,Region,City,CustomerID,CustomerName,Segment,Category,SubCategory,ProductName,Quantity,UnitPrice,Discount,Sales,Profit,Returned
"1001","2024-01-02","2024-01-05","West","Los Angeles","C001","David Miller","Consumer","Technology","Laptops","HP Pavilion 15",1,720,0,720,95,"No"
"1002","2024-01-02","2024-01-06","Central","Chicago","C002","Sarah Johnson","Corporate","Furniture","Chairs","ErgoMax Pro Chair",2,140,0.1,252,30,"No"
"1003","2024-01-03","2024-01-07","East","New York","C003","John Lee","Home Office","Office Supplies","Binders","Premium Binder Pack",5,12,0,60,11,"No"
"1004","2024-01-03","2024-01-08","South","Miami","C004","Ana Gomez","Consumer","Technology","Phones","Samsung Galaxy A54",1,399,0.05,379.05,48,"No"
"1005","2024-01-04","2024-01-09","West","Seattle","C005","Karen Black","Consumer","Furniture","Tables","Oak Wooden Table",1,450,0,450,52,"Yes"
"1006","2024-01-04","2024-01-08","Central","Denver","C006","Robert Brown","Corporate","Office Supplies","Pens","Blue Pen Pack (20)",3,8,0,24,5,"No"
"1007","2024-01-05","2024-01-10","East","Boston","C007","Emily Davis","Consumer","Technology","Accessories","Wireless Mouse",4,18,0,72,14,"No"
"1008","2024-01-05","2024-01-11","South","Atlanta","C008","Kyle Young","Home Office","Furniture","Chairs","ComfortMesh Chair",1,160,0.15,136,19,"No"
"1009","2024-01-06","2024-01-12","West","Portland","C009","Sophia Hill","Consumer","Technology","Phones","iPhone SE",2,429,0,858,115,"No"
"1010","2024-01-06","2024-01-13","Central","St. Louis","C010","Tom Harris","Corporate","Office Supplies","Paper","A4 Copier Paper (500)",10,5,0,50,6,"No"
"1011","2024-01-07","2024-01-14","East","Philadelphia","C011","Olivia Adams","Home Office","Furniture","Tables","Adjustable Standing Desk",1,320,0.1,288,35,"No"
"1012","2024-01-07","2024-01-15","South","Orlando","C012","Ethan Clark","Consumer","Technology","Accessories","USB-C Cable",6,9,0,54,12,"No"
"1013","2024-01-08","2024-01-16","West","San Diego","C013","Isabella Scott","Consumer","Furniture","Sofas","Modern Sofa 3-Seater",1,850,0.2,680,88,"Yes"
"""

df = pd.read_csv(StringIO(csv_text))
df.to_csv("superstore_dataset.csv", index=False)
