class Solution:
    def numberToWords(self, num: int) -> str:
        # list out the digits and it's english 
        # convert it into englist
        # time:O(N) space:O(N)
        ten2Word = {20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 
        60:"Sixty", 70:"Seventy", 80:"Eighty", 90:"Ninety"}
        elf2Word = {10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 
        16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen", 20:"Twenty"}
        one2Word = {0:"Zero", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}
        def int2Eng(now):
            nonlocal one2Word, elf2Word, ten2Word
            digit = 1
            restNow= now
            while restNow>0:
                digit*=10
                restNow = restNow//10
            digit = digit//10
            midWord = ""
            larger = smaller = 0
            if digit>= 1000000000000:
                midWord = "Trillion"
                larger = now//1000000000000
                smaller += now%1000000000000
            elif digit>= 1000000000:
                midWord = "Billion"
                larger = now//1000000000
                smaller += now%1000000000
            elif digit >= 1000000:
                midWord = "Million"
                larger = now//1000000
                smaller += now%1000000
            elif digit >= 1000:
                midWord = "Thousand"
                larger = now//1000
                smaller += now%1000
            elif digit >= 100:
                midWord = "Hundred"
                larger = now//100
                smaller += now%100
            # print(digit, midWord, now, larger, smaller)
            if midWord != "":
                lWord = int2Eng(larger)
                if smaller == 0:
                    return lWord+" "+midWord
                sWord = int2Eng(smaller)
                return lWord+" "+midWord+" "+sWord
            if now<10:
                return one2Word[now]
            elif now>=10 and now<20:
                return elf2Word[now]
            # expect now>=20 and now<100
            lowDig = now%10
            lWord = ten2Word[now-lowDig]
            if lowDig == 0:
                return lWord
            
            sWord = int2Eng(lowDig)
            return lWord+" "+sWord
        return int2Eng(num)
            


