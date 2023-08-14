# Lecture1
# Classes, Classes are an incredibly iportant topic because every data structure that we're going to create is going to be created using classes.
class Cookie:  # declare the class
    def _init(self, color):  # consturtor's syntax.
        # and one of the things that is going to be different about a method, then a function is the self keyword. If it has self in there, it is a method that is part of a class.
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

cookie_one.set_color('yellow')

print('\nCookie one is now', cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color())

# Lecture2
# So when we do this, we're creating an interger 11 somewhere in memory, and then we point the variable.
num1 = 11
num2 = num1

print("Before num2 value is updated: ")
print("num1 =", num1)
print("num2 =", num2)

# This is going to give us the address where num one and num two are sorted.
print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))
# When run this and then you can see here that num one and num two point to the exact same address.
# They are pointing to the same number 11 in memory.
# Now the next question is what happens if we set num two to be equal to 22?
num2 = 22

print("After num2 value is updated: ")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))
# This is num two has been updated.
# In other words, now num one and num two r two different values and that num one here after the change is the same as it was before the changes.
# And the reason for that is that intergers are what called immutable, which means they cannot be changed.
# Once you put a number 11 into a particular place in memory, you can't change the number11.

dict1 = {
    'value': 11
}

dict2 = dict1
# The both of dictionaries r going to point to the same dictionary.
# So this is something that is going to be the same as if we are working with an integer.
print("\n\nBefore value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

dict2['value'] = 22

print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
# So now after the value is updated, both dict1 and dict2 have value 22.
# This is diffrent that what we had with integers.
# Also, you can see the dict1 and dict2 are still pointing to the same address, which is identical to what is was before we did the update.
# Intergers are immutable they can't be changed but dictinoaries can be changed.
# When we have a linked list, the nodes in a linked list are going to operate very much like dictionaries.

dict3 = {
    'value': 33
}
dict2 = dict3
# if we set dict2 to be equal to dict3. We can take that and point that down at the new dictionary so we can change where there variables point to.
# We might want to move ahead to point to a new node.
# And when we do that, we just need to set head to be equal to smth else that is pointing at that node.
dict1 = dict2
# If so, that dict1 is going to point that down here, and we'll have all three variables pointing at this same dictionary.
# Not the question is, '{ 'value': 11 }' what happens to this dict, bc we no longer have anything pointing to it.
# And if you don't have variables that's pointing to this, you don't have any way to access this.
# So what python does in this situation is python will remove this through a process called garbage collection.
