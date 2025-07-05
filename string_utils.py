def reverse_string(s):
    reversed_s = ''
    for i in range(len(s)):
        reversed_s += s[i]
    return reversed_s

def to_upper(s):
    result = ''
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result