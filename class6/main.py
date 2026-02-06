# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,100)

# creating window to hold all subplots

plt.figure()

# creating first subplot, and where it should be displayed

plt.subplot(221)
# each subolot is reffered to as rowscolumnsindex with no spaces

plt.plot(x,x)
plt.title("y=x")

plt.subplot(222)
plt.plot(x,x**2)
plt.title("y=x^2")

plt.subplot(223)
plt.plot(x,np.sqrt(x))
plt.title("y=root(x)")

plt.subplot(224)
plt.plot(x,1/x)
plt.title("reciprocal x")

plt.tight_layout()
plt.show()
