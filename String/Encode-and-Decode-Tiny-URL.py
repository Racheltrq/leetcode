import base64
class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        lst = longUrl.split("/")
        return "https://" + lst[-1] + ".com/" + base64.b64encode(longUrl, altchars=None)
        
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        lst = shortUrl.split(".com/")
        temp = base64.b64decode(lst[-1], altchars=None)
        index = temp.find("http")
        
        return base64.b64decode(lst[-1], altchars=None)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))