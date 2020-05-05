import test_info
import pandas as pd
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)

df=pd.read_csv("test.csv")
dirmail=[]

print("Enter starting row and ending row : ")
rowinit=int(input("Start:"))
rowend=int(input("End:"))

for i in range(rowinit-2,rowend-1):
    comp_name=df.at[i,'name']
    print("Company Name: ",comp_name)

    dirmail=test_info.spider(comp_name)

    df.at[i,'ceo']=dirmail[0]
    df.at[i,'email']=dirmail[1]
    print("Entered Successfully......")
    df.to_csv('updated.csv')
    print("updated.csv saved successfully")

print("Data fetched successfully")