class SubQuery:
    def __init__(self, index):
        self.index = index
        self.sums = 0
        self.LastElement = 0
    
    def getSums(self):
        return self.sums
    
    def getLastElement(self):
        return self.LastElement
    def addElement(self, element):
        self.LastElement = element
        self.sums+=element
        
        
n = int(input())
m = [int (it) for it in input().split()]
SQs = list()
m_sum = 0;
for i in range(len(m) - 1, -1, -1):
    if m[i] > m_sum:
        SQs.clear()
        m_sum = m[i]
    SQ = SubQuery(i)
    SQ.addElement(m[i])
    SQs.append(SQ)
    for j in range(len(SQs)-2, -1, -1):
        SQ = SQs[j]
        SQ.addElement(min(m[i], SQ.getLastElement()))
        if SQs[j+1].getSums() >  SQ.getSums():
            SQs.pop(j)
        elif SQ.getSums() + SQ.getLastElement() > m_sum:
            m_sum = SQ.getSums() + SQ.getLastElement()
print(" ".join(["1", str(SQs[0].index + 1),str(SQs[0].getSums())]))
