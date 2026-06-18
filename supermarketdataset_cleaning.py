import pandas as pd
import numpy as np

df=pd.read_csv("/content/SampleSuperstore.csv")
print(df.head())

#check if there is any null value
print(df.isna().sum())
#check if there are any duplicates
print(df.duplicated().sum())
df[df.duplicated(keep=False)].sort_values(by=df.columns.tolist())
#remove duplicates
df = df.drop_duplicates()
#verifying all duplicates are removed
print(df.duplicated().sum())

print(df.info())

df.describe()

df[df['Sales'] < 0]
df[df['Quantity'] <= 0]
df[df['Profit'] < 0] #to find loss

df[df['Profit'] < 0] #checking situation where profit is in neg(i-e loss)

df[df['Profit'] < 0]['Profit'].sum() #checking overall loss
df.groupby('Category')['Profit'].sum().sort_values()
df.groupby('Sub-Category')['Profit'].sum().sort_values() #checking where loss is happening
df.groupby('Sub-Category')['Profit'].sum().sort_values().plot(kind='bar') #plotting reason for loss in graph

df[['Discount', 'Profit']].corr()
#neg shows Profit and Discount have inverse propotional relation

#loss making transactions
df[df['Profit'] < 0][['Sub-Category', 'Sales', 'Discount', 'Profit']]

df['Category'].unique() #to check for spelling errors
df['Region'].unique()

df.groupby('Region')['Sales'].sum().plot(kind="bar") #sales per region

df.groupby('Segment')['Sales'].sum().plot(kind='bar')

df[df['Sub-Category'] == 'Tables'][['Sales','Discount','Profit']] #checking why tables are generating loss

df.groupby('Sub-Category')['Profit'].sum() / df.groupby('Sub-Category')['Sales'].sum() #checking profit margin earned

df.to_csv("cleaned_superstore_data.csv", index=False)
from google.colab import files
files.download("cleaned_superstore_data.csv")
