l=(1,2,3,4,5,6)
l_itr=iter(l)
print(l_itr)
while True:
    try:
        l_next=next(l_itr)
        print(l_next)
    except StopIteration:
        break    