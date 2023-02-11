class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # create dict
        d = {}
        i = 0
        for c in key:
            if c not in d and c != " ":
                d[c] = chr(97 + i)
                i += 1
        
        # remove duplicates from key
        key = "".join(list(d.keys()))
        
        # decode message
        plain_text = ""
        for c in message:
            if c == " ":
                plain_text += " "
            else:
                plain_text += d[c]
        
        # return plain text
        return plain_text
