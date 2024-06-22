class FreqStack:

    def __init__(self):
        # need to have the one with group of freq to the num
        # since we remove the maxFreq, it can always find a smaller freqency
        # as we build it up from base
        # time: O(1)
        # space:O(N)
        self.counter = {}
        self.freqGroup = {}
        self.maxFreq = 0
        # will time out
        # # counter for the frequency to determine the most frequent int to pop
        # # stack to keep record of the top freqeunt int until the current point
        # # update counter and stack for push and pop
        # # int : freqCnt
        # self.counter = {} 
        # # stack of the top freq
        # self.topNum = 0
        # self.stackNum = []


# method brute force
    # push time:O(1) get 2 hash of freq and push it to the stack
    # space: O(2N):O(N) hash table and array
    def push(self, val: int) -> None:
        if val not in self.counter.keys():
            self.counter[val] = 0
        self.counter[val] += 1
        self.maxFreq = max(self.maxFreq, self.counter[val])
        if self.counter[val] not in self.freqGroup.keys():
            self.freqGroup[self.counter[val]] = []
        self.freqGroup[self.counter[val]].append(val)

        # if len(self.stackNum) == 0:
        #      self.topNum = val
        # else:
        #     # compare the freq of val pushed with latest top
        #     curTop = self.topNum
        #     if self.counter[val]>=self.counter[curTop]:
        #         self.topNum = val
        # self.stackNum.append(val)

    # get the remove idx: O(N) + array trucation takes O(N)
    # need to update the top :O(2N) access the hash and the numbers
    # overall time: O(N)
    def pop(self) -> int:
        curTop = self.freqGroup[self.maxFreq][-1]
        self.counter[curTop] -= 1
        self.freqGroup[self.maxFreq].pop()
        if len(self.freqGroup[self.maxFreq])==0:
            self.maxFreq -= 1
        return curTop
        # curTop = self.topNum
        # self.counter[curTop] -= 1
        # # recalculate the top
        # removeIdx = len(self.stackNum)-1
        # # print("pop")
        # # print(self.stackNum)
        # while removeIdx>=0 and self.stackNum[removeIdx]!= curTop:
        #     removeIdx -= 1
        
        # self.stackNum = self.stackNum[:removeIdx]+self.stackNum[removeIdx+1:]
        # # print(self.stackNum)
        # if len(self.stackNum) > 0:
        #     nextTop = self.stackNum[-1]
        #     for i in range(len(self.stackNum)-1, -1, -1):
        #         if self.counter[nextTop]<self.counter[self.stackNum[i]]:
        #             nextTop = self.stackNum[i]
        #     self.topNum = nextTop
        # # print(nextTop)
        # return curTop

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()