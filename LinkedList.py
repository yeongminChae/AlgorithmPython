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

# Lecture5
# linked list : Print List

# In order to look at all of the values in a linkedList, i've created a method called print list.


def print_list(self):
    temp = self.head
    while temp is not None:
        print(temp.value)
        temp = temp.next

# Lecture6
# linked list : Append

# We'll have that last item that was in the list point to be the new node will have tail point to the new node that adds into the list.
# So twp things we did here, last itme and tail pointing to the new node.
# But we do have an edge case for when we don't have any items in the linked list.
# Obviously we can't have the last item and tail point to the new node bc there is no last item.
# In this situation, we r going to have head and tail point to the new node.


def append(self, value):
    # The value that we pass the append method, and then the node class will create our node.
    new_node = Node(value)
    if self.head is None:  # We have to determine is the list empty?
        self.head = new_node
        self.tail = new_node
        # Then, head and tail point to the new node.
    else:  # the situation where there are items already existing in the link list.
        self.tail.next = new_node
        self.tail = new_node
    # The only thing left todo is to increase the length of the link list by one.
    self.length += 1
    # optional : in few cases, we'll going to write another method that requires boolean value.
    return True

# Lecture7
# linked list : Pop Intro

# In the normal linkedlist, we are going to remove that last item, and we're going to return it, we have 2 edges case.

# Code challenge
# First edge case is if we have an empty link list.
# Other edge case is if we only have one node in that list.

# The thing that makes this more complicated us when you move tail to the left like this and remove that the tail is moving the opposite direction of the arrow in the length list.
# The arrows are all pointing to the right and tail is moving to the left.
# So i'm going to bring in two variables pre and temp, and i'm going to set them equal to head.
# And i'm going to remove head and tail, and i'm going to move pre underneath the element.
# So what we're going todo is we're going to say if temp.next is not none, in other words, we're not to the end of the list.
# What we're going todo is we're going to set pre equal to temp, which it is already in the first iteration and then we're going to set temp equl to temp.next.
# And keep doing this, then this will be the last time that it's not none, we're going to move pre up. temp over and now temp.next is equal to none. And these stop right here.
# So we're going to need that temp variable to return that node that we're popping off the end.
# But for right now i'm going to remove temp and we'll work with the pre variable first.
# The only thing the pre variable is four is we're going to set tail equal to pre and that's the only thing we're going to use four.
# That's going to move tail back. Then we'll say tail.next is none that breaks this off the end of the list.
# And remember temp is stil pointing four, and we need that to be able to return this. We'll say return temp and that returns this node.(previous element in the linked list.)
# (4 is the last element in the example linked list.)

# Lecture8
# linked list : Pop Code.
# We had three difference scenarios to code for, and i tend to start with the one where we don't have any items and three are a few ways to test for this.


def pop(self):
    if self.length == 0:  # You Could say if head is none, tail is none.
        return None

# So the next situation we're going to code for is if we have two or more items in the linked list.
# We're going to have two variables that are going to be temp and pre.
# We'll say temp equals self.head and pre eqauls self.head.
# And we're saying while temp,while temp connects is true, if it's pointing to a node it's true.
# And where this is going to become not true is at the end of the list where that pointer is going to be None. So there are couple of different ways you could write this.

    temp = self.head
    pre = self.head
    # In this case, temp.next is pointing at a node, which is going to make this true.
    while (temp.next):
        pre = temp  # It is already pointing to the same node as temp.
        # We'll say temp equals temp.next, which moves temp over like that.
        temp = temp.next
    self.tail = pre
    # we need to take that four and break it off from the end of the linkedlist.
    self.tail.next = None

# So this is we wrote so far.


def pop(self):
    if self.length == 0:
        return None
    temp = self.head
    pre = self.head
    while (temp.next):
        pre = temp
        temp = temp.next
    self.tail = pre
    self.tail.next = None
    self.length -= 1

# But it still leaves us with one other edge case. That's the situation where you have one node.
# Let's walk through this situation, we have head and tail pointing to it. We have temp and pre set equal to head.
# All four of these pointers are going to be pointing at this one node.
# So the two highlighted lines of code there, temp and pre, i'm going to remove those two and everything above it and we'll walk through these now.
    while (temp.next):
        pre = temp
        self.tail = pre
        self.tial.next = None
        self.length -= 1
