import numpy as np
import sklearn
from scipy.linalg import khatri_rao
from sklearn.linear_model import SGDClassifier


# You are allowed to import any submodules of sklearn that learn linear models e.g. sklearn.svm etc
# You are not allowed to use other libraries such as keras, tensorflow etc
# You are not allowed to use any scipy routine other than khatri_rao

# SUBMIT YOUR CODE AS A SINGLE PYTHON (.PY) FILE INSIDE A ZIP ARCHIVE
# THE NAME OF THE PYTHON FILE MUST BE submit.py

# DO NOT CHANGE THE NAME OF THE METHODS my_fit, my_map, my_decode etc BELOW
# THESE WILL BE INVOKED BY THE EVALUATION SCRIPT. CHANGING THESE NAMES WILL CAUSE EVALUATION FAILURE

# You may define any new functions, variables, classes here
# For example, functions to calculate next coordinate or step length

################################
# Non Editable Region Starting #
################################
def my_fit( X_train, y_train ):
################################
#  Non Editable Region Ending  #
################################

	# Use this method to train your models using training CRPs
	# X_train has 8 columns containing the challenge bits
	# y_train contains the values for responses
	
	# THE RETURNED MODEL SHOULD BE ONE VECTOR AND ONE BIAS TERM
	# If you do not wish to use a bias term, set it to 0
 
	X_train = my_map(X_train)
	model = SGDClassifier(loss='hinge', max_iter=10000, tol=1e-3, random_state=42)
	model.fit(X_train, y_train)

	w = model.coef_
	b = model.intercept_
	return w, b


################################
# Non Editable Region Starting #
################################
def my_map( X ):
################################
#  Non Editable Region Ending  #
################################

	# Use this method to create features.
	# It is likely that my_fit will internally call my_map to create features for train points
	X = 1 - 2 * X
	suffix = np.flip(np.cumprod(np.flip(X, axis=1), axis=1), axis=1)
	f1 = np.concatenate((X,  suffix[:, :-1]), axis=1)

	row_indices, col_indices = np.triu_indices(f1.shape[1], 1)
	feat = f1[:, row_indices] * f1[:, col_indices]
  
	return feat


################################
# Non Editable Region Starting #
################################
def my_decode( w ):
################################
#  Non Editable Region Ending  #
################################

	# Use this method to invert a PUF linear model to get back delays
	# w is a single 65-dim vector (last dimension being the bias term)
	# The output should be four 64-dimensional vectors

	p = w[:-1].copy()
	q = np.zeros(64)
	r = p.copy()
	s = np.zeros(64)

	p[-1] += w[-1]
	r[-1] -= w[-1]

	min_val = min(p.min(), q.min(), r.min(), s.min())

	p -= min_val
	q -= min_val
	r -= min_val
	s -= min_val
 
	return p, q, r, s

