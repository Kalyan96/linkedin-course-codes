class Solution(object):
    def all_sum(self, arr):
        sum = 0
        for i in arr:
            sum += i
        return sum

    def compare_arrays(self, arr1, arr2):
        if len(arr1) != len(arr2):
            print("array lens not equal " + len(arr1) + "  " + len(arr2))
        else:
            for i in range(len(arr1)):
                if arr1[i] != arr2[i]:
                    return False
            return True

    def find_arr(self, target, curr):
        if len(curr) == 0:
            for i in range(0, len(target)):
                curr.append(1)
        for i in range(1, len(curr)):
            curr[i] = self.all_sum(curr)
        curr[0] = self.all_sum(curr)
        return curr

    def isPossible(self, target):
        curr = []
        curr = self.find_arr(target, curr)
        decsn = self.compare_arrays(target, curr)
        if min(target) > max(curr) and decsn == False:
            curr = self.find_arr(target, curr)
            decsn = self.compare_arrays(target, curr)
        else :
            return decsn

        """
        x >> sum of all in curr_arr
        i >> is 0-n-1 starting
        """
        """
        :type target: List[int]
        :rtype: bool
        """
