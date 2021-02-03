
def unique_list(names):
    new = list()
    for name in names:
        if name not in new:
            new.append(name)
    print(new)


a = ['Robin', 'Michelle', 'Sara', 'Robin', 'Sara']
unique_list(a)
