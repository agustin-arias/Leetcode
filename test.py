# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def addTwoNumbers(self, l1, l2):
    	firstList = l1
    	secondList = l2

    	carry = 0
    	output = ListNode()
    	cumulative = output

    	while firstList.next != None and secondList.next != None:
    		cumulative.val = (firstList.val + secondList.val + carry) % 10
    		carry = (firstList.val + secondList.val) // 10

    		print(f"cumulative.val:{cumulative.val}")
    		print(f"firstList.val:{firstList.val}")
    		print(f"secondList.val:{secondList.val}")

    		cumulative.next = ListNode()



    		firstList = firstList.next
    		secondList = secondList.next
    		cumulative = cumulative.next

    	if firstList.next == None:
    		while secondList.next != None:
    			secondList = secondList.next
    			cumulative.next = ListNode(secondList.val)

    	if secondList.next == None:
    		while firstList.next != None:
    			firstList = firstList.next
    			cumulative.next = ListNode(firstList.val)


    	return output

l1 = ListNode(val=9, next=ListNode(val=8, next=ListNode(val=7)))
l2 = ListNode(val=9, next=ListNode(val=8))#, next=ListNode(val=4)))

l3 = Solution().addTwoNumbers(l1, l2)
print(l3.val)
print(l3.next.val)
print(l3.next.next.val)
