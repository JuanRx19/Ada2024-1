#Juan Miguel Rojas Mejía
#8963761

from sys import stdin

def conflict(noWords, speech, word):
  ans = True
  if(word in speech):
    ans = False
  else:
    i = 0
    while(ans and i < len(noWords)):
      #print("Data", noWords)
      if((noWords[i][0] in speech and word == noWords[i][1]) or (noWords[i][1] in speech and word == noWords[i][0])):
        ans = False
      i+=1
  
  return ans
    
def solve(words, noWords, s, i, speech):
  if(len(speech) == s):
    print(" ".join(speech))
  else:
    for x in range(i, len(words)):
      if(conflict(noWords, speech, words[x])):
        speech.append(words[x])
        solve(words, noWords, s, x + 1, speech)
        speech.pop()
  
def main():
  C = int(stdin.readline())
  set = C
  while(C > 0):
      words = []
      noWords = []
      t, p, s = map(int, stdin.readline().split())
      for _ in range(t):
        word = stdin.readline()
        words.append(word.upper().split()[0])
        
      for _ in range(p):
        word = stdin.readline().split()
        noWords.append((word[0].upper(), word[1].upper()))
      
      words.sort(key=lambda x: (-len(x), x))

      print(f"Set {set - C + 1}:")
      solve(words, noWords, s, 0, [])
      print()
      C -= 1

main()