class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        # define set of all unique email address
        unique = set()
        
        # iterate through list of emails
        for email in emails:        
            # clean email address
            clean_email = self.clean(email)
            # add to set of all unique email address
            unique.add(clean_email)
        
        # return the number of different addresses that actually receive mails
        return len(unique)
    
    def clean(self, email: str) -> str:
        # split email into local name and domain name
        split_email = email.split('@')
        local = split_email[0]
        domain = split_email[1]
        
        # clean local name
        # remove periods
        removed_periods = ''.join([c for c in local if c!='.'])
        # ignore everything after first plus sign
        n = len(removed_periods)
        pointer = 0
        while pointer < n:
            if removed_periods[pointer] == '+':
                break
            pointer += 1
        local = removed_periods[:pointer]
        
        # combine local and domain name
        res = local + '&' + domain
        
        # return clean email address
        return res