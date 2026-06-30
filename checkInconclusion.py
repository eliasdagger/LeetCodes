
def checkInclusion(s1: str, s2: str) -> bool:
    l, r = 0, len(s1)
    while r <= len(s2):
        if "".join(sorted(s1)) in "".join(sorted(s2[l:r])):
            return True
        else:
            r += 1
            l += 1
    return False

s1 = "abc"
s2 = "lecabee"

print(checkInclusion(s1, s2))

