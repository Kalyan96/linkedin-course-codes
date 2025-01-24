class Solution(object):
    def swapPairs(self, head):
        ret = []
        for i in range(0,int(len(head)),2 ):
                ret.append(head[i+1])
                ret.append(head[i])
        return ret

    def reverse(self, x):
        stx = ""
        if x > -1*(2**31) and x < 2**31-1:
            if x >= 0:
                for char in str(x):
                    stx = char + stx
                # print(int(stx))
            else :
                for char in str(x):
                    if not (char == "-"):
                        stx = char + stx
                stx = "-"+stx
                # print(int(stx))
            if int(stx) > -1*(2**31) and int(stx) < 2**31-1:
                return int(stx)
            else :
                return 0
        else:
            return 0

    def myAtoi(self, s):
        strs = ""
        ints = 0
        first_int_found = 0
        for i in s:
            if (i=="0") or (i=="1") or (i=="2") or (i=="3") or (i=="4") or (i=="5") or (i=="6") or (i=="7") or (i=="8") or (i=="9")  :
                if first_int_found == 0 :
                    strs = strs + "0"
                strs = strs + i
                first_int_found = 1
            elif (i=="+") or (i=="-") :
                if len(strs) > 0 and (strs[0] == "+" or strs[0] == "-"):
                    break
                strs = strs + i
            elif not (i== " ") and first_int_found == 1:
                break
            elif not (i == " ") and first_int_found == 0:
                return 0


        if (strs[0]=="-"):
            pow =0
            for i in range(len(strs)-1,0,-1):
                ints = ints + int(strs[i])*10**pow
                pow+=1
            res = -1*ints

        elif (strs[0]=="+"):
            pow =0
            for i in range(len(strs)-1,0,-1):
                ints = ints + int(strs[i])*10**pow
                pow+=1
            res = ints

        else :
            pow = 0
            for i in range(len(strs)-1, -1, -1):
                ints = ints + int(strs[i])*10**pow
                pow += 1
            res = ints

        if res > -1*(2**31) and res < 2**31-1:
            return res
        elif res <= -1*(2**31):
            return -1*(2**31)
        elif res >= 2**31-1 :
            return 2**31-1

    def isPalindrome(self, x):
        strx = str(x)
        flag = True
        if len(strx) > 1:
            for i in range(0, int(len(strx)/2) ):
                if ( strx[i] == strx[len(strx)-i-1] ) and flag:
                    flag = True
                else :
                    flag = False
                    break
            return flag

                # print (strx[i]+" "+strx[len(strx)-i-1])
        else :
            return False

    def maxArea(self, height):
        start=0
        end = len(height)-1
        max_area = 0

    def longestCommonPrefix(self, strs):
        ref = min(strs, key=len)
        for s in strs:
            while not (ref in s) and len(ref)>0:
                ref=ref[:-1]
        print (ref)

    def threeSum(self, nums):
        nums_ref = nums
        fin_list = []
        temp_list = []
        for i in range(0,len(nums)):
            inti = nums.pop(i)
            for j in range(0,len(nums)):
                intj = nums.pop(j)
                for k in range(0,len(nums)):
                    intk = nums.pop(k)
                    if (inti+intj+intk) == 0:
                        temp_list.append(inti)
                        temp_list.append(intj)
                        temp_list.append(intk)
                        match=0
                        if len(fin_list) == 0:
                            fin_list.append(temp_list)
                        else :
                            temp_list.sort()
                            for lis in fin_list:
                                lis.sort()
                                if (temp_list == lis ):#lists  matching then break
                                    match=1
                            if match == 0:
                                fin_list.append(temp_list)
                        temp_list=[]
                    nums.insert(k,intk)
                nums.insert(j, intj)
            nums.insert(i, inti)
        return fin_list

    def letterCombinations(self, digits):
        strarr = []
        keys = {
            '2':['a','b','c'],
            '3':['d', 'e', 'f'],
            '4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'],
            '6':['m', 'n', 'o'],
            '7':['p', 'q', 'r','s'],
            '8':['t', 'u', 'v'],
            '9':['w','x', 'y', 'z']
        }


        for num in digits:
            if len(strarr) == 0:
                for char in keys[num]:
                    strarr.append(char)
            else :
                temp = strarr
                strarr=[]
                for st in temp:
                    for char in keys[num]:
                        strarr.append(  str(st+char)  )

        return strarr





    def twoSum(self, nums, target):
        nums_org=[]
        for num in nums :
            nums_org.append(num)
        nums.sort()
        start = 0
        end = len(nums)-1
        while start < end:
            if nums[start]+nums[end] > target:
                end-=1
            elif nums[start]+nums[end] < target:
                start+=1
            elif nums[start]+nums[end] == target:
                ret = []
                # print(nums)
                # print(nums_org)

                #for retruning the numbers
                ret.append(nums[start])
                ret.append(nums[end])
                # for retruning the index of the numbers uncomment below lines
                # ret.append(nums_org.index(nums[start]))
                # if nums[start] == nums[end] :
                #     ret.append(nums_org.index(nums[end],ret[0]+1))
                # else :
                #     ret.append(nums_org.index(nums[end]))
                print ("2sums for "+str(target)+" "+str(ret) )
                return ret
        return []

    def threeSum(self, nums):
        nums_org = []
        for num in nums:
            nums_org.append(num)
        nums.sort()

        fin_arr = []
        ind=0
        for i in nums:
            if ind == len(nums)-1 and len(fin_arr) == 0:
                print('none found ')
                return []


            ret = Solution().twoSum(nums[ind+1:], -1*i )
            if (len(ret) == 2 ):
                ret.append(i)
                print("nums="+str(ret)+ "for i "+str(i) )
                flag=0

                #appending to fin_arr
                for arr in fin_arr:
                    if arr == ret:
                        flag=1
                        break
                if flag == 0:
                    fin_arr.append(ret)

                temp_ret = ret[0:]

                recheck = nums[ind + 1:]

                recheck.pop(recheck.index(temp_ret[0]))
                ret = Solution().twoSum(recheck, -1*i)
                if (len(ret) == 2):
                    ret.append(i)
                    print("nums=" + str(ret) + "for i " + str(i))
                    flag = 0

                    # appending to fin_arr
                    for arr in fin_arr:
                        if arr == ret:
                            flag = 1
                            break
                    if flag == 0:
                        fin_arr.append(ret)

                recheck.pop(recheck.index(temp_ret[1]))
                ret = Solution().twoSum(recheck, -1 * i)
                if (len(ret) == 2):
                    ret.append(i)
                    print("nums=" + str(ret) + "for i " + str(i))
                    flag = 0

                    # appending to fin_arr
                    for arr in fin_arr:
                        if arr == ret:
                            flag = 1
                            break
                    if flag == 0:
                        fin_arr.append(ret)

                recheck.append(temp_ret[0])
                ret = Solution().twoSum(recheck, -1 * i)
                if (len(ret) == 2):
                    ret.append(i)
                    print("nums=" + str(ret) + "for i " + str(i))
                    flag = 0

                    # appending to fin_arr
                    for arr in fin_arr:
                        if arr == ret:
                            flag = 1
                            break
                    if flag == 0:
                        fin_arr.append(ret)

            ind += 1

        return (fin_arr)


    def minMeetingRooms(self, intervals):
        finlist=[]
        intervals.sort(key= lambda each: each[0] ) # sort as per the start times
        print (intervals)

        finlist.append(intervals[0][1]) # first stack element is inserted

        for i in intervals[1:]:
            ind=0
            for j in finlist[0:len(finlist)-1]:
                if j <= i[0]: #not overlapping
                    finlist[ind] = i[1] #replace the end timer
                    break
                ind+=1
            if finlist[len(finlist)-1] > i[0]: # overlapping
                finlist.append(i[1]) # just append and create new meeting room
            print (finlist)
        return len(finlist)

    def maximumWealth(self, accounts):
        max=0
        for i in accounts:
            s=sum(i)
            if s>max:
                max=s
        return s
        ind=[]
        ind.ind



print(Solution().minMeetingRooms(    [[0,30],[5,10],[15,20]]    ))
# print(Solution().twoSum(    [-1,0,1,2,-1,-4],-1    ))


