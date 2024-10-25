class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        # start to inumerate the numbers, and add until we have n numbers
        # also need to convert the ip to CIDR
        # make sure the 255 to bits
        def ip2nArr(ip):
            blocks = list(map(int,ip.split('.')))
            n = (blocks[0]<<24)+(blocks[1]<<16)+(blocks[2]<<8)+(blocks[3])
            return n
        def nArr2ip(n):
            return ".".join([str(n>>24&255), str(n>>16&255), str(n>>8&255), str(n&255)])
    # would return the index i of the first '1' starting from the right. 
    # The index of the first 1 helps to define how many ips have the same (32-i)part. 
        def iLowBit(x):
            for i in range(32):
                if(x&(1<<i)):
                    return i
            return 32
        
        def lowBit(x):
            y  = iLowBit(x)
            # getting the lowest Bit as we need to calculate how many i can be included
            # thus we need to shift 1 to the left
            # print("lowBit ", x, y)
            return 1<<y

        num = ip2nArr(ip)
        ret = []
        while n>0:
            lowB = lowBit(num)
            # print(num, lowB)
            while lowB>n:
                lowB = lowB//2
            n = n-lowB
            usedBit = iLowBit(lowB)
            # print("usedBit ", num, lowB, usedBit)
            ret.append(nArr2ip(num) +"/"+ str(32-iLowBit(lowB)))
            num = num+lowB
        return ret