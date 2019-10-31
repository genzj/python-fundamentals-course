import collections

def stat(s):
    ans = collections.Counter(s)
    print(ans)
    return ans


ans = stat('The quick brown fox jumps over the lazy dog')


l = [2, 3, 5, 1, 2]
def qsort(l):
    if not l:
        return l
    return qsort([x for x in l[1:] if x <l[0]]) + [l[0],] + qsort([x for x in l[1:] if x >= l[0]])

print(qsort(l))
