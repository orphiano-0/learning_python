import statistics

numbers = [14, 23, 5, 12, 52, 523, 52, 52, 5, 12, 32, 12]

# central location of all data
print(statistics.harmonic_mean(numbers))
# calculate the average 
print(statistics.mean(numbers))
# print the value of the given data
print(statistics.median(numbers))
# return the most repeated value
print(statistics.mode(numbers))
# return the standard deviation
print(statistics.stdev(numbers))
# return the variance
print(statistics.variance(numbers))

