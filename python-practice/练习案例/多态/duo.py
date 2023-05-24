class fuqin:
    def run(self):
        pass


class dog(fuqin):
    def run(self):
        print('dog_run')

class cat(fuqin):
    def run(self):
        print('cat_run')

dg = dog()
ct = cat()
def make(fq:fuqin):
    fq.run()

make(dg)
make(ct)
