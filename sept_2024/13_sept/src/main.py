# Leet code submissions

class Solutions:
    # TO DO: Optimize
    def longestPalindrome(self, s: str) -> int:
        """ 
        409. Longest Palindrome
        """
        max_size = 0

        if len(s) == 1:
            max_size = 1
        else:
            char_dict = {}

            for char in s:
                if char in char_dict:
                    char_dict[char] += 1
                else:
                    char_dict[char] = 1
            
            has_odd = False

            for key, value in char_dict.items():
                print(f"{key}:, {value}")
                if value % 2 == 0:
                    max_size += value
                else:
                    has_odd = True
                    max_size += value - 1

            max_size += 1 if has_odd else 0
        
        return max_size
    
    # TO DO: Optimize
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(g) == 1 and len(s) == 1:
            if g[0] == s[0]:
                return 1
            else:
                return 0
        elif len(s) == 0:
            return 0
        
        i = 0 
        j = 0
        happy = 0

        g.sort()
        s.sort()

        while  i < len(g):
            child = g[i]
            is_happy = False

            while is_happy == False and j < len(s):
                cookie = s[j]

                if cookie >= child:
                    happy += 1
                    is_happy = True

                j += 1

            i += 1
            
        return happy
    
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        i = 0

        while i < len(flowerbed) and n > 0:
            if flowerbed[i] == 0: 
                if ((i - 1 < 0 or flowerbed[i - 1] == 0)
                    and  (i + 1 >= len(flowerbed) or flowerbed[i + 1] == 0)):
                        flowerbed[i] = 1
                        n -= 1
            
            if flowerbed[i] == 1:
                i += 2
            else:
                i += 1
        
        print(n)

        return True if n == 0 else False
    
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        i = 0
        result = 0

        while i < len(nums):
            result += nums[i]
            i += 2
        
        return result
        
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        if nums[0] == 0 and len(nums) > 1:
            return False
        
        i = current = 0

        while i < len(nums) - 1:
            if nums[i] > current:
                current = nums[i]
            
            if i < len(nums) - 1 and current == 0:
                return False
            
            current -= 1
            i += 1 
        
        return i == len(nums) - 1



