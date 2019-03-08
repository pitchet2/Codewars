
#    /3/
#   \7\ 4 
#  2 \4\ 6 
# 8 5 \9\ 3
# Here comes the task...
# Let's say that the 'slide down' is a sum of consecutive numbers from the top to the bottom of the pyramid. As you can see, the longest 'slide down' is 3 + 7 + 4 + 9 = 23
# 
# Your task is to write a function longestSlideDown (in ruby: longest_slide_down) that takes a pyramid representation as argument and returns its' longest 'slide down'. For example,
# 
# longestSlideDown([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]])
# # => 23

def longest_slide_down(pyramid):
    for i in reversed(range(len(pyramid))):
        for j in range(0, i):
            pyramid[i - 1][j] += max(pyramid[i][j], pyramid[i][j + 1])
            print(pyramid)
    return pyramid[0][0]
