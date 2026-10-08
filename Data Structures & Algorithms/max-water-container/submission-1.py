class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        #area: height of smaller bar x distance between smaller and larger = height x width
        #smallest of height of smaller / larger bar is: min(heigths[i])
        #distance between smaller and larger: distance between two pointers / indices

        #find 2 maximums, and distance between them, add area to area_arr, next ptr is one smaller, loop
        '''
        sorted_heights = sorted(heights)
        heigher1 = sorted_heights[len(sorted_heights) - 1]                     #[1,7,2,5,4,7,3,5]
        second_higher = sorted_heights[len(sorted_heights) - 2]                           #[1,2,3,4,5,6,7,7]
        distance = heights[heigher1] - heights[second_higher]
        area = distance * second_higher
        heights_arr = []
        while len(heights_arr) < len(heights):
            heights_arr.append(area)
            second_higher -=1
        return max(heights_arr)
        '''

        '''
        left = 0
        right = 1
        arr_area = []
        area = 0
        for num in heights:
            while right < len(heights):
                area = min(heights[left], heights[right]) * (right - left)
                arr_area.append(area)
                right +=1
        print(arr_area)
        return max(arr_area)
        '''


        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            current = min(heights[left], heights[right]) * (right - left)
            max_area = max(current,max_area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area
            