class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # modify the email into key without the . and +
        uniEmail = set()
        def modUni(email):
            ret = ""
            sep = email.split('@')
            if len(sep) == 2:
                loc, dom = sep
                if loc.find('+')!=-1:
                    loc = loc[:loc.find('+')]
                loc = loc.replace('.','')
                ret = loc+"@"+dom
            return ret

        for e in emails:
            uniE = modUni(e)
            if len(uniE)>0:
                uniEmail.add(uniE)
        return len(uniEmail)
