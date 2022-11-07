def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    i=0
    k=0
    while i<len(s):
        if not s[i]== "a" and not s[i]== "e" and not s[i]== "i" and not s[i]== "o" and not s[i]== "u":
            k+=1
        i+=1
    return k
print(main("salom"))