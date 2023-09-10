import numpy as np
import matplotlib.pyplot as plt


# modelo de regressão: lida com dados independentes e faz uma previsão QUANTITATIVA baseada neles

# modelo de classificação: lida com dados independentes e faz uma previsão QUALITATIVA baseada neles

def f(x):
    return np.random.randn() + np.random.randn() * x


def f2(x):
    return np.random.randn() * x


x = np.linspace(-10, 10, 100)

plt.figure(0)
for i in range(50):
    plt.plot(x, f2(x))
plt.grid(True)

plt.figure(1)
for i in range(50):
    plt.plot(x, f(x))
plt.grid(True)

plt.show()
