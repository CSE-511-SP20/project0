import sys
import matplotlib.pyplot as plt

path = sys.argv[1]
f1 = open(path,'r')

lines = f1.readlines()

y1 = []

for line in lines:
    for i in range (0,1000):
        y1.append(line)
	
x = []
count = 1
for items in y1:
	x.append(count)
	count += 1

# plotting the line 1 points
line1, = plt.plot(x, y1, label = "Memory")

# naming the x axis
plt.xlabel('x-axis -> Time')
# naming the y axis
plt.ylabel('y - axis -> Memory in KB')
# giving a title to my graph
plt.title('Total Memory Consumption')

# show a legend on the plot
plt.legend(handles=[line1], loc=1)

# function to show the plot
plt.show()

