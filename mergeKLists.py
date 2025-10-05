class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Min heap
        heap = []
        
        # Push initial heads of all linked lists
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))  
                # (value, index, node) -> index to avoid comparison issue

        dummy = ListNode(0)
        current = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
