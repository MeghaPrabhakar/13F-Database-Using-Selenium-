import pandas as pd

def full_info():
    df=pd.read_csv(r'/Users/meghaprabhakar/PycharmProjects/DA2/out.csv')
    #print(df)
    df.to_csv('file_1.csv', mode='a', index=False, header=False)
full_info()

def full_info1():
    df=pd.read_csv(r'/Users/meghaprabhakar/PycharmProjects/DA2/out1.csv')
    #print(df)
    df.to_csv('file_2.csv', mode='a', index=False, header=False)
full_info1()