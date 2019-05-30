from sklearn.metrics import mean_squared_error as mse
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

#分岐
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

scaler = StandardScaler()

scaler.fit(x_train)


clf_lasso = linear_model.LassoCV(alphas=10 ** np.arange(-6, 1, 0.1), cv=5)
clf.fit(scaler.transform(X_train), y_train)

y_pred = clf_lasso.predict(scaler.transform(X_test))
data = {}
coefficient = clf_lasso.coef_
index_list = X_train.columns.values
indexes = []
coefficients = []
for i in range(len(index_list)):
    if index_list[i]  not in existing_index:
        indexes.append(index_list[i])
        coefficients.append(coefficient[i])
#index_list = [l for l in index_list if l not in existing_index]
data["coefficient"] = coefficients
data["index"] = indexes
rf = pd.DataFrame(data)
rf.drop(rf.index[rf.coefficient == 0], inplace=True)
rf.to_csv("result/lassoCV_dataset"+num+".csv",encoding="utf_8_sig")

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
