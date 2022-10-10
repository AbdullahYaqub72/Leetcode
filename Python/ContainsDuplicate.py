#Name: Abdullah Yaqub
#Username: AbdullahYaqub72
#Approach: If elements are not repeated then set should be equal to list elements

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set_list=set(nums)
        list_set=list(set_list)
        if len(nums)==len(list_set):
            return False
        else:
            return True