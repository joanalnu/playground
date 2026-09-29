import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 1000)

base = 10
prime = 5

n = 3
m = 7

# general exponential
y1 = np.emath.logn(x**(n*m), base) # general exponential
y2 = np.emath.logn((x**(n*m)) % prime, base) # modular arithmetic

# plot
plt.plot(x, y1, label="regular")
plt.plot(x,y2,label="modular")
plt.legend()
plt.grid(True, alpha=0.5)
plt.ylim(0.0, 1.0)
plt.show()

