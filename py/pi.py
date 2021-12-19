"""approximate value of pi"""
'''
Since the ratio of an area if a circle is inscribed in a square is π/4, we can calculate the approximate value of pi
'''

from random import uniform

# initialize variables for the number of points in and outside of a circle
in_ = 0
total = 0

# loop 1,000,000 times, increase the value for more a more accurate result
for _ in range(1_000_000):
    # generate 1 point
    x = uniform(0, 1)
    y = uniform(0, 1)
    # calculate its distamce from the origin
    distance = (x ** 2 + y ** 2) ** 0.5
    # check the distance and determine if it's in the circle
    if distance <= 1:
      in_ += 1
    total += 1

# since the value of in_/total is π/4, we multiply it by 4
print(in_/total*4)
