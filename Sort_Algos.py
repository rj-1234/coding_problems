"""
Links - 
1. https://codeburst.io/algorithms-i-searching-and-sorting-algorithms-56497dbaef20
2. https://betterexplained.com/articles/sorting-algorithms/
3. https://www.youtube.com/watch?list=UUIqiLefbVHsOAXDAxQJH7Xw&time_continue=15&v=ywWBy6J5gz8
4. https://www.toptal.com/developers/sorting-algorithms ******
"""

class Sorting:
    def __init__(self, alist):
        self.alist = alist
        

    def bubbleSort(self, alist):
        """
        swap_flag = True
        while swap_flag:
            swap_flag = False
            for i in range(len(alist)-1):
                if alist[i] > alist[i+1]:
                    alist[i], alist[i+1] = alist[i+1], alist[i]
                    swap_flag = True
        """

        for i in range(len(alist)):
            for j in range(0, len(alist)-i-1):
                if alist[j] > alist[j+1]:
                    alist[j], alist[j+1] = alist[j+1], alist[j]

        return alist

    def insertionSort(self, alist):
        for i in range(1, len(alist)):
            key = alist[i]

            j = i - 1

            while j >= 0 and key < alist[j]:
                alist[j+1] = alist[j]
                j -= 1
            alist[j+1] = key

        return alist

    def selectionSort(self, alist):
        for i in range(len(alist)):
            key = alist[i]
            key_idx = i

            for j in range(i+1, len(alist)):
                if key > alist[j]:
                    key = alist[j]
                    key_idx = j
            alist[key_idx], alist[i] = alist[i], alist[key_idx]

        return alist

    def mergeSort(self, alist):
        if len(alist) < 2:
            return alist
        mid = len(alist)/2
        left = self.mergeSort(alist[:mid])
        right = self.mergeSort(alist[mid:])

        return self._merge(left, right)

    def _merge(self, left, right):
        final_list = []

        while left and right:
            if left[0] > right[0]:
                final_list.append(right[0])
                del right[0]
            else:
                final_list.append(left[0])
                del left[0]

        while left:
            final_list.append(left[0])
            del left[0]
        
        while right:
            final_list.append(right[0])
            del right[0]

        return final_list


    def quickSort(self, alist):
        if len(alist) < 2:
            return alist
        self._quickSortHelper(alist, 0, len(alist)-1)
        return alist

    def _quickSortHelper(self, alist, first, last):
        if first < last:
            partition = self.doPartition(alist, first, last)

            self._quickSortHelper(alist, first, partition-1)
            self._quickSortHelper(alist, partition+1, last)

        return 

    def doPartition(self, alist, first, last):
        pivot = alist[last]

        left = first
        right = last - 1

        while left <= right:
            while alist[left] < pivot:
                left += 1
            while alist[right] > pivot:
                right -= 1

            if right < left:
                break
            else:
                alist[left], alist[right] = alist[right], alist[left]
        
        alist[left], alist[last] = alist[last], alist[left]
        return left

if __name__ == "__main__":
    testSet = [[], [1], [9, 3], [9,4,7], [9,7,6,5,4,3,2,1], [0,1,2,3,4,5,6,7,8,9]]
    for i in testSet:
        sort = Sorting(i)
        print("Original unsorted list : ", i)
        print("Bubble Sort set "+str(testSet.index(i))+" : ",sort.bubbleSort(i))
        print("Insertion  Sort set "+str(testSet.index(i))+" : ",sort.insertionSort(i))
        print("Selection Sort set "+str(testSet.index(i))+" : ",sort.selectionSort(i))
        print("Merge Sort set "+str(testSet.index(i))+" : ",sort.mergeSort(i))
        print("Quick Sort set "+str(testSet.index(i))+" : ",sort.quickSort(i))
        print("\n\n")