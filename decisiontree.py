from sklearn import tree
import graphviz

# The training examples.

X = [[1, 1], [0, 0], [1, 0], [0, 1]]
Y = [1, 0, 1, 1]

# No limit max_depth decision tree.

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

print(clf.predict([[0., 0.]]))

dot_data = tree.export_graphviz(clf, out_file=None,
                                class_names=['0', '1'])
graph = graphviz.Source(dot_data)
graph.render("basic")

# max_depth=1 decision tree.

clf = tree.DecisionTreeClassifier(max_depth=1)
clf = clf.fit(X, Y)

dot_data = tree.export_graphviz(clf, out_file=None,
                                class_names=['0', '1'])
graph = graphviz.Source(dot_data)
graph.render("basic_maxdepth1")