# so temp.next is not none we're going to run this loop.
# Right after that this equates to false, and the while loop does not run.
# So remove the while loop.
# And that's all we're going to use temp for. so drop temp out.
    # They are already pointing at the same item, so that doesn't do anything.
    self.tail = pre
    # Tail.next is already none, so that doesn't do anything.
    self.tial.next = None
    # The only thing left todo is decrement the length by one. So the length was one bc we had the one node in there and we decrement it to 0.
    self.length -= 1
# So When we run this lines of code, We decrement the length to 0. But the problem is head and tail are still pointing at that node. So we have to correct that.
# Bring that code back here and we'll have to add a few lines of code.


def pop(self):
    if self.length == 0:
        return None
    temp = self.head
    pre = self.head
    while (temp.next):
        pre = temp
        temp = temp.next
    self.tail = pre
    self.tail.next = None
    self.length -= 1
    if self.length == 0:  # We had to started with one, we decrement it by one and then we got to 0. This just added one is when we started with 1 item.
        self.head = None
        self.tail = None
    return temp  # Which returns the node that we just removed.


my_linked_list = my_linked_list(1)
my_linked_list.append(2)

# my_linked_list.print_list()
# (2) Items - Returns 2 Node
print(my_linked_list.pop())
# (1) Item - Returns 1 Node
print(my_linked_list.pop())
# (0) Items - Returns None
print(my_linked_list.pop())

# Lecture9
# linked list : Prepend
# We're going todo is add an item to the beginning of the linked list. So first we want that new node to point at that first node (in linkedlist).
# So we need to set the next pointer on that node equal to smth that is pointing at that node.
# So we'll set the next node on the new node equal to head, and that points that over there.
# And then we'll have head point to the new node. And adds that into list.
# And of course, this is going to be a little different if we have an empty list like this.
# When we add it in this situation, we're going to have head and tail point to the new node.


def prepend(self, value):
    # The first thing we're going todo is create the node with that value.
    new_node = Node(value)
    # case 1 : empty one
    # In this situation, we're going to have head and tail point to the new node.
    # So in order to do this, we have to test to see is the list empty that we're interesting into?
    if self.length == 0:
        self.head = new_node
        self.tail = new_node
    else:  # We actually have items in the list.
        # We want that new node to point at that first element of the linkedlist node, and we'll set it equal to the head.
        new_node.next = self.head
        self.head = new_node  # Head equals new node.
    self.length += 1
    return True


my_linked_list = LinkedList_New(2)
my_linked_list.append(3)

my_linked_list.prepend(1)

my_linked_list.print_list()

# Lecture10
# linked list : Pop First
# Case 1 : if we have one itme in the link list
# This is similar to when we poppend an item off of the other end that we have an edge case for when we have one item and then we have another edge case for when we don't have any items in the link list.


def pop_first(self):
    if self.length == 0:
        return None
    # We are removing that first node there. In order to return that, we have to have smth pointing at it.
    # And we'll call that temp
    temp = self.head
    # So we'll set that equal to head.next and then it'll move that over.
    self.head = self.head.next
    temp.next = None
    self.length -= 1
    # So we'll say if the length is 0, we will have tail be set equal to none, and that solves the problem.

# the entire codes.


def pop_first(self):
    if self.length == 0:
        return None
    temp = self.head
    self.head = self.head.next
    temp.next = None
    self.length -= 1
    if self.length == 0:
        self.tail = None
    return temp  # Which is the item that we removed from the linked list.


my_linked_list = LinkedList_New(2)
my_linked_list.append(1)

# (2) Items - Returns 2 Node
print(my_linked_list.pop_first())
# (1) Item - Returns 1 Node
print(my_linked_list.pop_first())
# (0) Items - Returns None
print(my_linked_list.pop_first())

# Lecture11
# linked list : Get


def get(self, index):
    if index < 0 or index >= self.length:
        return None
    # So whatever the index is, that's going to be the number of times we have to move temp over.
    temp = self.head
    # So then, we'll create a for loop that is going to run, and get us the correct node.
    for _ in range(index):
        temp = temp.next  # That will move temp along the linked list.
    return temp


