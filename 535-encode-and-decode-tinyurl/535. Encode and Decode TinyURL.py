class Codec:
    def __init__(self):
        self.dic = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        hashedValue = "http://tinyurl.com/" + str(hash(longUrl))
        self.dic[hashedValue] = longUrl
        return hashedValue
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.dic[shortUrl]


        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))