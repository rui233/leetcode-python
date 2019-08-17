# 可多次买进卖出

class Solution(object):
	def maxProfit(self,prices):
		"""

		:type prices:List[int]
		:rtype:int
		"""
		if len(prices) <= 1:
			return 0

		total = 0
		for i in range(1,len(prices)):
			if prices[i] > prices[i-1]:
				total += prices[i] - prices[i-1]

			return total
