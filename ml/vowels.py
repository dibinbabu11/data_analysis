class about:
    def above(self,v,count,vo):
        self.v=v
        self.count=count
        self.vo=vo
    def hello(self):
        self.v=input("enter your string=")
        self.count=0
        self.vo="aeiou"
        for i in self.v:
            if i in self.vo:
                self.count=self.count+1
        return self.count
    def pr(self):
        print(self.count)
a=about()
a.above("","","")
a.hello()
a.pr()
