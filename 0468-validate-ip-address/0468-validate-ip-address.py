class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if self.isIPv4(queryIP):
            return "IPv4"
        elif self.isIPv6(queryIP):
            return "IPv6"
        else:
            return "Neither"
    
    def isIPv4(self, query: str) -> bool:
        # return True if query is a valid IPv4, else False
        query_split = query.split('.')
        if len(query_split) != 4:
            return False
        for q in query_split:
            if len(q) < 1 or len(q) > 3:
                return False
            if q[0] == '0' and len(q) != 1:
                return False            
            if not all(p in string.digits for p in q):
                return False
            if int(q) < 0 or int(q) > 255:
                return False
        return True

    def isIPv6(self, query: str) -> bool:
        # return True if query is a valid IPv6, else False
        query_split = query.split(':')
        if len(query_split) != 8:
            return False
        for q in query_split:
            if len(q) < 1 or len(q) > 4:
                return False
            if not all(p in string.hexdigits for p in q):
                return False
        return True