class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        tot_var = len(nums1) + len(nums2)
        if tot_var % 2 != 0:
            if len(nums1) == 0 and len(nums2) == 1 or len(nums2) == 0 and len(nums1) == 1:
                mid_var = 1
            else :
                mid_var = int(tot_var / 2)
            i=0
            j=0
            found = 0
            for co in range(mid_var +1):
                if len(nums1) != i and len(nums2) != j:
                    if nums1[i] < nums2[j]:
                        found = nums1[i]
                        i+=1
                    elif nums2[j] < nums1[i]:
                        found = nums2[j]
                        j+=1
                    elif nums2[j] == nums1[i]:
                        found = nums1[i]
                        i+=1
                elif len(nums1) == i and len(nums2) != j:
                        found = nums2[j]
                        j+=1
                elif len(nums1) != i and len(nums2) == j:
                        found = nums1[i]
                        i+=1
                print(str(found) +" " )
            return found
        else:
            mid_var = int(tot_var / 2)
            i = 0
            j = 0
            found_prev =0
            found = 0
            for co in range(mid_var + 1):
                found_prev = found
                if len(nums1) != i and len(nums2) != j:
                    if nums1[i] < nums2[j]:
                        found = nums1[i]
                        i += 1
                    elif nums2[j] < nums1[i]:
                        found = nums2[j]
                        j += 1
                    elif nums2[j] == nums1[i]:
                        found = nums1[i]
                        i += 1
                elif len(nums1) == i and len(nums2) != j:
                        found = nums2[j]
                        j += 1
                elif len(nums1) != i and len(nums2) == j:
                        found = nums1[i]
                        i += 1
                print(str(found_prev) + " "+str(found))
            print ((found + found_prev)/float(2))
            return (found + found_prev)/float(2)


