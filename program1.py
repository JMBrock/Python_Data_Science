from sklearn import tree
from sklearn import ensemble
from sklearn import naive_bayes

# Decision Tree Program

#[height, weight, shoe size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37],
	 [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40],
	 [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'female', 'female', 'female', 'male', 'male',
	 'male', 'female', 'male', 'female', 'male']

# GaussianProcessClassifier(1.0 * RBF(1.0))
# DecisionTreeClassifier(max_depth=5)
# RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1)

# clf = tree.DecisionTreeClassifier()
# clf = ensemble.RandomForestClassifier()
clf = naive_bayes.GaussianNB()

clf = clf.fit(X,Y)

prediction = clf.predict([[190, 70, 43]])

print(prediction)