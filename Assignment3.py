from pandas import DataFrame, read_excel
import matplotlib.pyplot as plt
#import xlrd
import pandas as pd
import numpy as np

file = 'cse425data.xlsx'
df = pd.read_excel(file, 'Sheet1')
#print(df['Name'])
print (df)
df_np = np.array(df)
#df_np.astype(float)
print(df_np)
#for x in np.nditer(df_np.T):
    #print(x, end=' ')
#plt.style.use("Student Attendance Pie Chart")
slices = [15,7,3,5]
labels = ['70%', '60&', '45%', '30%']
colors = ['#008fd5', '#dc4f38' , '#e5ae37', '#19ff19']
plt.pie(slices,labels=labels,colors=colors, wedgeprops={'edgecolor':'black'})
plt.title("Attendance Percentage Student Count")
plt.tight_layout()
plt.show()


objects = ('113', '131', '142', '151', '153', '161', '162', '171')
y_pos = np.arange(len(objects))
performance = [1,1,1,4,3,10,6,10]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Number of Students')
plt.title('ID-Wise Student Count')
plt.show()



"""
# Python3 program to find the sum 
# of each row and column of a matrix 

# import numpy library as np alias 
import numpy as np 

# Get the size m and n 
m , n = 4, 4		

# Function to calculate sum of each row 
def row_sum(arr) : 

	sum = 0

	print("\nFinding Sum of each row:\n") 

	# finding the row sum 
	for i in range(4) : 
		for j in range(4) : 

			# Add the element 
			sum += arr[i][j] 

		# Print the row sum 
		print("Sum of the row",i,"=",sum) 

		# Reset the sum 
		sum = 0


# Function to calculate sum of each column 
def column_sum(arr) : 

	sum = 0

	print("\nFinding Sum of each column:\n") 

	# finding the column sum 
	for i in range(4) : 
		for j in range(4) : 

			# Add the element 
			sum += arr[j][i] 

		# Print the column sum 
		print("Sum of the column",i,"=",sum) 

		# Reset the sum 
		sum = 0

		

# Driver code	 
if __name__ == "__main__" : 

	arr = np.zeros((4, 4)) 

	# Get the matrix elements 
	x = 1
	
	for i in range(m) : 
		for j in range(n) : 
			arr[i][j] = x 

			x += 1
				
	# Get each row sum 
	row_sum(arr) 

	# Get each column sum 
	column_sum(arr) 

# This code is contributed by 
# ANKITRAI1 

"""