class Solution(object):
    def findin(self,s,start,end):
        # for sub_len in range(len(s)-1,0,-1):#size of sub str
        for sub_len in range(start,end,-1):#size of sub str
            #print (sub_len)
            for i in range(0,len(s)-sub_len):#position of sub str
                testsub = s[i:i+sub_len]
                find = s.find(testsub,s.find(testsub,0,len(s))+1,len(s))
                #print(testsub, find)
                if find != -1:
                    return testsub

        return ""
        """
        :type s: str
        :rtype: str
        """

    def longestDupSubstring(self, s):
        longest_len = 0
        if len(s) > 10:
            res = self.findin(s,int(len(s)/2)-1, 0)
            if res == "":
                return self.findin(s,len(s)-1, int(len(s)/2)-1)

        else:
            return self.findin(s, len(s) - 1, 0)

print ("answer:" +Solution().longestDupSubstring("jvgegcvhehzqdmlzaoqblsawjpdjepqvbsrqmzcqwreewdtrnxlxshbevyorswlhdcjyzvibsmvwgdwmdqmwvyciuqwtlnbtgvkufeolzpzrbfoztyceeqyywnzwecvpetzjdnfmpykbonrjltnbbtxbtqwlbtrskceoyupjidhoxqmysnjgaprphmygbfqbbgamgyrgudqxwakkwoanxcuehdcxeaiphhdfrloqbcayiewxjpogvssnwsycrutxvbuaegycgvugmygumzsbnusdqmejuicnmsfkhyatexynibiymmtvniyntjyluiqspoazlvoxbljmohehunujwxihohdsvkrhdmhiiwmdumduypvejlkpzqceytefuxihesnwiyvbddploxijffrxmwlqenrfjiobfvoxtnsiigxvmuhbohreykexcgjmnakenfrsjpxsyrvdsekhuhrgtqiyrsfhfntotxrgqqqoztpqyiyldcciskddtfobgwwsdfgmabxwopysavjvoqrkzbenespibdjkfmxevwzqevjudskxxvdinfvrmqgyxcjhxqevcablajybbtkxyorqwsfbykvhnoixkttjxtuinecsyforvouddwhzpqmttojjekthgbhihutqoisdrdbejnhxfgawtttjhqtncnbuxpocuepzhxgrsfkdtbrpfsljxpwhhqcjjwblzdzscdbbvugphijyzeoctjzydfvsniuigepssdcofrrkfuhejgeorjrmremudqxkclicyhiwqhwnwhlxjseuandmvnithfudpbpjkdeieyuywwqosodytfahsrqmpoalgaszbhhrlvtjwjigjdcpbnveapgdpsjvqwydussnpgwydhuqibosxbgyhaiilxhabftgjxvocoajqqfgrtkkmtfevwmeerihwmmql"))