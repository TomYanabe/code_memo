import pandas as pd
import numpy as np

num_list = ["2","4"]

for num in num_list:
    df = pd.read_csv("dataset/dataset_all/dataset.csv")
    del df["Unnamed: 0"]

    #企業setの取得
    company_set = list(set(df["企業名称"]))
    company_name = sorted(company_set)
    company_num = len(company_name)

    print("get company name successfully!")

    #企業単位に分割
    companies = []
    for company in company_name:
        companies.append(df[df["企業名称"] == company])

    print("get company data successfully!")

    #------2:欠損値を企業の平均値で補完したもの-------
    if num == "2":
        print("start interpolate")
        data = []
        for target in companies:
            target = target.fillna(df.mean())
            data.append(target)
        df = pd.concat(data)
        print("interpolate successfully!")

    #------#4:欠損値を企業単位で線形補完したもの-------
    if num =="4":
        data = []
        for target in companies:
            target = target.interpolate(method='linear',limit_direction='both')
            data.append(target)
        df = pd.concat(data)
        print("interpolate successfully!")

    df = df.dropna()
    df = df.set_index(["企業名称","年度"])

    df.to_csv("dataset/dataset{}/dataset.csv".format(num),encoding='utf_8_sig')

    print("save successfully!")
