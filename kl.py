from scipy.stats import entropy
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 1)

x = [0,1,2,3,4,5,6,7,8,9]
y = [.01,.01,.02,.03,.1,.1,.4,.3,.02,.01]

n1 = norm.pdf(x, loc=6, scale=1)
n2 = norm.pdf(x, loc=3, scale=2)
ax.plot(x, y, 'r-', lw=2, alpha=0.6, label='real')
ax.plot(x, n1, 'b--', lw=2, alpha=0.6, label='normal1')
ax.plot(x, n2, 'g--', lw=2, alpha=0.6, label='normal2')


kl1 = entropy(y,n1)
print("kl1:", kl1)

kl2 = entropy(y,n2)
print("kl2:", kl2)

ax.legend(loc='best', frameon=False)
plt.show()