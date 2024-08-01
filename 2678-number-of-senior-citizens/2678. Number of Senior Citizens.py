class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # since it's 15 len, meaning the age isat str[11:13] for the 2
        # time:O(N), space:O(1)
        ret = 0
        for person in details:
            age = int(person[11:13])
            # print(age)
            if age>60:
                ret+=1

        return ret
        