def stat(s):
    ans = dict()
    for c in s:
        ans[c] = ans.get(c, 0) + 1
    print(ans)


stat('The quick brown fox jumps over the lazy dog')
