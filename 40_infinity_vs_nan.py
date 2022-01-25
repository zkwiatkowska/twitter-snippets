import numpy as np

print(np.nan == np.nan)          # FALSE
print(np.inf == np.inf)          # TRUE

print(np.nan == np.log(-1))      # FALSE
print(np.isnan(np.log(-1)))      # TRUE

print(-np.inf == np.log(0))      # TRUE

print(np.isnan(np.inf))          # FALSE
