from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""

    li = []

    set_a = set([])
    set_b = set([])
    st = ""
    t = 0
    ln_a = len(a)
    ln_b = len(b)

    for i in a:
        t += 1
        if (i == '\n' or t == ln_a):
            if t == ln_a:
                st += i
            set_a.add(st)
            st = ''
        else:
            st += i

    st = ''
    t = 0

    for i in b:
        t += 1
        if (i == '\n' or t == ln_b):
            if t == ln_b:
                st += i
            set_b.add(st)
            st = ''
        else:
            st += i

    for i in set_a:
        for j in set_b:
            if i == j:
                li.append(i)
    		
    return li


def sentences(a, b):
    """Return sentences in both a and b"""
    # a.decode("utf8")
    
    st = set([])
    li_a = sent_tokenize(a)
    li_b = sent_tokenize(b)

    for i in li_a:
        for j in li_b:
            if i == j:
                st.add(i)

    return list(st)


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    set_a = set([])
    set_b = set([])
    sets = set([])

    ln_a = len(a)
    ln_b = len(b)

    i = 0

    while i < ln_a:
        st = ''
        cnt = 0
        k = i
        while(cnt != n and k < ln_a):
            st += a[k]
            cnt += 1
            k += 1

        if len(st) == n:
            set_a.add(st)

        i += 1
    
    i = 0

    while i < ln_b:
        st = ''
        cnt = 0
        k = i
        while(cnt != n and k < ln_b):
            st += b[k]
            cnt += 1
            k += 1

        if len(st) == n:
            set_b.add(st)

        i += 1

    for i in set_a:
        for j in set_b:
            if i == j:
                sets.add(i)

    return list(sets)