# Lecture1
# linked list
# List = [11,3,23,7]
# First difference is that a linked list doesn't have indexes, so remove indexes from list.
# Next thiong is that a list is in a contiguous place in memory. There are all right next to each other in memory with a link list.
# All of the nodes are going to be spread all over the place.
# So also with a link list, we have a variable called head, and it points to the first node in the list.
# Then we're also going to have tail point to the last item, and then each node points to the next until last one is point to none.
# So to emphasize that there are going to be spread out in diffrent places in memory.
# But because one points to the next, to the next, you're able to find all of your nodes without losing any data that is as opposed to a list.
# And list is all in a contigous place in memory, this is why we can have indexes and access those indexes O(1).
# Bc we can map each one of these indexes to a specific address in memory.

# Lecture2
# linked list : BigO
# And first method is going to be to append a new node to the end of the list.
# So in order to do this, we have the last node point to it. (Tail is point to it.) And we add it into the list. This is O(1).
# The reason being, it doesn't matter how many nodes we have in the list, the number of operations to add it to the end is exactly the same.
# But when we are removing from the end of a link list, it's more complicated than that.
# In order to have tail point to that last node, we have to have that pointer there.
# Be set equal to smth else that is pointing at that node.
# These are all just pointers, so we have to set it equal to another pointer and the only thing that points to the seven node is this pointer.
# So in order to get to that node, we have to start at the head iterate through the list until we get to that pointer.
# Then we can set tail equal, to that pointer and that points it at the seven node.
# But bc we had to iterate through the entire list, this is O(n).
# Next, we're going to add an item to the front.
# We need to have that 4 to the 11 node, but still the head is points 11 so we'll have the next pointer from the four be set equal.
# And that we have head point at the new node. And that adds it into the list.
# It doesn't matter how many items we have in the list, it's going to be the same nubmer of operations to add an item on the front of the list.
# So that is O(1)
# Now let's look at removing that 4 node, the first thing we have to do is head points to 11 node.
# We can do that by saying head is equal to head dot next, and that moves that over.
# And then remove that item from the link list. This is going to be O(1), bc it doesn't matter how many items we have in the list.
# Let's say we're going to insert that 4 after 23 node.
# In order to find that node, we have to start at the head and iterate through the list until we get to that 23 node.
# Now we want the 4 to point at that 7 node. So we'll set the pointer from the four equal to that points to there.
# We have that 23 nodse point to the new node.
# But because we had to iterate thrpough the list, this is O(n).
# Let's remove 4, we start at the head and we iterate through the list until we get to the 4.
# We want the 23 to point at that 7 node. So we're going to set the pointer from the 23 equal to the pointer that's going from the 4 to the 7 then remove 4 from the linked list.
# Once again, we had to iterate through the list, it's O(n).
# In linked list, we're going to look at this by index and the 23 is that the index of 2, you have to start at the head and iterate through the indexes until you get to the index of 2.
# This is smth that is different than list.
# Bc in list, you can do this by index of O(1), but with the linked list u both looking it up by the value or looking it up by index is O(n).

# Lecture3
# linked list : Under The Hood.
# What is node ? It is not only the value, it is also the pointer. Both of these together make up the node.
# It's essentially a dictionary. Where a value is a 4 and next is equal to none. (like the node which is points the tail).
{
    "value": 4,
    "next": None
}
# You can use the same syntax to access it. but you'll see it's very similar as we get to the end of this video.
head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value": 4,
                "next": None
            }
        }
    }
}

print(head["next"]["next"]["value"])

# This will only run with a Linked List.
# print(my_linked_list.head.next.next.value)

# Lecture4
# linked list : Constructor


class LinkedList_Old:
    # Bc of self parameters, this is how you tell that this is a method inside of a class instead of a function.
    def __init__(self, value):
        # We're going to use value to create the first node at the time that we initalize the link list.
        self.value = value
        # This constructor is creating the node, it's also going to init the new linked list, but it's going to create the node.

    def append(self, value):
        return
        # The append method is going to create a node and then add that node to the end.

    def prepend(self, value):
        return
        # Prepend is going to create a node and add that node to the beginning inserts going to create a node.

    def insert(self, index, value):
        return
        # Insert is going to create a node and insert node whatever index u want.
# So these methodrs a all create a new node.
# That we don't want to write the code for creating a new node for differemt times. So we r going to do is we're going to create a class that does nothing but create nodes


class Node:
    def __init__(self, value):
        # And when you have variables that apply to a specific instance, remember we use the self keyword, self value and self dot next.
        self.value = value
        self.next = None
    # So when we call on the node class we're going to pass it a value.


class LinkedList_New:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


my_linked_list = LinkedList_New(4)
# And by writing this line, the my_link_list you are creating you have created a head and a tail, it points to the new node, and it assigns the value of 4 to that new node. And gives the linked list a length of 1.
