from scipy import stats



def welch(df,target_name,existing_index):
    df = df.dropna()
    welch_1_index = []
    welch_2_index = []
    welch_3_index = []
    add_indexes = []
    #3パターンでy_testによる分別
    pattern1_higher = df[df["次年度"+target_name] >= 0.95]
    pattern1_lower = df[df["次年度"+target_name] < 0.95]
    pattern2_higher = df[df["次年度"+target_name] >= 0.9]
    pattern2_lower = df[df["次年度"+target_name] < 0.9]
    pattern3_higher = df[df["次年度"+target_name] >= 0.95]
    pattern3_lower = df[df["次年度"+target_name] < 0.95]
    pattern3_lower = pattern3_lower[pattern3_lower["次年度"+target_name] > 0.8]

    indexes = df.columns.values.tolist()
    indexes = [l for l in indexes if "Unnamed" not in l]
    indexes = [l for l in indexes if "次年度" not in l]

    #既存指標を削除
    index_list = [l for l in indexes if l not in existing_index]
    p_list_1,p_list_2,p_list_3 = [],[],[]
    for index in index_list:
        try:
            value1,value2 = pattern1_higher[index].values,pattern1_lower[index].values
            t,p = stats.ttest_ind(value1, value2, equal_var = False)
        except:
            print(index)
        if p > 0.05:
            continue
        if index in existing_index:
            continue
        if index not in welch_1_index:
            p_list_1.append(p)
            welch_1_index.append(index)
            continue
    data1 = {}
    data1["index"] = welch_1_index
    data1["p"] = p_list_1
    data1 = pd.DataFrame(data1)
    data1 = data1.sort_values("p")
    for index in index_list:
        try:
            value1,value2 = pattern1_higher[index].values,pattern1_lower[index].values
            t,p = stats.ttest_ind(value1, value2, equal_var = False)
        except:
            print(index)
        if p > 0.05:
            continue
        if index in existing_index:
            continue
        if index in welch_1_index:
            continue
        if index not in welch_2_index:
            p_list_2.append(p)
            welch_2_index.append(index)
            continue
    data2 = {}
    data2["index"] = welch_2_index
    data2["p"] = p_list_2
    data2 = pd.DataFrame(data2)
    data2 = data2.sort_values("p")
    for index in index_list:
        try:
            value1,value2 = pattern1_higher[index].values,pattern1_lower[index].values
            t,p = stats.ttest_ind(value1, value2, equal_var = False)
        except:
            print(index)
        if p > 0.05:
            continue
        if index in existing_index:
            continue
        if index in welch_1_index:
            continue
        if index in welch_2_index:
            continue
            welch_3_index.append(index)
            p_list_3.append(p)
    data3 = {}
    data3["index"] = welch_3_index
    data3["p"] = p_list_3
    data3 = pd.DataFrame(data3)
    data3 = data3.sort_values("p")

    data = pd.concat([data1,data2,data3],axis=0)
    add_indexes = data["index"].values.tolist()
    return add_indexes
