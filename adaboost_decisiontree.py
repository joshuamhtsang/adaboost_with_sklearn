from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
import graphviz

# The training examples.

X = [[1, 1], [0, 0], [1, 0], [0, 1]]
Y = [1, 0, 1, 1]

# Create and fit an AdaBoosted decision tree
abc = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1),
                         n_estimators=200)

abc.fit(X, Y)

print(abc.predict([[0., 0.]]))
