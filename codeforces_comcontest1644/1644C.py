# def search(arr, val, indexes):
#     for i in range(len(arr)):
#         if arr[i] == val and not i in indexes:
#             indexes.append(i)
#             return i
def max_sum(a, x, k):
    ans = a[0]
    s = 0
    min_sum = 0
    ans_l = 0
    ans_r = 0
    min_pos = 0
    for r in range(len(a)):
        s+=a[i]
        cur = s - min_sum
        if cur > ans:
            ans = cur
            ans_l = min_pos + 1
            ans_r = r
        if s < min_sum:
            min_sum = s
            min_pos = r
    return max(0, ans) + min(k,ans_r-ans_l)*x
t = int(input())
dicts = []
for i in range(t):
    nx = input().split()
    d ={'n': int(nx[0])}
    d.update({'x': int(nx[1])})
    a = [int (it) for it in input().split()]
    d.update({'a': a})
    dicts.append(d)

for d in dicts:
    n = d['n']
    x = d['x']
    a = d['a']

    # sorted_a = a.copy()
    # sorted_a.sort(reverse = True)
    p = []
    for k in range(n+1):
        # b = a.copy()
        # indexes = []
        # for j in range(k):
        #    # ind = a.index(sorted_a[j])
        #    ind = search(a, sorted_a[j], indexes) 
        #    b[ind]+=x
        # ans = b[0]
        # s = 0
        # min_sum = 0
        # for i in range(n):
        #     s+=b[i]
        #     ans = max(ans, s-min_sum)
        #     min_sum = min(min_sum, s)
        # ans = max(0, ans)
        ans = max_sum(a, x, k)
        p.append(ans)
    print(' '.join([str(it) for it in p]))
        
        
    