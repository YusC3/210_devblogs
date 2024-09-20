from typing import List
from typing import overload
import random as rnd 

class Solutions:
    # Modularation to call code without passing in values
    def __quickSort(self, arr:List[int]):
        start = 0
        end = len(arr) - 1
        return self.__runQuickSort(arr, start, end)
    
    # Code based on NeetCode template. This still didn't work...
    def __runQuickSort(self, arr:List[int], start:int, end:int):
        if end - start <= 1:
            return arr
        
        pivot_val = arr[end]
        left = start

        for i in range(start, end):
            if arr[i] < pivot_val:
                temp = arr[left]
                arr[left] = arr[i]
                arr[i] = temp
                left += 1

        arr[end] = arr[left]
        arr[left] = pivot_val
        self.__runQuickSort(arr, start, i - 1)
        self.__runQuickSort(arr, i + 1, end)
        return arr
    
    def __generateRandomIntArr(self): 
        size = rnd.randint(1, 20)
        int_arr = []

        for i in range(size):
            int_arr.append(rnd.randint(0,200))
        
        return int_arr

    def testQuickSort(self):
        int_arr = self.__generateRandomIntArr()
        print(f"Unsorted: {int_arr}")
        self.__quickSort(int_arr)
        print(f"Sorted: {int_arr}")

def main():
    mySolutions = Solutions()
    mySolutions.testQuickSort()

if __name__ == "__main__":
    main()