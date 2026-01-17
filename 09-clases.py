
class operabass():

    num1=0
    num2=0
    num3=0
    
    def __init_subclass__(self):
        self.num1=0
        self.num2=0

    def suma(self,a):
            self.num1=a
            self.res=self.num1+self.num2
            print('la suma es: {}'. format(self.res))

    def resta(self):
            self.res=self.num1-self.num2
            print('la resta es: {}'. format(self.res))

def main():
    obj=operabass()
    obj.suma(5)
    obj.resta()

if __name__== '__main__':
    main()