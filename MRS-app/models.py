class Movie:
    def __init__(self,mid,mname,mdirector,mboxoffice ,mimg):
        self.mid = mid
        self.mname = mname
        self.mdirector = mdirector
        self.mboxoffice = mboxoffice
        self.mimg = mimg
    
    def __str__(self) :
        return f'Movie[{self.mid},{self.mname},{self.mdirector}]'

    def __repr__(self) :
        return f'Movie[{self.mid},{self.mname},{self.mdirector}]'