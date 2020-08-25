i = 0

def hamborger(e):
  for i in range(e):
    print("H A M B O U R G E R\n")

def hotdoge(n):
  global i

  while True:
    print("H O T D O G E\n")
    i += 1

    if i == n:
      break

hamborger(3)
hotdoge(21)