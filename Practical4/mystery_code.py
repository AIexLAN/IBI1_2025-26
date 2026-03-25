# What does this piece of code do?
# Answer:
# This code generates 11 random integers between 1 and 10, calculates their sum, and prints the total

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

# This initialized varieble will store the sum of all random numbers
total_rand = 0

# This variable acts as a counter to control how many times the loop runs
progress=0

# Start a while loop
while progress<=10:
	# Increase the 'progress' variable by 1 each time the loop runs
	progress+=1
	# Generate a random integer between 1 and 10
	n = randint(1,10)
	# Add the random number 'n' to the running total 'total_rand'
	total_rand+=n

# Print the final value of 'total_rand'
print(total_rand)

