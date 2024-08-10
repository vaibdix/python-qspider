
#########################
# IMP
########################

class Test:
    @staticmethod
    def demo():
        print("demo")


class Test2(Test):
    @staticmethod
    def demo2():
        super(Test2,Test2).demo()
        print("demo2")

Test2.demo2()
