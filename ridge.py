from sklearn.linear_model import RidgeCV

def Ridge(train,test,target,use_index):
    use_index.append("次年度"+target)
    use_index = [l for l in use_index if l in train.columns.values.tolist()]
    train = train.loc[:,use_index]
    test = test.loc[:,use_index]
    train = train.dropna()
    test = test.dropna()
    ytrain = train["次年度"+target]
    ytest = test["次年度"+target]
    del train["次年度"+target]
    del test["次年度"+target]
    Xtrain = (train - train.mean()) / train.std(ddof=0)
    Xtest = (test - test.mean()) / test.std(ddof=0)
    model = RidgeCV()
    model.fit(Xtrain, ytrain)
    ypred = model.predict(Xtest)
    return ytest,ypred
