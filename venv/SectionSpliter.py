import re


class SectionSplitter:
    def __init__(self, sectionExpression):
        sectionNames = []
        users = []
        sections = []
        self.txt = sectionExpression

    def showAll(self):
        testStr = re.findall(r"§§(.+?)§§", self.txt, flags=re.DOTALL)
        #for i in range(0, en(testStr)):
            #print(testStr[i])
        count = 0
        for element in testStr:
            print(element)
            count +=1


        print(len(testStr))
        print(count)
        #
        print("show zzz")






