
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
   levels = dict()
   locationList = dict(dict())
   weights = dict()

   def __init__(self):
    self.levels['high'] = 3
    self.levels['medium'] = 2
    self.levels['low'] = 1
    self.locationList['stockholm - central'] = {'stockholm - east' : 2,'stockholm - west' : 1,'stockholm - central' : 0}
    self.locationList['stockholm - east'] = {'stockholm - central' : 2,'stockholm - west': 3, 'stockholm - east' : 0}
    self.locationList['stockholm - west'] = {'stockholm - central' : 1,'stockholm - east': 3, 'stockholm - west' : 0}
    self.weights["Size"] = 2
    self.weights['Quality'] = 5
    self.weights['Price'] = 3
    self.weights['Music'] = 2
    self.weights['Location'] = 4
    self.weights['Open'] = 5

    self.caseList.append(ResturantCase("High","Low","Medium","Medium","Stockholm - Central","Mo,Tu,We,Th,Fr,Sa,Su","McDonalds"))
    self.caseList.append(ResturantCase("Low","Medium","Medium","Low","Stockholm - East","Mo,Tu,We,Th,Fr,Sa","Mamas and Tapas"))
    self.caseList.append(ResturantCase("Medium","High","High","Medium","Stockholm - Central","Mo,Tu,We,Th,Fr,Sa,Su","TGI Fridays"))
    self.caseList.append(ResturantCase("High","High","High","Low","Stockholm - West","Mo,We,Fr,Sa","Kungsholmen"))
    self.caseList.append(ResturantCase("Low","Medium","Medium","Low","Stockholm - Central","Mo,Tu,We,Fr","Rosmarin"))

   def Similarity(self,one,another):
    returnSim = 0
    diff = 0
    diffOneDays = 0
    diffAnotherDays = 0
    if one.size.lower() in self.levels.keys():
        diff = self.weights['Size'] * ((3 - abs(self.levels[one.size.lower()] - self.levels[another.size.lower()])) / 3)
    returnSim += diff
    if one.quality.lower() in self.levels.keys():
        diff = self.weights['Quality'] * ((3 - abs(self.levels[one.quality.lower()] - self.levels[another.quality.lower()])) / 3)
    returnSim += diff
    if one.price.lower() in self.levels.keys():
        diff = self.weights['Price'] * ((3 - abs(self.levels[one.price.lower()] - self.levels[another.price.lower()])) / 3)
    returnSim += diff
    if one.music.lower() in self.levels.keys():
        diff = self.weights['Music'] * ((3 - abs(self.levels[one.music.lower()] - self.levels[another.music.lower()])) / 3)
    returnSim += diff
    anotherWeekDays = list(another.openAt.split(','))
    returnSim += self.weights['Location'] * self.simLocation(one.location,another.location)
    returnSim += self.weights['Open'] * self.simDays(one.openAt,anotherWeekDays)
    
    
    return returnSim

   def simDays(self,one,another):
    if one in another:
        return 1
    else:
        return 0

   def simLocation(self,one,another):
    if one.lower() in self.locationList:
        diff = (3 - self.locationList[one.lower()][another.lower()]) / 3
        return diff 
    else:
        return 0

   def findMatchCase(self,case):
    sim = 0
    matchCase = 0
    for c in self.caseList:
        if self.Similarity(case,c) > sim:
            sim = self.Similarity(case,c)
            matchCase = c
    return matchCase


CB = CaseBase()
breakFlag = False
while 1:
    print("\nResturant case (type exit to exit....): ")
    print("Format: Low - Medium - High or None")
    while 1:
        size = input("Size: ")
        if size == "exit":
            breakFlag = True
            break
        elif size.lower() == 'none':
            break
        elif size.lower() not in CB.levels.keys():
            print("Wrong format try again!")
        else:
            break
    if breakFlag == True:
        break
    while 1:
        quality = input("Quality: ")
        if quality.lower() == 'none':
            break
        elif quality.lower() not in CB.levels.keys():
            print("Wrong format try again!")
        else:
            break
    while 1:
        price = input("Price: ")
        if price.lower() == 'none':
            break
        elif price.lower() not in CB.levels.keys():
            print("Wrong format try again!")
        else:
            break
    while 1:
        music = input("Music: ")
        if music.lower() == 'none':
            break
        elif music.lower() not in CB.levels.keys():
            print("Wrong format try again!")
        else:
            break
    while 1:
        location = input("Location (town - area): ")
        if location.lower() == 'none':
            break
        elif location.lower() not in CB.locationList.keys():
            print("Wrong format try again!")
        else:
            break
    while 1:
        openAt = input("Open at (mo,tu,we ...): ")
        if openAt.lower() == 'none':
            break
        elif openAt.lower() not in ['mo','tu','we','th','fr','sa','su']:
            print("Wrong format try again!")
        else:
            break
    solutionCase = CB.findMatchCase(ResturantCase(size,quality,price,music,location,openAt))
    CB.caseList.append(ResturantCase(size,quality,price,music,location,openAt,solutionCase.solution))
    print("The most matching case in the case base: ")
    solutionCase.print()
    