from functools import reduce

l1 = [1,2,3,4,5,6,7,8,9,10]
ans = reduce(lambda a, b: a * b, l1)

print(ans)


# agar a*b mei a=1 and b=2
#product s mei save hoga abd jab next value pe jaenge to array se 3 
#value be mei jaega and s se 2 value a mei aise hi phir inka product krenge