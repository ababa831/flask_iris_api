from sklearn import datasets, model_selection, svm, metrics, externals

iris = datasets.load_iris()
X_train, X_valid, y_train, y_valid = model_selection.train_test_split(
    iris.data, iris.target)

# Training by Support Vector Machine
clf = svm.SVC()
clf.fit(X_train, y_train)

# Validation
y_pred = clf.predict(X_valid)
accuracy = metrics.accuracy_score(y_valid, y_pred)
print("Accuracy score: ", accuracy)

# Saving trained model as .pkl by joblib
externals.joblib.dump(clf, "./models/iris_pretrained_svc.pkl")