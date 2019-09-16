import matplotlib.pyplot as plt
import numpy as np

#https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?src=CF
x = [1947, 1914, 1912, 6100, 11464, 3014, 2229, 2306, 2363, 2814, 2930, 3027, 2730, 2116, 1514, 1079, 831, 789]
tpopboone = sum(x)
y = []
i = 2.5
print(tpopboone)
while i < 88:
    y.append(i)
    i += 5
print(y)
weighted = [m / (sum(x)) for m in x]
val = []
i = 0
for c in weighted:
    val.append(c * y[i])
    i += 1
print(weighted)

plt.subplot(1,2,1)
index = np.arange(len(y))
plt.bar(index, x)
plt.xticks(index, y, fontsize=5, rotation=30)

plt.subplot(1,2,2)
mu, sigma = 46, 13
x2 = [6.2,6.3,6.4,6.5,6.6,7.2,6.7,6.6,6.0,6.4,6.5,6.7,6.2,5.3,4.1,2.8,1.7,1.9]
x2 = [(m / 100) for m in x2]
xfinal = [(m * tpopboone) for m in x2]
plt.xticks(index, y, fontsize=5, rotation=30)
plt.bar(index, xfinal)
plt.savefig('pop.png', transparent=True)
plt.show()
