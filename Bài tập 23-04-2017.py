#-What is nested list?
##It is a list that is created to hold data, in a given order.

#-Can a list store both integers and strings in it?
##Yes, yes it can.

#-Do exercise 1, 2 in this chapter:

#1.Finish CRUD exercise in class, simulate a clothes shop:
#items
item0 = "T-shirt"
item1 = "Sweater"
item2 = "Jeans"
#list
items = ["T=shirt","Sweater","Jeans"]
print(items)
#update
items[1]="Skirt"
print(items)
#delete
del items[2]
print(items)


#2. You are a shepherd who owns a flock of sheep
#sheep size
sheep0 = 12
sheep1 = 8
sheep2 = 10
sheep3 = 11
sheep4 = 9

#show list
sizes = [12,8,10,11,9]
print("Hello, I'm Hoang and here's my sheep sizes", sizes)

#chose the biggest
sizes = [12,8,10,11,9]
print("It's" ,sizes.index(max(sizes)), ",I have my biggest sheep, lets sheer it!")

#replace the sheered sheep size with default size = 8
sizes = [12,8,10,11,9]
for n,i in enumerate(sizes):
    if i == max(sizes):
        sizes[n]=8
print("This is my post sheering sheep flock" ,sizes)

#next month the sheep increase in size by 50 each
a = list(sizes)
b = [f+50for f in a]
print("My sheeps has got fatter this month",b)
c = [f+50for f in b]
print("My sheeps has got fatter this month",c)
d = [f+50for f in c]
print("My sheeps has got fatter this month",d)
e = [f+50for f in d]
print("My sheeps has got fatter this month",e)

#selling wool
s = sum(e)
print("My flock has",s ,"in total")
t = s*2
print("I would get",s ,"* 2 $ =", t, "$")
