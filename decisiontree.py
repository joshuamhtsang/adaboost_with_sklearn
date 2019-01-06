from sklearn import tree
import graphviz

X = [[1, 1], [0, 0], [1, 0], [0, 1]]
Y = [1, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

print(clf.predict([[0., 0.]]))

dot_data = tree.export_graphviz(clf, out_file=None,
                                class_names=['0', '1'])
graph = graphviz.Source(dot_data)
graph.render("basic")

from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

