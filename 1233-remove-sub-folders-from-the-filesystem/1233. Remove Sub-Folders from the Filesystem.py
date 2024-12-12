class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # build a trie from the main folder, then if any folder is sub folder should be skip
        # method 2: add all folder as key, then each word check from the back to see
        # it the parent folder exists, time;O(N*M) M is the avg folder path
        existFold = set(folder)
        ret = []
        for f in folder:
            prevI = 1
            keep = True
            while prevI<len(f):
                idx = f.find("/", prevI)
                prevI = idx+1
                # no more / appeared
                if idx==-1:
                    break
                # print(f, prevI, idx)
                if idx<len(f):
                    if f[:idx] in existFold:
                        keep = False
                        break
            if keep:
                ret.append(f)
        return ret
                