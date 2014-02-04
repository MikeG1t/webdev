def encryptn(s):
  alph = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'    
  LETTERS = len(alph)
  
  if s not in alph:
    return s
  if (alph.find(s)+26) >= LETTERS-1:
    return alph[(alph.find(s)+26) - (LETTERS)]
    
  return alph[alph.find(s) + 26]

def encryp(s):
  a=""
  for c in s:
    a = a+encryptn(c)
    
  return a