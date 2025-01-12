from PIL import Image
class StegoDecryption:
    
    
    @classmethod
    def decode(cls,img):
        cls.data = ""
        image = Image.open(img, 'r')
        imgdata = iter(image.getdata())
        while (True):
            pixels = [value for value in imgdata.__next__()[:3] +
                                    imgdata.__next__()[:3] +
                                    imgdata.__next__()[:3]]

            binstr = ''

            # string of binary data
            for i in pixels[:8]:
                if (i % 2 == 0):
                    binstr += '0'
                else:
                    binstr += '1'

            cls.data += chr(int(binstr, 2))
            if (pixels[-1] % 2 != 0):
                return cls.data
                # print(self.data)


