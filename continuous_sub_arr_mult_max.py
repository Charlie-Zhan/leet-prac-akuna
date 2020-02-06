class Solution:
    def maxProduct(self, nums):
        final_prod = nums[0]
        max_prod = nums[0]
        min_prod = nums[0]

        for elems in nums[1:]:
            loca_max = max(elems, max_prod * elems, min_prod * elems)
            local_min = min(elems, max_prod * elems, min_prod * elems)
            max_prod = loca_max
            min_prod = local_min
            final_prod = max(final_prod, max_prod)
        return final_prod

if __name__ == '__main__':
	s = Solution()
	ls = [-4,-3,-2]
    #ls = [2, 3, -2, 4]
	#ls = [-2, 3, -4]
	#ls = [0, -1]
    #ls = []
	print(s.maxProduct(ls))
        