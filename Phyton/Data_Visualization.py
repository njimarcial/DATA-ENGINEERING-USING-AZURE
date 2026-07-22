# IMPORT DATA AND READ FILE
#Import library pandas
import pandas as pd
#Reading the CSV file
df = pd.read_csv("C:/Users/hp/OneDrive/Documents/Data set/Cleaned_Sales.csv")
# Confirm the file was found and read successfully
print(df.head())
#Understanding the dataset
print(df.info())
#Import Data Viz library
import matplotlib
#Import Package
import matplotlib.pyplot as plt
#impoort numpy for mathematical calculation
import numpy as np

"""""
#DATA VISUALIZATION USING PYTHON
Plotting x and y points
The plot() function is used to draw points (markers) in a diagram.
By default, the plot() function draws a line from point to point.
The function takes parameters for specifying points in the diagram.
Parameter 1 is an array containing the points on the x-axis.
Parameter 2 is an array containing the points on the y-axis.
If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.'''
#Draw a line in a diagram from position (1,8) to position (3,10):
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
plt.plot(xpoints, ypoints)
plt.show()

#Draw a line in a diagram from position (0,0) to position (6,250)
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])
plt.plot(xpoints, ypoints)
plt.show()
#Adding a marker to a line chart
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = "o")  # 'o' means Mark each point with a circle
plt.show()

ypoints = np.array([0, 6, 0, 25])
plt.plot (ypoints, marker = '*') ##'*' means Mark each point with a axterix
plt.show()
"""
## Using Linestyle
ypoints = np.array([3, 8, 1, 10])
plt.plot (ypoints, linestyle = 'dotted') ##'*' means Mark each point with a dot
plt.show()

ypoints = np.array([0, 6, 0, 25])
plt.plot(ypoints, marker = '*') # '*' means Mark each point with a astrerik
plt.show()
#Using Linestyle
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linestyle = 'dotted')
plt.show()
#Create Labels and Titels for a Plot
#With Pyplot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show()
#Add Grid Lines to a Plot
#With Pyplot, you can use the grid() function to add grid lines to the plot
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y, marker = 'o')
plt.grid()
plt.show()
#Display Multiple Plots
#With the subplot() function you can draw multiple plots in one figure
#Draw 2 plots
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1)
plt.plot(x,y)
#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.show()

#Creating Scatter Plots
'''
With Pyplot, you can use the scatter() function to draw a scatter plot.
The scatter() function plots one dot for each observation. It needs two arrays of the same length, one for the values of the x-axis, 
and one for values on the y-axis:'''
''
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)
plt.show()
#Creating Bars
#With Pyplot, you can use the bar() function to draw bar graphs:
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x,y)
plt.show()
# Another bar chart
x = ["APPLES", "BANANAS"]
y = [400, 350]
plt.bar(x, y)
plt.show()
# Plots a histogram
x = np.random.normal(170, 10, 250)
plt.hist(x)
plt.show() 
''
#Creating Pie Charts
#With Pyplot, you can use the pie() function to draw pie charts:
y = np.array([35, 25, 25, 15])
plt.pie(y)
plt.show()
