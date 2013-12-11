import difflib
class ResturantCase:
    size = ""
    quality = ""
    price = ""
    music = ""
    location = ""
    openAt = ""
    solution = ""

    def __init__(self, size, quality, price, music, location, openAt, solution = ""):
        self.size = size
        self.quality = quality
        self.price = price
        self.music = music
        self.location = location
        self.openAt = openAt
        self.solution = solution
    def print(self):
        print("Size: ",self.size,"\nQuality: ",self.quality,"\nPrice: ",self.price,"\nMusic: ",self.music,"\nLocation: ",self.location,"\nOpen at: ",self.openAt,"\nSolution: ",self.solution)

class CaseBase:

   caseList = list()

   def __init__(self):
    self.caseList.append(ResturantCase("Large","Low","Medium","Medium","Stockholm - Central","Mo,Tu,We,Th,Fr,Sa,Su","McDonalds"))
    self.caseList.append(ResturantCase("Small","Medium","Medium","Low","Stockholm - East","Mo,Tu,We,Th,Fr,Sa","Mamas and Tapas"))
    self.caseList.append(ResturantCase("Medium","High","High","Medium","Stockholm - Central","Mo,Tu,We,Th,Fr,Sa,Su","TGI Fridays"))
    self.caseList.append(ResturantCase("Large","High","High","Low","Stockholm - West","Mo,We,Fr,Sa","Kungsholmen"))
    self.caseList.append(ResturantCase("Small","Medium","Medium","Low","Stockholm - Central","Mo,Tu,We,Fr","Rosmarin"))

   def Similarity(self,one,another):
    returnSim = 0
    diff = difflib.SequenceMatcher(a = one.size.lower(), b = another.size.lower())
    returnSim = diff.ratio()
    diff = difflib.SequenceMatcher(a = one.quality.lower(), b = another.quality.lower())
    returnSim = returnSim + diff.ratio()
    diff = difflib.SequenceMatcher(a = one.price.lower(), b = another.price.lower())
    returnSim = returnSim + diff.ratio()
    diff = difflib.SequenceMatcher(a = one.music.lower(), b = another.music.lower())
    returnSim = returnSim + diff.ratio()
    diff = difflib.SequenceMatcher(a = one.location.lower(), b = another.location.lower())
    returnSim = returnSim + diff.ratio()
    diff = difflib.SequenceMatcher(a = one.openAt.lower(), b = another.openAt.lower())
    returnSim = returnSim + diff.ratio()

    return returnSim / 6

   def findMatchCase(self,case):
    sim = 0
    matchCase = 0
    for c in self.caseList:
        if self.Similarity(case,c) > sim:
            sim = self.Similarity(case,c)
            matchCase = c
    return matchCase


CB = CaseBase()
while 1:
    print("Resturant case (type exit to exit....): ")
    size = input("Size: ")
    if size == "exit":
        break
    quality = input("Quality: ")
    price = input("Price: ")
    music = input("Music: ")
    location = input("Location (town - area): ")
    openAt = input("Open at (day,day): ")
    solutionCase = CB.findMatchCase(ResturantCase(size,quality,price,music,location,openAt))
    CB.caseList.append(ResturantCase(size,quality,price,music,location,openAt,solutionCase.solution))
    print("The most matching case in the case base: ")
    solutionCase.print()
    