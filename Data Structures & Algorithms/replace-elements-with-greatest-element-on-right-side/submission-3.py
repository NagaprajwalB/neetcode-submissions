class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)

        for i in range(n):
            max_n = []
            for j in range(i + 1, n):
                max_n.append(arr[j])

            if max_n:
                arr[i] = max(max_n)

            else:
                arr[i] = -1      

        return arr        