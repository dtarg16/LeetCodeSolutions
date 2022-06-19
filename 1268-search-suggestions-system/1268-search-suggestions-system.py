class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        n = len(products)
        products.sort() 
        ans = []
        beginSearch = 0
        prefix = ""
        for c in searchWord:
            prefix += c
            beginSearch = insertIndex = bisect_left(products, prefix, beginSearch, n)
            suggestProducts = []
            for i in range(insertIndex, min(insertIndex+3, n)):
                if products[i].startswith(prefix):
                    suggestProducts.append(products[i])
            ans.append(suggestProducts)
        return ans