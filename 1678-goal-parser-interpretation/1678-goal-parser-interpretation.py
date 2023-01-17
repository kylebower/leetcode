class Solution:
    def interpret(self, command: str) -> str:
        # define output string
        result = ""
        
        while command:            
            # parse input string
            if command[0] == "G":
                # update output string
                result += "G"
                command = command[1:]
            elif command[0:2] == "()":
                result += "o"
                command = command[2:]           
            else:
                result += "al"
                command = command[4:]
        
        # return output string
        return result
