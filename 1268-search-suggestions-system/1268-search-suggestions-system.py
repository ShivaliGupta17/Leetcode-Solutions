class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result=[]
        for i in range(len(searchWord)):
            l=[]
            count=0
            for word in products:
                if searchWord[:i+1]==word[:i+1]:
                    l.append(word)
                    count+=1
                if count==3:
                    break
            result.append(l)
        return result
        