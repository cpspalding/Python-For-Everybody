# Adds variables into a dictionary and prints one name at a time in
# consecutive order on separate lines like followed
#chad:1
#chad:1 brock:1
#chad:1 brock:1 gwen:1
#chad:1 brock:1 gwen:1 Jennifer:1


ognames = dict()
names = ['chad', 'brock', 'Gwen', 'Jennifer']
for name in names:
    ognames[name] = ognames.get(name,0) + 1
    print(ognames)
