x = int(input("Please enter the value :"))
for i in range(x):
    print(i)

words = ['cat', 'window', 'defenestarte']

for w in words[:]:
    print(w, len(w))
    if len(w) > 6:
        words.insert(0, w)

print(words)