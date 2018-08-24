#In python every thing is a object. Object are typed,variable are untyped.
print(isinstance(4,object))
print(isinstance("Hello",object))
print(isinstance(None,object))
print(isinstance([1,2,3],object))

#object have identity
#id(object) gives object's "identity"
#"identity" is unique and fixed during an object's lifetime
#objects are tagged with their type at runtime
#objects contain pointers to their data blob
#This means even small things take up a lot of space!

print((4).__sizeof__())
