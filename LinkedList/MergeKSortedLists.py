"""
LeetCode 21: Merge Two Sorted Lists
LeetCode 23: Merge k Sorted Lists

FAANG Patterns:
1. Sentinel Node Two-Pointer Merge (O(N), O(1) space)
2. Bottom-Up Divide and Conquer Pairwise Merging (O(N log k), O(1) space)
3. Priority Queue / Min-Heap (O(N log k), O(k) space)
"""

from typing import Optional, List
import heapq

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    # Required for heapq comparisons if values match
    def __lt__(self, other: 'ListNode') -> bool:
        return self.val < other.val

    @staticmethod
    def from_list(values: List[int]) -> Optional['ListNode']:
        dummy = ListNode(0)
        curr = dummy
        for v in values:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next

    def to_list(self) -> List[int]:
        res = []
        curr = self
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res


def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    LeetCode 21: Merge 2 sorted lists in O(N) time and O(1) space.
    """
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    curr.next = l1 if l1 else l2
    return dummy.next


def merge_k_lists_divide_and_conquer(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    LeetCode 23: Merge k sorted lists using Bottom-Up Divide and Conquer.
    Time: O(N log k) where N is total nodes across all lists.
    Space: O(1) auxiliary space (zero heap allocations!).
    """
    if not lists:
        return None

    interval = 1
    amount = len(lists)
    while interval < amount:
        for i in range(0, amount - interval, interval * 2):
            lists[i] = merge_two_lists(lists[i], lists[i + interval])
        interval *= 2

    return lists[0]


def merge_k_lists_heap(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    LeetCode 23: Merge k sorted lists using a Min-Heap.
    Time: O(N log k), Space: O(k)
    """
    heap = []
    for node in lists:
        if node:
            heapq.heappush(heap, node)

    dummy = ListNode(0)
    curr = dummy

    while heap:
        smallest = heapq.heappop(heap)
        curr.next = smallest
        curr = curr.next
        if smallest.next:
            heapq.heappush(heap, smallest.next)

    return dummy.next


if __name__ == "__main__":
    # Test LC 21
    l1 = ListNode.from_list([1, 2, 4])
    l2 = ListNode.from_list([1, 3, 4])
    merged2 = merge_two_lists(l1, l2)
    print("Merged 2 lists:", merged2.to_list())
    assert merged2.to_list() == [1, 1, 2, 3, 4, 4]

    # Test LC 23 Divide & Conquer
    k_lists_1 = [
        ListNode.from_list([1, 4, 5]),
        ListNode.from_list([1, 3, 4]),
        ListNode.from_list([2, 6])
    ]
    merged_k1 = merge_k_lists_divide_and_conquer(k_lists_1)
    print("Merged k lists (D&C):", merged_k1.to_list())
    assert merged_k1.to_list() == [1, 1, 2, 3, 4, 4, 5, 6]

    # Test LC 23 Min-Heap
    k_lists_2 = [
        ListNode.from_list([1, 4, 5]),
        ListNode.from_list([1, 3, 4]),
        ListNode.from_list([2, 6])
    ]
    merged_k2 = merge_k_lists_heap(k_lists_2)
    print("Merged k lists (Heap):", merged_k2.to_list())
    assert merged_k2.to_list() == [1, 1, 2, 3, 4, 4, 5, 6]
    print("All tests passed successfully!")
