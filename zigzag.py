class Solution(object):
    def convert(self, s, numRows):
        rows = range(numRows)
        ans = []
        up=False
        down=True
        i=0
        j=4
        for ro in rows:
            ans.append([])
        for c in range(len(s)):
            if down and i < rows:
                ans[i].append(c)
                i+=1
                if (i==rows):
                    down=False
                    up=True
                    i-=2
            elif up and i >= 0:
                ans[i].append(c)
                i-=1
                if(i<0):
                    down = True
                    up = False
                    i+=2
        print(ans)
        return ans
