'''sett={'hello',2,'hi',1}
print(dir(set))
print(set())'''
myset={"apple","orange"}
print(myset)
myset.add("banana")
print(myset)
myset.update(["hollo",85,99])
print(myset)
myset.discard("banana")
print(myset)
myset.remove("orange")
print(myset)
myset.discard("grape")
print(myset)
#length of the set
print(len(myset))
subset={"book","pen",2,7}
print(subset)
print(type(subset))
subset.remove("pen")
print(subset)
myset.add(subset("book"))
print(myset)

