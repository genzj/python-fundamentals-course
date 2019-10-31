def stat(s):
    ans = dict()
    for c in s:
        if c not in ans:
            ans[c] = 1
        else:
            ans[c] += 1
    print(ans)


stat('''The quick brown
     fox jumps over the lazy dog''')
