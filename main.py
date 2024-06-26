"""
Problem: 
Find the Repeated Number in an Array
You are given an array of integers where one number is repeated. The array contains n+1 integers where each integer is between 1 and n (inclusive). 
Your task is to find the repeated number in the array.

Time Complexity: O(n)
Space Complexity: O(n)
"""

#Solution
def find_duplicate(nums):
	"""This function takes a list or array of integers 'nums' and returns the duplicated number"""
	#Create a empty dictionary to keep track of the numbers we see
	num_dict = {}
	#Iterate through the list
	for num in nums:
		#Check if the number is already in the dictionary
		if num in num_dict:
			#If the number is already in the dictionary, return the number
			return num
		else:
			#If the number is not in the dictionary, add it to the dictionary with a count of 1
			num_dict[num] = 1
	#If no duplicates is found (although the problem guarentees one exits)
	return None

#Test Cases
nums = [3,1,3,4,2]
nums_without_duplicate = [3,1,9,4,2]


#Print the result
print(f"The duplicate number is: {find_duplicate(nums)}")
print(f"The duplicate number is: {find_duplicate(nums_without_duplicate)}")
