class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)

        # heapify:
        # fix teh subtree starting at index i so it follows max-heap rules
        def heapify(i, heap_size):
            while True:
                largest = i

                left = 2 * i + 1
                right = 2 * i + 2
                
                # check left child
                if left < heap_size and nums[left] > nums[largest]:
                    largest = left
                
                # check right child
                if right < heap_size and nums[right] > nums[largest]:
                    largest = right

                # if parent is already the largest, heap is valid
                if largest == i:
                    break

                # swap parent with the larger child
                nums[i], nums[largest] = nums[largest], nums[i]

                # continue checking downward from where the old parent moved
                i = largest

        # 1. build  max heap
        # heapify all parent nodes from the bottom upward
        # last parent is n // 2 - 1
        for i in range(n // 2 - 1, -1, -1):
            heapify(i, n)

        # 2. repeatedly move the largest value to the end
        for end in range(n - 1, 0, -1):
            # root is the largest value
            nums[0], nums[end] = nums[end], nums[0]

            # end is now sorted, so exclude it from the heap
            heapify(0, end)
        return nums