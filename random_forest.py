#feature importance using random forest
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators=80, max_features='auto')
rf.fit(X_train, y_train)
print('Training done using Random Forest')

ranking = np.argsort(-rf.feature_importances_)
score=rf.feature_importances_[ranking]
label=X_train.columns.values[ranking]
importance_index = pd.Series(score,index=label)
#print(importance_index)
