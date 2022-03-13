def news(s, k, h):
    b = k-h+1
    if len(s) > 0:
        last = s[len(s)-1]
        if b > last[0]:
            s.append([k,h])
        else:
            s.pop()
            f = min(k-h, last[0] - last[1])
            news(s, k, k-f)
    else:
        s.append([k,h])

t = int(input())
dicts = []
for i in range(t):
    d ={'n': int(input())}
    k = [int (it) for it in input().split()]
    d.update({'k': k}) 
    h = [int (it) for it in input().split()]
    d.update({'h': h})
    dicts.append(d)
for d in dicts:
    s = []
    for i in range(d.get('n')):
        k = d['k'][i]
        h = d['h'][i]
        news(s, k, h)
    n = 0    
    for i in s:
        n+=i[1] * (i[1]+1)
    print(n//2)
        