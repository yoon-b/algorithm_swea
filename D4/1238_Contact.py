for tc in range(1):
    n, s = map(int, input().split())
    data = list(map(int, input().split()))
    contacts = {}
    for d in range(n//2):
        if data[2 * d] in contacts.keys():
            if data[2 * d + 1] not in contacts[data[2 * d]]:
                contacts[data[2 * d]].append(data[2 * d + 1])
        else:
            contacts[data[2 * d]] = [data[2 * d + 1]]
    log = [s]
    queue = [contacts[s]]


    while queue:
        contact = queue.pop(0)
        for c in contact:
            if c not in log:
                log.append(c)

                if c in contacts.keys():
                    queue.append(contacts[c])



    print(log)


