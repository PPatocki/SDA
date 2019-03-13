

slowo='kajak'

def palindrom(slowo):
    if slowo == slowo[::-1]:    #zamiast ifa wystarczy return slowo == slowo[::-1]
        return True
    else:
        return False

print(palindrom(slowo))


