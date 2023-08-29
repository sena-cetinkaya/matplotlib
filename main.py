# import the "matplotlib", "pandas" and "numpy" libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# We downloaded and read the "iris" dataset, one of the most well-known datasets.
data = pd.read_csv("iris.csv")
print(data.head())

# It is possible to create many kinds of graphics with this library. Let's create a few of them.
# Histogram Plot
"""plt.hist(data["variety"], label="Çeşitlilik")
plt.legend(loc=4)        # The "loc" value determines the position of the graphic label.(1: top right, 2: top left, 3: bottom left, 4: bottom right)
plt.show()"""

# Scatter Plot
"""plt.scatter(data["petal.length"],data["petal.width"])
plt.show()"""

# Line Plot
"""plt.plot(data["sepal.length"])
plt.show()"""

# Pie Plot
"""plt.pie(data["variety"].value_counts(), labels= data["variety"].unique())
plt.show()"""

""" 
Some frequently used functions in this library
plt.title() : Adding a title to a chart
plt.xlabel() : Naming the X-axis of the chart.
plt.ylabel() : Naming the Y-axis of the chart.
plt.show() : 
"""

# Showing two different data in one graph.
"""plt.figure(figsize=(12,6))
plt.plot(data["petal.width"], data["petal.width"], color="red")
plt.plot(data["sepal.length"], data["sepal.length"], color="blue")
plt.show()"""

# Drawing multiple graphs at once (subplot(row,column,which graph)).
"""plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
plt.plot(data["petal.width"], data["petal.width"], color="r")

plt.subplot(2,2,2)
plt.plot(data["sepal.length"], data["sepal.length"], color="blue")
plt.show()"""

# Nested Graph Drawing.
"""f=plt.figure(figsize=(12,4))
axes1=f.add_axes([0.1,0.1,0.8,0.8])               #coordinates
axes2=f.add_axes([0.6,0.2,0.2,0.3])
axes1.plot(data["petal.width"], data["petal.width"], color="blue")
axes2.plot(data["sepal.length"], data["sepal.length"], color="red")
plt.show()"""



