class Kdbx:
    '''
    kdbx file class
    '''

    def __init__(self):
        self.sig1 = 0x9AA2D903 #the first 32 bits of a kdbx file
        self.sig2 = 0xB54BFB67 #the next 32 bits of a kdbx file
