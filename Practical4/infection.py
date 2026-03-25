# Initialize variables
# a = current number of infected students (starting with 5)
# b = daily growth rate (40% increase = multiply by 1.4)
# c = day counter (starting from 0)
# d = total class population (91 students)
a=5
b=1.4
c=0
d=91
# Continue loop as long as infected count is less than total population
while a<d:
      # Increment day counter by 1
      c=c+1
      # Calculate new infected count for today
      # New infected = previous infected × growth rate
      a=a*b
      # Check if infected count exceeds total population
      # If yes, set it to exactly total population (cannot exceed d)
      if a>d:
            a=d
      print("day=",c,"infection number=",a)
print("total day is:",c)
# Display results
      