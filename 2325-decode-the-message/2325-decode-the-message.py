class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # create dict
        d = {" ": " "}
        i = 0
        for c in key:
            if c not in d:
                d[c] = chr(97 + i)
                i += 1
        
        # decode message
        plain_text = ""
        for c in message:
            plain_text += d[c]
        
        # return plain text
        return plain_text
