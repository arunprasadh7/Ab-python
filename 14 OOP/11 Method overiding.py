# Method overiding 

class  Iphone6:
    def home(self):
        print( 'Physical home button is pressed.')
    

class IphoneX(Iphone6):
    def home(self):
        print( 'Home button has been replaced with touch sensor.')
        super().home()    
    
i6 = Iphone6()
i6.home()

ix = IphoneX()
ix.home()