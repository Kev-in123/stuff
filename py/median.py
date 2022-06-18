class MedianFinder: #class

    def __init__(self):
        """
        Initialize a list 
        """ 
        self.nums = []

    def addNum(self, num: int):
        """
        Function to add numbers to the list above
        """
        self.nums.append(num)

    def findMedian(self):
        """
        Calculate the median
        """
        self.nums.sort() # sort the numbers
        length = len(self.nums) # find the length
        middle = length//2  #get the middle index
        val = self.nums[middle] # find the middle value
        if length % 2 != 0: # if the length of the list is odd, return the value
          return val
        val2 = self.nums[middle - 1] # find the previous value if the length of the list is even 
        return (val + val2)/2 # return the value

# driver code
m = MedianFinder()
m.addNum(1)
m.addNum(10)
print(m.findMedian())
