names=("hello","hihi","namaste","pranam")
print(names[1])
print(names[-1])
print(names[-2])
print(names[1:3])
print(names[:-1])
print(names[::-1])
print(names[1::])
l=list(names)
l[1]="hi"
t=tuple(l)
print(t)
for a in names:
    print(a)
for a in l:
    print(a)
for a in t:
    print(a)