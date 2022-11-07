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
        if not s[i]== "a" or not s[i]== "e" or not s[i]== "i" or not s[i]== "o" or not s[i]== "u":
            k+=1
        i+=1
    return k
print(main("salom"))