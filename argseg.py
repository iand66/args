def printme(*args):
    print(type(args), args)

def printme1(*args, **kwargs):
    print(type(args), args)
    print(type(kwargs), kwargs)

# printme('Ian')
# printme('Ian','Jeanette')
# printme(*'Ian','Jeanette')
# printme(*'Ian',*'Jeanette')

printme1('First', *{'Firstname':'Ian','Lastname':'Davies'})
printme1('First',**{'Firstname':'Ian','Lastname':'Davies'}) 