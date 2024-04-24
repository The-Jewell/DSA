# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1

#time taken 5:53

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        to_string_x = str(x)
        return to_string_x == to_string_x[::-1]


#tests 
test1 = Solution()
test2 = Solution()
test3 = Solution()

print(test1.isPalindrome(121))#expected true 
print(test2.isPalindrome(-121))#expected true 
print(test3.isPalindrome(10))#expected true 
