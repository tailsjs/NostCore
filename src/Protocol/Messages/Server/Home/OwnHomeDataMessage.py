from DataStream.ByteStream import Writer


class OwnHomeData(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player

    def encode(self):
        #write your ohd
        
        self.writeVInt(0)
        