import sys

def exit():
  sys.exit(0)

def scramble(L):
  A = L
  i = 2
  print(A)
  while (i < len(A)):
    A[i-2] += A.pop(i-1)
    A[i-1].append(A[:i-2])
    i += 1
    print(A)
  return L

def get_flag():
  flag = "abcdefghijklmnopqrstuvwkyz"
  flag = flag.strip()
  hex_flag = []
  for c in flag:
    hex_flag.append([str(hex(ord(c)))])

  return hex_flag

def unscramble(A):
    str = []
    for a in A:
        print(a)
        if not isinstance(a[0], list):
          str.append(a[0])
        if not isinstance(a[-1], list):
          str.append(a[-1])
    return str

def main():
  flag = get_flag()
  cypher = scramble(flag)
  print(cypher)
  a = unscramble(cypher)
  result = ''.join(chr(int(h, 16)) for h in a)
  print(result)

if __name__ == '__main__':
  main()
