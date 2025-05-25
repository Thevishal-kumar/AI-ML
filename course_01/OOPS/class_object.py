import string
import random

class ShortURL:
    
    def __init__(self):
        self.d = dict()

    def getShortURL(self, longURL):
        l = random.randint(6, 10)
        chars = string.ascii_lowercase
        shortURL = ''.join(random.choice(chars) for i in range(l))

        if shortURL in self.d:
            return self.getShortURL(longURL)
        else:
            self.d[shortURL] = longURL

        r = "https://www.shortURL.com/" + shortURL
        return r

    def getLongURL(self, shortURL):
        # extract key from URL https://www.shortURL.com/mxzmuis ---> mxzmuis
        k = shortURL[25:]

        if k in self.d:
            return self.d[k]
        else:
            return None

# Test
s = ShortURL()
short = s.getShortURL("appliedaicourse.com")
print(short)

print(s.d)
print(s.getLongURL(short))
