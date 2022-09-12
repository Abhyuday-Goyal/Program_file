import csv
fields = ['Prod_ID','Prod_Name','Prod_Qty','Prod_Price' ]
rows = [[123,'iphone',65,200000],
        [124,'smartwatch',80,90000],
        [125,'ipad',10,100000]]
filename = 'products.csv'
with open(filename,'w', newline ='') as f:
    csv_w = csv.writer(f, delimiter='|')
    csv_w .writerow(fields)
    for i in rows:
        csv_w.writerow(i)
    print("created")
f1 = open('products.csv','r')
csv_reader = csv.reader(f1)
for r1 in csv_reader:
    print(r1)
f.close()