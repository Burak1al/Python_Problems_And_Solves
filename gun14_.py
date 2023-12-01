inp = input()
# .split() eklicektim ama örnekte de yok :)
harfler = []
for char in inp:
    harfler += char
for x in harfler:
    while harfler.count(x)> 1:
        harfler.remove(x)
print(harfler)
# print(list(set(harfler)))
# this one makes the arrangement of the output random which looks ugly so i did the top one tho this IS shorter