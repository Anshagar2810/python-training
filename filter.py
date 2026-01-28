l1 = [1,2,3,4,5,6,7,8,9,10]
ans = list(filter(lambda a: a & 1 == 0, l1))
print(ans)


#so ham & bhi use krsakte hai even mei chk karne ke lie


l1 = [1,2,3,4,5,6,7,8,9,10]
ans = list(filter(lambda a: not(a%2 != 0), l1))
print(ans)
