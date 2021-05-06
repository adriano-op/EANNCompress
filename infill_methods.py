import numpy as np

def rand(n,X,F,G=[]):
    random_indices = np.random.choice(X.shape[0], size=n, replace=False)
    nX = X[random_indices,:]
    nF = F[random_indices,:]
    nG = nG = G[random_indices,:] if G else []
    return {'X':nX,
            'F':nF,
            'G':nG}
