from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import graphviz

# The training examples.

X = [[1, 1], [0, 0], [1, 0], [0, 1]]
Y = [1, -1, 1, 1]

# Create and fit an AdaBoosted decision tree
abc = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1),
                         n_estimators=200)
abc.fit(X, Y)

print(abc.estimator_weights_)

# Output graph for estimator 0

dot_data = tree.export_graphviz(abc.estimators_[0], out_file=None,
                                class_names=['-1', '+1'])
graph = graphviz.Source(dot_data)
graph.render("abc1")

# Output graph for estimator 1

dot_data = tree.export_graphviz(abc.estimators_[1], out_file=None,
                                class_names=['-1', '+1'])
graph = graphviz.Source(dot_data)
graph.render("abc2")

print(abc.predict([[0., 0.]]))
print(abc.predict([[1., 1.]]))
print(abc.predict([[1., 0.]]))
print(abc.predict([[0., 1.]]))

