words = []
with open('file.txt', 'r', encoding='utf-8') as f:
    for l in f:
        if l[-1] == '\n':
            words.append(l[:-1])
        else:
            words.append(l)

def bruteforce(words):
    best = 0
    best_pair = None
    for i in range(len(words)):
        for j in range(len(words)):
            if words[i] != words[j]:
                for l in range(min(len(words[i]), len(words[j])), 0, -1):
                    if words[i][-l:] == words[j][:l]:
                        if l > best:
                            best = l
                            best_pair = (words[i], words[j])
    return best, best_pair

def dict_find(words):
    prefix = dict()
    best = 0
    best_pair = None
    for w in words:
        for l in range(1, len(w) + 1):
            if w[:l] not in prefix:
                prefix[w[:l]] = {w:''}
            else:
                prefix[w[:l]][w] = ''

    for word in words:
        for l in range(len(word), 0 ,-1):
            suf = word[-l:]
            if suf in prefix:
                for second_word in prefix[suf]:
                    if second_word != word:
                        if l > best:
                            best = l
                            best_pair = (word, second_word)
    return best, best_pair
