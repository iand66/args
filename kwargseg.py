def func(*args, **kwargs):
    print(args, kwargs)
    print(*args) #Unpack args
    #print(**kwargs) #Invalid result

func(1,2,3,4,5, one=1, two=2) #Keyword arguments