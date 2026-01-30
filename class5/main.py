import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



# Simple line chart

days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
temp = [15,15,16,21,21,22,23,19,18,18,14,15,16,19,20,21,22,20,19,17,18,20,19,21,21,22,20,21,22,19]

plt.plot(days,temp)
plt.xlabel("Date")
plt.ylabel("Temperatute in Celsius")
plt.title("Temperature in June")
plt.legend()
plt.show()
# (x,y)

# -----------------------
# Bar chart

subjects = ["Math","Economics","Chemistry","Physics","English"]
grades = [30,30,50,40,50]
plt.bar(subjects,grades)
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.legend()
plt.show()

# ------------------------
# Pie chart

pets = ["Dog only","Cat only", "Cat and Dog", "Other", "No pets"]
pet_counts = [20,13,4,15,54]
plt.pie(pet_counts,labels=pets)
plt.legend()
plt.show()

# _----------------------
# scatter plot

height = [150,165,149,155,170,172,155]
weight = [54,66,60,59,55,70,72]
plt.scatter(height,weight)
plt.xlabel("Height of student (cm)")
plt.ylabel("Weight of student (kg)")
plt.legend()
plt.show()

# ---------------------------
# Histogram
marks = [40,50,60,70,80,90,100,90,90,90,80,30,30,30,30,40,50,70,90]
plt.hist(marks)
plt.xlabel("Marks")
plt.ylabel("Number of students")
plt.legend()
plt.show()

# ======================
# multiline plots
days = [1,2,3,4,5,6,7,8,9,10]
india_temp = [25,26,26,27,28,25,24,22,25,25]
europe_temp = [15,16,14,14,13,11,15,16,17,11]
plt.plot(days,india_temp,label="India")
plt.plot(days,europe_temp,label="Europe")
plt.xlabel("Date")
plt.ylabel("Temperature in C")
plt.legend()
plt.show()


# 
x_values = np.arange(-15,15,0.1)
linear_values = x_values*3
quadratic = x_values**2
cubic = x_values**3

plt.plot(x_values,linear_values,label = "Linear",linewidth = 1, linestyle = "-.")
plt.plot(x_values,quadratic, label = "Quadratic", linewidth = 2,linestyle = "--")
plt.plot(x_values,cubic, label = "Cubic",linewidth = 3,linestyle="-")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("graph")
plt.xlim(-5,5)
plt.ylim(-20,20)
plt.legend()
plt.show()

# ---------------------------------
