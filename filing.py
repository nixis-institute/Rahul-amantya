import pandas as pd

def fill_data():
    df = pd.read_csv('putting_value.csv') # input file 
    fd = open('final_product.csv','w',encoding='utf-8') # output file
    ky = df.keys()
    for i in range(len(df.keys())):
        df[ky[i]] = df[ky[i]].fillna(df[ky[i]].value_counts().index[0])
    df.to_csv(fd)
    fd.close()

fill_data()
