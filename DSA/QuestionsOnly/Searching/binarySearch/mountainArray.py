class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        self.array = arr

        ans = self.findPeak()
        return ans
    

    def findPeak(self):
        start = 0
        end = len(self.array)

        while start < end:
            mid = start + (end-start)//2

            if self.array[mid] < self.array[mid+1]:
                start = mid+1
            else:
                end = mid

        return self.array[start]
    

        
    
obj = Solution()
obj.peakIndexInMountainArray([0,10,5,2])

    


        