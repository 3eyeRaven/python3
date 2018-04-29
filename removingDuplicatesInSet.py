def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1,2,3,5,6,7,7,3,2,8,6,9]

list(dedupe(a))