my_linked_list = LinkedList_New(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

print(my_linked_list.get(2))

# Lecture11
# linked list : Set


# set is a key word in python, so i can't use that as a method name.
def set_values(self, index, value):
    # We're going to have a variable that will iterate through to a particular index and that will change the value.
    # pass the get method of the index and then have temp point to the appropriate node.
    temp = self.get(index)
    # Get is going to return one of two things. It is either going to return none if it's an invalid index. Or it's goint to return a node.
    # So the first thing we have todo is test to see is this pointing to a node, Or is temp equal to none.
    if temp:
        temp.value = value  # This is the value that we pass the method.
        return True
    # If get method returns none, it's an invalid index, then we'll return false.
    return False


my_linked_list = LinkedList_New(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

my_linked_list.set_value(1, 4)

my_linked_list.print_list()

# Lecture12
# linked list : Insert


def insert(self, index, value):
    if index < 0 or index > self.length:
        return False
    if index == 0:
        return self.prepend(value)
    # It has the return keyword in here, which is saying once this prepend method runs, we're not going to keep running code in this method.
    # The other one is 'self' keyword, we are running this on this particular instance of the link list.
    if index == self.length:
        return self.append(value)
    # In order to add the value middle of the index, we're going to need to have a variable that points to the node before the index where we're inserting this.
    # The reason why you have it point here instead of the index where You are going to need the next pointer from that node which is you r pointing now.
    new_node = Node(value)
    temp = self.get(index - 1)
    new_node.next = temp.next
    temp.next = new_node
    self.length += 1
    return True


my_linked_list = LinkedList_New(0)
my_linked_list.append(2)

my_linked_list.insert(1, 1)

my_linked_list.print_list()

# Lecture13
# linked list : Remove


def remove(self, index):
    if index < 0 or index >= self.length:
        return None
    # The reason why we return false in other methods(like insert), and return None here?
    # Bc if we're successful in the insert method we return true, and if we weren't then we return false.
    # In the other hand, the remove method if we're successful, we're going to return a node.
    # So we return None here, bc none is the opposite of returning a node.
    if index == 0:
        return self.pop_first
    if index == self.length - 1:
        return self.pop()
    # So we've accounted for situations when the index is out of range or if it's the first item or the last item.
    # So let's look at removing an item that's somewhere in the middle. We'll do the index of two.
    # At the end of this, we're going to return temp, but we'll need another variable to point to the itme before it.
    # And to show why we need that variable pointing at the node before the one we're going to remove.
    # We need that there to be able to say prev.next points to that next node. So you have to have smth to the left of that arrow.
    prev = self.get(index - 1)
    # We have a variable at the node before this. This is more efficient and therefore correct way of doing that.
    temp = prev.next
    prev.next = temp.next
    temp.next = None
    self.length -= 1
    return temp

# Entire method of remove


def remove(self, index):
    if index < 0 or index >= self.length:
        return None
    if index == 0:
        return self.pop_first()
    if index == self.length - 1:
        return self.pop()
    prev = self.get(index - 1)
    temp = prev.next
    prev.next = temp.next
    temp.next = None
    self.length -= 1
    return temp


my_linked_list = LinkedList_New(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

print(my_linked_list.remove(2), '\n')

my_linked_list.print_list()

# Lecture14
# linked list : Reverse

# This is a very common interview question.


def reverse(self):

    # Switch the possesions of the head and tail.
    temp = self.head
    self.head = self.tail
    self.tail = temp
    after = temp.next  # Variable : Of right side of the temp.
    before = None  # Variable : Of left side of the temp.
    # And these 3 variables (temp, after, before) are iterate through the link list as we are reversing everything.
    for _ in range(self.length):
        after = temp.next
        temp.next = before  # This is what flips that arrow over the other way.
        # After this, there is a gap between elements of the linked list.
        # So you have to make sure that your linked list never breaks in such a way that you can't get to smth across that gap.
        # That is what the after variable is, therefore.
        before = temp
        temp = after

    # The for loop that goes through the length of the linked list.

# Entire code of the reverse method.


def reverse(self):
    temp = self.head
    self.head = self.tail
    self.tail = temp
    after = temp.next
    before = None
    for _ in range(self.length):
        after = temp.next
        temp.next = before
        before = temp
        temp = after


my_linked_list = LinkedList_New(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.reverse()

my_linked_list.print_list()
