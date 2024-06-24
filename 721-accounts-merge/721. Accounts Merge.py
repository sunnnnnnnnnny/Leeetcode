class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # union find need to build the basem which is link to it's original group
        # once we find the common amaong it, then we add it to the group(merge)
        # we always merge it with the smaller size to biger size
        # N accounts, M is the max len of an account
        # time: O(N*M log(NM)
        # space: O(NM)
        baseSize = {}
        baseRep = {}
        # time: build DSU O(N)
        def constructDSU(groupSize):
            for i in range(groupSize):
                baseSize[i] = 1
                baseRep[i] = i
        # time:O(alpha(N))
        def findRepBase(groupI):
            if baseRep[groupI] == groupI:
                return groupI
            baseRep[groupI] = findRepBase(baseRep[groupI])
            return baseRep[groupI]
        # time:O(alpha(N))
        def unionBySize(groupA, groupB):
            repBaseA = findRepBase(groupA)
            repBaseB = findRepBase(groupB)
            if repBaseA == repBaseB:
                return 
            if baseSize[repBaseA]>=baseSize[repBaseB]:
                baseRep[repBaseB] = repBaseA
                baseSize[repBaseA] += baseSize[repBaseB]
            else:
                baseRep[repBaseA] = repBaseB
                baseSize[repBaseB] += baseSize[repBaseA]
        
        totalGroup = len(accounts)
        constructDSU(totalGroup)
        appearedEmails = {}
        # time: O(N*M)
        for i in range(totalGroup):
            # traverse the emails
            for j in range(1, len(accounts[i])):
                if accounts[i][j] in appearedEmails.keys():
                    # merge group i with group of appearedEmails
                    unionBySize(i, appearedEmails[accounts[i][j]])
                else:
                    appearedEmails[accounts[i][j]] = i
        groupToEmails = {}
        # time:O(M)
        for email in appearedEmails.keys():
            # print(email)
            groupIdx = findRepBase(appearedEmails[email])
            if groupIdx not in groupToEmails.keys():
                groupToEmails[groupIdx] = []
            groupToEmails[groupIdx].append(email)
        # sort the emails, takes O(n*M log(NM)) if all emails belong to the same account
        ans = []
        for groupI in groupToEmails.keys():
            # print(groupToEmails[groupI])
            # groupList = groupToEmails[groupI].sort()
            # l = [accounts[groupI][0]]+groupList
            # ans.append([accounts[groupI][0]])
            groupToEmails[groupI].sort()
            ans.append([accounts[groupI][0]]+groupToEmails[groupI])
        return ans


        # making each email as the key and link it to the account idex
        # saying the total distinct email is M and accouts is N
        # space: O(M) for dict time: O(N*M)? should be longer
        