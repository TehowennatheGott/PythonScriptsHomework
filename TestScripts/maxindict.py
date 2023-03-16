testdict = {"max":45,
            "john":55,
            "Sam":34}
print(max(testdict, key=testdict.get))