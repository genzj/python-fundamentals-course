from collections import Counter

article = '''
Twitter is officially putting tweets from strangers in your timeline
by Jon Fingas | @jonfingas | from Engadget.com 

Twitter notification page on an LG G3

You know how Twitter started inserting others' favorites and 
follows into your timeline? As it turns out, it's not an experiment -- it's official policy. We now know that the 
social network recently updated its timeline explanation to confirm that it's adding tweets from strangers, 
new accounts to follow and other "popular" content to your feed. Like you might have suspected, the company is trying 
to make your stream "even more relevant and interesting" by showing you material you might not otherwise have seen. 
'''


def filter_non_alpha(s):
    return s.translate(str.maketrans('', '', ',.|@-"\''))


def wordstat(s):
    ans = Counter(s.split())
    print(ans)
    return ans


wordstat(filter_non_alpha(article).lower())

