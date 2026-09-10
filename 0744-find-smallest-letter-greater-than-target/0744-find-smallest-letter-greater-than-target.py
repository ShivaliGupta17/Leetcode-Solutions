class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        mini=ord('z')
        c=mini
        for i in range(len(letters)):
            if ord(target)<ord(letters[i]):
                mini=min(ord(chr(mini)),ord(letters[i]))
        if (mini==c and chr(mini) not in letters) or target=='z':
            return letters[0]
        else:
            return chr(mini)
                
        