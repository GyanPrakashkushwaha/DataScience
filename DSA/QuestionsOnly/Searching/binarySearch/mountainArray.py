class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:

        start = 0
        end = len(arr)

        while start < end:
            mid = start + (end-start)//2

            if arr[mid] < arr[mid+1]:
                start = mid+1
            else:
                end = mid

        return start
    
        
    
obj = Solution()
print(obj.peakIndexInMountainArray([0,10,5,2]))

    


        