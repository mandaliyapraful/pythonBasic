sqaures = [1, 3, 4, 6, 8, 9]
print(sqaures)
print(sqaures[-1])
print(sqaures[-3:])
print(sqaures[:])
sqaures += [2, 5, 7]
print(sqaures[:])
#Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:
sqaures[1] = 10
print(sqaures[:])
sqaures.append(3)
print(sqaures)
print(sorted(sqaures))
#replace some value
sqaures[2:5] = ['a', 'b', 'c']
print(sqaures[:]) 
# reomve values from particular index(range)
sqaures[2:5] = []
print(sqaures[:])
#nested list
alpha = ['a', 'b', 'c']
alphaNum = [alpha, sqaures]
print(alphaNum)

house =  ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]
print(house)
del(house[-4:-2])
print(house)



