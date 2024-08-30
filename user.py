def reverse_string(s: str) -> str:
    # Initialize an empty stack
    stack = []
    
    # Push all characters of the string onto the stack
    for char in s:
        stack.append(char)
    
    # Pop characters from the stack and collect them into a new string
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

# Example usage
input_string = "hello"
output_string = reverse_string(input_string)
print(output_string)  # Output: "olleh"





class QueueWithStacks:
    def __init__(self):
        # Initialize two stacks
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int):
        # Push the element onto stack1
        self.stack1.append(x)

    def dequeue(self) -> int:
        # If stack2 is empty, move all elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # If stack2 is still empty, the queue is empty
        if not self.stack2:
            raise IndexError("dequeue from an empty queue")

        # Pop the element from stack2, which is the front of the queue
        return self.stack2.pop()

# Example usage
q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2






class Node:
    def __init__(self, data):
        self.data = data  # Store the data of the node
        self.next = None  # Initialize the next pointer to None


class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list to None

    def append(self, data: int):
        """Appends a new node with the given data to the end of the linked list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty, make the new node the head
            self.head = new_node
        else:
            # Traverse to the end of the list and append the new node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_max(self) -> int:
        """Finds and returns the maximum element in the linked list."""
        if not self.head:  # If the list is empty, raise an exception
            raise ValueError("The linked list is empty")

        # Initialize the max value with the head node's data
        max_value = self.head.data
        current = self.head.next

        # Traverse the list to find the maximum value
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next

        return max_value


# Example usage
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())  # Output: 4
