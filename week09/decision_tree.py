from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris(as_frane=True)
X_iris = iris.data[["petal length (cm)", "petal width (cm)"]].values
y_iris =