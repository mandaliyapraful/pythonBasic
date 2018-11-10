import matplotlib.pyplot as plt

year = [1950 ,1970 ,1990 ,2010,2030]
pop = [2.519,3.692,5.263,6.972,8.5]

# To plot as line 
plt.plot(year,pop)

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projection')
plt.yticks([0,2,4,6,8,10],
            ['0B','2B','4B','6B','8B','10B'])
# To plot only the dataset points we use sactter function
#plt.scatter(year,pop)
plt.show()