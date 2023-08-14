# Lecture1
# Big O is a way of Comparing Two sets of code mathematically about how efficient they run.
# Time Complexity : Time Complexity is not measured in time. it's measured in the number of operations that it takes to complete smth.
# In addition to time complexity, we measure space complexity.
# When you dealing with time complexity and space complexity There is 3 greek letters. 

# Lecture2
# Omega, Theta, Omicron which is better known as O as in BigO.
# Omega is the best case scenario for running a piece of code. Theta is average case scenario. And Omicron is worst case scenario.
# Technically when you talk about BigO, you are always talking about worst case.

# Lecture3
# About O(n)
def print_items(n) :
    for i in range(n) :
        print(i)
# This function is an example of something that is O of n (O(n))
# O of n is always going to be a straight line. (looks like y=x graph)
# That graph's bottom axis is n and on the otehr axis this is the number of operations.
# It is what is called proportional.

# Lecture4
# There are few ways in which we can simplify our BigO notations.
# First that is called Drop Constats.  
def print_items2(n) :
    for i in range(n) :
        print(i)
    for j in range(n) :
        print(j)
# print_items2 this run n + n times or 2n times. So you might think we're going to write this as 0(2n), 
# but we can simplify this O(n) by dropping constants. It doesn't mind is O(10n) or O(20n). it always simplify as O(n).

# Lecture5
# About O(n^2)
def print_items3(n) :
    for i in range(n) :
        for j in range(n) :
            print(i,j)
# print_items3 this run n * n times or n^2 times. So you might think we're going to write this as 0(n^2), 
# This grapg is much stepper than O of n, and this means it's a less efficient in time complexity standpoint.

# Lecture6
# Second simplication technique for BigO is callsed drop non-dominants.
def print_items4(n) :
    for i in range(n) :
        for j in range(n) :
            print(i,j)
            
    for k in range(n) :
        print(k)
# That nested for loops run O(n^2) times this and single loop run O(n)
# So the total number of items that we output was O(n^2) + O(n) so we could write it like O(n^2 + n).
# The main thing we're concerned about within what happens when we start having n be a very large number.
# So as a percentage of the total number of operation, it is insignificant. Bc n is a very small portion of the number.
# So in this equation, n^2 is the dominant and that stand alone n is the non-dominant term.
# That we drop the n. We drop the non-dominants.
# O(n^2 + n) -> O(n^2)

# Lecture7
# About O(1)
def add_items(n) :
    return n + n
# So far we've seen as n gets bigger the number of operations are increasing in Big(O).
# But in this case, the only operation is the addition.
# If n is 1, you have one operation. Even if n is a million, you still have one operation and that is O(1).
def add_items_V2(n) :
    return n + n + n
# Even in this situation, we're going to call it O(1)
# So O of one is also called constant time, meaning that as n increases, the number of operation is going to remain constat.
# Even if we have two additions like we do here, the number of operations will remain constant as n increases.
# O(1) is just that flat purple line across the bottom is just going to stay across the bottom bc as n increases, we r not going increasing the number of operations.
# It's the most efficient BigO any time that you can make anything O(1), that is optimal as you can make it.

# Lecture8
# About O(log n)
# Bring up a list(sorted data list) that has items one through eight in it.
# And what we're going todo is find the most efficient way of finging a number in this list.
# Take the list and cut it half and say, is it in the first half if so, then remove the second half.
# And repeat this until we found what we r looking for. 
# So we have 8 items in the list and it took us three steps to find a number.
# And it just so happens that two to the third power is eight.
# And take this equation here and turn it into a logarithm.
# Log sub two of eight equals 3.
# So if you think about a list with a billion items in it, if you're going to iterate through that linearly, from beginning to end, you could have over a billion operations.
# But if you do this process of cutting it in half repeatedly, you can find any number in that list in 31 steps,
# And that is O(log n) 
# If u see this in graphm it is very flat and very efficient. It isn't as flat as O(1), but it is far more efficient that O(n) and O(n^2).

# Lecture8
def print_items_V2(a,b) :
    for i in range(a) :
        print(i)
    for j in range(b) :
        print(j)
# Like this, the different terms for inputs, they will take what looks a whole lot like this and make a change to it.
# And where they get you with this, is that a for loop you think okay, a for loop is O(n) and then b for loop is O(n) so it could be O(n) + O(n) = O(2n).
# But u can't do that with a function that has 2 parameters.
# So it can be O(a) + O(b) -> O(a+b), you can't simplify this all the way down to one variable and call it O(n).
def print_items_V3(a,b) :
    for i in range(a) :
        for j in range(b) :
            print(i,j)
# Similarly, if you had nested for loops like this, this would be O(a * b). 
# And that is different terms for inputs.

# Lecture9
# Let's take a look at the BigO of lists. 
# And since this is a built in data structure, it's very common to compare other data structures like the ones we're going to build against lists.
# example: my_list : [11(index:0),3(index:1),23(index:2),7(index:3)]
# my_list.append(17) -> [11(index:0),3(index:1),23(index:2),7(index:3), 17(index:4)], There is no re-indexing that has to happen.
# We don't have to do any re-indexing of any of these items all the way down the list.
# my_list.pop() -> [11(index:0),3(index:1),23(index:2),7(index:3)], Once again, when we remove that, there is no re-indexing all the way down the line.
# Once again, when we remove that, there is no re-indexing all the way down the line.
# All we have todo is add or remove when we do an append or a pop. So that is O(1).
# my_list.pop(1) when we remove this, the problem that we have is that this index isn't correct.
# [3(index:0),23(index:1),7(index:2)], so we need to take that index on one and re-index it to a zero. 
# my_list.insert(0,11) -> [11(index:0),3(index:1),23(index:2),7(index:3)], in this case, we have to re-index the two like this and the next one all the way down the line in order.
# So it doesn't matter if you're removing or if you're adding to a list, it's O(n). and n in this case is the number of items in this list.
# So as far as BigO of list goes, the most important things to remember on the last index, adding or removing is O(1).
# On the first index,removing bc of the re-indexing that has to happen and bringing it back, adding it onto the list like that is O(n).
# So O(1) and O(n) on the other.
# So if we're going to look for an item and we're going to look for it by value, we're going to look for 7.
# We're going to start here and we're going to loop through iterate through this list until we get to 7, that going to be O(n).
# However, if you're going to look at this by index and you want the value that's at the index of three, You can goto directly to that place in memory based on that index that is O(1).