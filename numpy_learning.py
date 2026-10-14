import numpy
from scipy import stats
import matplotlib.pyplot as plt


speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)
x= numpy.median(speed)
x= stats.mode(speed)

# Standard deviation is a number that describes how spread out the values are.
# A low standard deviation means that most of the numbers are close to the mean (average) value.
# A high standard deviation means that the values are spread out over a wider range.
x = numpy.std(speed)

# Variance is another number that indicates how spread out the values are.
x = numpy.var(speed)

# Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.
x = numpy.percentile(speed, 75)
# 94 is the answer, which means 75 percent of the array is less that 94 speed

# create 250 array values between 0 and 5
x = numpy.random.uniform(0.0, 5.0, 250)

# create histogram, it creates 250 random values between 0 and 5 and equally distributed
x = numpy.random.uniform(0.0, 5.0, 250)
# plt.hist(x, 5)
# plt.show()

#normal distributed data creates 100000 values with mean as 5 and 1 as the standard deviation
x = numpy.random.normal(5.0, 1.0, 100000)
# plt.hist(x, 100)
# plt.show()

# scatter plot to distribute data between x and y axis
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()