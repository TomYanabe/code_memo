import lightgbm as lgb
import numpy as np
import pandas as pd

params = {
         'objective': 'regression',
         'metric': 'rmse',
         'num_leaves': num_leanve,
         'learning_rate': learning_rate,
         'max_depth': max_depth,
         'num_iterations':n_estimators,
         'feature_fraction': feature_fraction,
         'subsample': subsample,
         'min_data_in_leaf': min_data_in_leaf,
         'verbose': 0
         }

train = train.loc[:,use_index]
test = test.loc[:,use_index]
val = val.loc[:,use_index]
train = train.dropna()
test = test.dropna()
val = val.dropna()
ytrain = train["次年度"+target]
ytest = test["次年度"+target]
yval = val["次年度"+target]
del train["次年度"+target]
del test["次年度"+target]
del val["次年度"+target]
Xtrain = train
Xtest = test
Xval = val
lgb_train = lgb.Dataset(Xtrain, ytrain)
lgb_eval = lgb.Dataset(Xval, yval, reference=lgb_train)
model = lgb.train(params, lgb_train, valid_sets=lgb_eval)
ypred = model.predict(Xtest, num_iteration=model.best_iteration)
