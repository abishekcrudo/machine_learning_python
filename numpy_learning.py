import numpy
from scipy import stats
import matplotlib.pyplot as plt
from sklearn import linear_model


speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

#x = numpy.mean(speed)
#x= numpy.median(speed)
#x= stats.mode(speed)

# Standard deviation is a number that describes how spread out the values are.
# A low standard deviation means that most of the numbers are close to the mean (average) value.
# A high standard deviation means that the values are spread out over a wider range.
#x = numpy.std(speed)

# Variance is another number that indicates how spread out the values are.
#x = numpy.var(speed)

# Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.
#x = numpy.percentile(speed, 75)
# 94 is the answer, which means 75 percent of the array is less that 94 speed

# create 250 array values between 0 and 5
#x = numpy.random.uniform(0.0, 5.0, 250)

# create histogram, it creates 250 random values between 0 and 5 and equally distributed
#x = numpy.random.uniform(0.0, 5.0, 250)
# plt.hist(x, 5)
# plt.show()

#normal distributed data creates 100000 values with mean as 5 and 1 as the standard deviation
#x = numpy.random.normal(5.0, 1.0, 100000)
# plt.hist(x, 100)
# plt.show()

# scatter plot to distribute data between x and y axis
#x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
#y = [99,86,87,88,111,86,103,87,94,78,77,85,86]


#-------------------------------------------LINEAR-REGRESSION-------------------------------------------------------
'''
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

plt.scatter(x, y)
plt.show()
'''
#-------------------------------------------LOGISTIC REGRESSION----------------------------------------------------------

#below is mathematical calculation for sigmoid function
'''---------------
b = 1
x = [0, 10, 2]
w = [2, -1, 5]
y = b + numpy.dot(w,x)
print("The value of y based on given x and slope values:" , y) #linear value

def sigmoid(z):
    return 1 / (1 + numpy.exp(-z))

predicted_value = sigmoid(y)
print("The predicted sigmoid probabilty for the y to right or wrong:" , predicted_value)
----------------'''

# below example shows how to execute sigmoid function using python regression
'''-------------------------------
X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

logr = linear_model.LogisticRegression() # making the object as model for logistic regression
logr.fit(X,y) # fit is the function to input x and y values
predicted = logr.predict(numpy.array([3.46]).reshape(-1,1)) # predicted is the answer for x as 3.46, and predicting the value of y for it
print(predicted)
----------------------------'''

#below is calculating coeffecient for log-loss in the logistic regression
X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

logr = linear_model.LogisticRegression()
logr.fit(X,y)

log_odds = logr.coef_
print("Calculating the coefficent of log odds for the x , y values: ", log_odds)
odds = numpy.exp(log_odds)

print("Calculating the log odds: ", odds)