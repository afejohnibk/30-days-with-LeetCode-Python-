"""
    Assuming head = [1,2,3,4,5]
    Since this is a linked list and not just a regular list
    the elements are 1 > 2 > 3 > 4 > 5 the arrows show that they are linked
    So unlike array we are not going to use pointers or indexing
    Since this is not leetcode but my own code, I had to create a linked list function.
    One that creates and prints a linked list :)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values


values = [1, 2, 3, 4, 5]
head = create_linked_list(values)


def reverseLL(head: ListNode) -> ListNode:
    new_list = None
    current = head
    while current:
        nextNode = current.next
        current.next = new_list
        new_list = current
        current = nextNode

    return new_list


reversed_head = reverseLL(head)
print(print_linked_list(reversed_head))
