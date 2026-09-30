class FSO: # ABC = abstract base class
    pass
class File(FSO):
    pass
class Folder(FSO):
    def _init__ (self, contents: list[FSO]):
        self.contents = contents 

