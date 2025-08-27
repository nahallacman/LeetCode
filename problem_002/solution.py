# Extra header to ensure that tests can run individually and as a suite
#  -------------------------------------------------------------------
import sys
from pathlib import Path
# Add the project root folder to the Python path
sys.path.append(str(Path(__file__).resolve().parents[1]))
#  -------------------------------------------------------------------

# Now you can import your wrapper
from test_runner.wrapper import run_tests

from typing import Optional

# Definition for doubly-linked list.
class __ListNode:
    def __init__(self, val=0, next=None, last=None):
        self.val = val
        self.next = next
        self.previous = last

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, last=None):
        self.val = val
        self.next = next

class LinkedList:
    head = None
    tail = None
  
    def __init__(self, input):
        first = True
        self.head = None
        self.tail = None
        for i in input:
            thisNode = ListNode(i)
            if first:
                first = False
                self.head = thisNode
                self.tail = self.head
            else:
                self.tail.next = thisNode
                thisNode.previous = self.tail
                #move the last pointer on to the next for the next iteration
                self.tail = thisNode
    
    def len(self):
        count = 1
        # If the linked list is empty
        if(not self.head):
            return 0
        # Else, we have at least one node in the list
        iter = self.head
        # Move the iterator forward until the next pointer is None (null)
        while iter.next:
            count += 1
            iter = iter.next

        # Count should now be the length of the linked list since we started at 1
        return count

class Solution:
    # def addTwoNumbersLinkedList(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    #     list1 = LinkedList(l1).head
    #     list2 = LinkedList(l2).head

    #     index_end = len(list1) - 1
    #     index = index_end
    #     retval = []
    #     for x in range(0, index_end+1):
    #         retval.append(0)

    #     while index >= 0:
    #         result = list1[index] + list2[index]
    #         if result > 9:
    #             retval[index+1] += 1
    #             result = result - 10
    #         retval[index] += result
    #         index -= 1
    #     return retval

    # def addTwoNumbersNoSizeChecking(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    #     index_end = len(l1) - 1
    #     index = index_end
    #     retval = []
    #     for x in range(0, index_end+1):
    #         retval.append(0)

    #     while index >= 0:
    #         result = l1[index] + l2[index]
    #         if result > 9:
    #             retval[index+1] += 1
    #             result = result - 10
    #         retval[index] += result
    #         index -= 1
    #     return retval
    
    # # So this works but the len() doen't work on the regular structure.
    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    #     current = 0
    #     overflow = 0
    #     retval = []
    #     max_len = max(len(l1), len(l2))

    #     for x in range(0, max_len):
    #         l1_current = 0
    #         l2_current = 0
    #         try:
    #             l1_current = l1[x]
    #         except Exception as E:
    #             # Debug printing only
    #             print(f"exception: {E}")
    #         try:
    #             l2_current = l2[x]
    #         except Exception as E:
    #             # Debug printing only
    #             print(f"exception: {E}")
    #         current = l1_current + l2_current + overflow
    #         if current >= 10:
    #             overflow = 1
    #             current = current - 10
    #         else:
    #             overflow = 0
            
    #         retval.append(current)

    #     if overflow == 1:
    #         retval.append(overflow)

    #     return retval
    
    # # So this works but the len() doen't work on the regular structure.
    # def __addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    #     current = 0
    #     overflow = 0
    #     retval = []
    #     max_len = max(len(l1), len(l2))

    #     for x in range(0, max_len):
    #         l1_current = 0
    #         l2_current = 0
    #         try:
    #             l1_current = l1[x]
    #         except Exception as E:
    #             # Debug printing only
    #             print(f"exception: {E}")
    #         try:
    #             l2_current = l2[x]
    #         except Exception as E:
    #             # Debug printing only
    #             print(f"exception: {E}")
    #         current = l1_current + l2_current + overflow
    #         if current >= 10:
    #             overflow = 1
    #             current = current - 10
    #         else:
    #             overflow = 0
            
    #         retval.append(current)

    #     if overflow == 1:
    #         retval.append(overflow)

    #     return retval
    
    def addTwoNumbersAndMakeLinkedList(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ll_head_1 = LinkedList(l1).head
        
        l1_iter = ll_head_1
        while l1_iter:
            print(f"test l1: {l1_iter.val}")
            l1_iter = l1_iter.next
        ll_head_2 = LinkedList(l2).head

        l2_iter = ll_head_2
        while l2_iter:
            print(f"test l2: {l2_iter.val}")
            l2_iter = l2_iter.next

        return_head = self.addTwoNumbers(ll_head_1, ll_head_2)
        return_iter = return_head
        retval = []
        while return_iter:
            retval.append(return_iter.val)
            return_iter = return_iter.next

        return retval
    
    # So this works but the len() doen't work on the regular structure.
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = 0
        overflow = 0
        ret_iter = None
        retval = None

        # Needs to only try to move on when there are still items in the list... 
        while l1 or l2:
            l1_current = 0
            l2_current = 0
            try:
                l1_current = l1.val
                l1 = l1.next
            except Exception as E:
                # Debug printing only
                print(f"exception: {E}")
            try:
                l2_current = l2.val
                l2 = l2.next
            except Exception as E:
                # Debug printing only
                print(f"exception: {E}")
            current = l1_current + l2_current + overflow
            if current >= 10:
                overflow = 1
                current = current - 10
            else:
                overflow = 0
            
            next = ListNode(current)
            if(not ret_iter):
                retval = next
                ret_iter = next
            else:
                ret_iter.next = next
                ret_iter = next

        if overflow == 1:
            next = ListNode(overflow)
            ret_iter.next = next
            ret_iter = next

        return retval



if __name__ == "__main__":
    # Get the directory where this solution.py script lives
    script_dir = Path(__file__).parent
    
    # Join the script's directory with the JSON filename to create a full path
    # Make sure your file is actually named "test_inputs.json"!
    test_file_path = script_dir / "test_inputs.json"
    
    run_tests(Solution, test_file_path)