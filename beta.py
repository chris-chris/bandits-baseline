from scipy.stats import beta
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 1)

# UCB : Deterministic / Requires update at every round
# TS : Probabilistic / Can accommodate delayed feedback / Better empirical evidence

# mean, var, skew, kurt = beta.stats(a, b, moments='mvsk')
x = np.linspace(0, 1, 100)
ax.plot(x, beta.pdf(x, 33, 100), 'r-', lw=3, alpha=0.6, label='banner1')
ax.plot(x, beta.pdf(x, 100, 223), 'g-', lw=3, alpha=0.6, label='banner2')
ax.plot(x, beta.pdf(x, 435, 611), 'b-', lw=3, alpha=0.6, label='banner3')

banner1_rvs = beta.rvs(33, 100, size=1)
banner2_rvs = beta.rvs(100, 223, size=1)
banner3_rvs = beta.rvs(435, 611, size=1)

print("banner1:", banner1_rvs)
print("banner2:", banner2_rvs)
print("banner3:", banner3_rvs)

ax.plot(banner1_rvs, 0, 'x', color='red')
ax.plot(banner2_rvs, 0, 'x', color='green')
ax.plot(banner3_rvs, 0, 'x', color='blue')

ax.legend(loc='best', frameon=False)
plt.show()