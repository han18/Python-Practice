# this is python pratice 

name = "Hanan"

print(name)

# ------------------------------------

# working with tuples 

t1 = ()
t2 = (1, 'two', 3)
print(t1)
print(t2)

t1 = (1, 'two', 3)
t2 = (t1, 3.25)
print(t2)
print((t1 + t2))
print((t1 + t2)[3])
print((t1 + t2)[2:5])

x = 25
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans <= x:
 ans += step
 numGuesses += 1
print('numGuesses =', numGuesses)
if abs(ans**2 - x) >= epsilon:
 print('Failed on square root of', x)
else:
 print(ans, 'is close to square root of', x)