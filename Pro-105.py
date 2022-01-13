import csv
import plotly.express as px
import pandas as pd
with open("class2.csv",newline = "") as f :
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
total =0
items = len(file_data)
for i in file_data :
    total = total + float(i[1])
    
    
x=[]
mean = total/items
j=0
items = len(file_data)
for i in file_data :
    x[j] = float(i[1]) - mean
    j=j+1