from collections import Counter

def vote(votes):
    counter = Counter(votes)
    return sorted(counter.items(), key=lambda x: x[1])[-1][0]

if __name__ == '__main__':
    vote()


# 1
# 2