def func(x,y):
    print(y,x)

pairs = [(1,2),(3,4)]

for pair in pairs:
    func(pair[0],pair[1])

for pair in pairs:
    func(*pair) # Single * tuples & lists

func(**{'x':1,'y':2}) # Double * for dictionaries
func(**{'y':4,'x':9}) # Key value pairs
