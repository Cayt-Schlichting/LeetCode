# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Start adding by first entry, make sure to carry, if none in a node, make it a zero
        ans = ListNode()
        cur = ans
        #initialize carry (for carrying the 1)
        carry = 0
        #loop while listnodes exist
        while l1 or l2:
            #get the value at that node, else 0, then add
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            n_sum = n1 + n2 + carry
            
            #Digit for this node is the remainder when divided by 10 (only gets last digit)
            val = n_sum % 10
            #set carry as how many times 10 goes into the sum 
            carry = n_sum // 10
            
            #set the next listnode
            #NOTE, for our first loop, this is actually setting the second node, since our 
            # first defaults to Zero per the class specifications
            cur.next = ListNode(val)
            #update pointers - cur is now the .next of the last loop's node (aka the latest ListNode)
            cur = cur.next
            #get next node of listnodes 
            #last node .next is None, but need to be explicit in case numbers are quite different
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        #If carry after the last loop is not 0, then we want to add it as a final node
        if carry != 0: cur.next = ListNode(carry)
        
        #return the ans.next - since our first node was actually zero
        return ans.next 
        