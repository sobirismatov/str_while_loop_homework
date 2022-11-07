def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    k=0
    while i<len(s):
        if s[i].isdigit():
            k+=int(s[i])
        i+=1
    return k
print(main("12345"))