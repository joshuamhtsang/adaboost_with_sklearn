from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import graphviz
from sklearn.datasets import load_iris

import os

TREE_DIAGRAM_DIR_NAME = 'tree_diagrams'
N_ESTIMATORS = 10

if __name__ == '__main__':
    # The training examples.

    X = [[1, 1], [0, 0], [1, 0], [0, 1]]
    Y = [1, -1, 1, 1]

    # Create and fit an AdaBoosted decision tree
    abc = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1),
                             n_estimators=N_ESTIMATORS)
    abc.fit(X, Y)

    print(abc.estimator_weights_)

    # Make a directory to contain tree diagrams.

    if not os.path.isdir(TREE_DIAGRAM_DIR_NAME):
        os.mkdir(TREE_DIAGRAM_DIR_NAME)

    for i in range(0, N_ESTIMATORS):
        dot_data = tree.export_graphviz(abc.estimators_[i], out_file=None,
                                        class_names=['-1', '+1'])
        graph = graphviz.Source(dot_data)
        graph.render(os.path.join(TREE_DIAGRAM_DIR_NAME, "abc"+str(i)))

    # Make some predictions.
    print(abc.predict([[0., 0.]]))
    print(abc.predict([[1., 1.]]))
    print(abc.predict([[1., 0.]]))
    print(abc.predict([[0., 1.]]))

