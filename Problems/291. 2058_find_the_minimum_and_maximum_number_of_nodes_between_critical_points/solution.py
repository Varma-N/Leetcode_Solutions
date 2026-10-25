# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        min_dis = float('inf')
        critical_points = []
        res = []
        pos = 1
        prev = head
        current = head.next
        while current.next:
            if prev.val < current.val > current.next.val:
                critical_points.append(pos)
            elif prev.val > current.val < current.next.val:
                critical_points.append(pos)
            pos += 1
            prev = current
            current = current.next

        if len(critical_points) < 2:
            return [-1, -1]
        else:
            for i in range(1, len(critical_points)):
                diff = critical_points[i]-critical_points[i-1]
                min_dis = min(min_dis, diff)
        return [min_dis, critical_points[-1]-critical_points[0]]