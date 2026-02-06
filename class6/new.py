import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

days = [1,2,3,4,5,6,7]
eating =         [6,7,8,6,3,6,4]
hours_sleep =    [9,8,8,9,10,7,6]
hours_working =  [6,6,6,7,6,2,4]
hours_freetime = [3,3,2,2,4,9,10]

plt.plot([],[],color="m",label = "Hours spent eating",linewidth = 2)
plt.plot([],[],color="b",label = "Hours spent sleeping",linewidth = 3)
plt.plot([],[],color="g",label = "Hours spent working",linewidth = 4)
plt.plot([],[],color="r",label = "Hours of freetime",linewidth = 5)

plt.stackplot(days,eating,hours_freetime,hours_sleep,hours_working,colors=["m","b","g","r"])

plt.xlabel("Day")
plt.title("Time distribution")
plt.legend()
plt.show()
