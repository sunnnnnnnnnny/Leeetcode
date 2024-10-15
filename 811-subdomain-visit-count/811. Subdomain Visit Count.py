class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # break down the domain as key and make accumulation
        # avg domain level is M
        # time:O(N*M) O(N*M)
        domainCnt = {}
        for cntDomain in cpdomains:
            cntStr, domain = cntDomain.split(' ')
            idx = 0
            cnt = int(cntStr)
            while idx<len(domain):
                key = domain[idx:]
                if key not in domainCnt.keys():
                    domainCnt[key] = 0
                domainCnt[key] += cnt
                while idx<len(domain):
                    if domain[idx] == '.':
                        idx+= 1
                        break
                    idx+=1
        ret = []
        for k ,freq in domainCnt.items():
            cntDoPair = str(freq)+" "+k
            ret.append(cntDoPair)
        return ret