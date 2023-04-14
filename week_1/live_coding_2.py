"""
Write a function del_char(s,c) that takes strings s and c as input, where c has length 1 (i.e., a single character), and returns the string obtained by deleting all occurrences of c in s . If c has
length other than 1, the function should return s

"""


def del_char(s,c):
  if len(c) != 1:
    return s

  return s.replace(c,"")


if __name__ == "__main__":

    s = input()
    c = input()
    print(del_char(s,c))
