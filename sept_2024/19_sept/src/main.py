import random as rnd 
from typing import List

class Solutions:
    # LEET CODE
    # 45. Jump Game II - REVIEW (did not work)
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        i = 0
        max_length = 0
        moves = 0

        while i < len(nums):
            curr = nums[i]

            if curr + i >= len(nums) - 1:
                moves += 1
                break
            elif max_length < curr:
                max_length = curr
                moves += 1
            
            max_length -= 1
            i += 1
        
        return moves
    
    # Implementation and testing of Merge Sort (NO LOOKING)
    def __mergeLeftAndRight(self, arr_l:List[int], arr_r:List[int]):
        i = 0
        j = 0

        merged = []

        while i < len(arr_l) and j < len(arr_r):
            if arr_l[i] <= arr_r[j]:
                merged.append(arr_l[i])
                i += 1
            else:
                merged.append(arr_r[j])
                j += 1
        
        if not i == len(arr_l):
            merged.extend(arr_l[i:])
        elif not j == len(arr_r):
            merged.extend(arr_r[j:])

        return merged
    
    def __mergeSort(self, arr: List[int]):
        if len(arr) <= 1:
            return arr

        middle = int(len(arr) / 2)
        left = self.__mergeSort(arr[0:middle])
        right = self.__mergeSort(arr[middle: ])

        sorted = self.__mergeLeftAndRight(left, right)
        return sorted
    
    def runMergeSortTest(self):
        random_size = rnd.randint(1, 20)
        arr = []

        for i in range(random_size):
            arr.append(rnd.randint(0, 200))
        
        sorted_arr = self.__mergeSort(arr)
        
        print(f"This is a random, unsorted list: {arr}")
        print(f"This is a random, sorted list: {sorted_arr}")

def main():
    mySolutions = Solutions()
    mySolutions.runMergeSortTest()

if __name__ == "__main__":
    main()

