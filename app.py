import os
from flask import Flask, render_template, request
app = Flask(__name__, template_folder="templtes")
path = os.path.dirname(os.path.abspath(__file__))


class Id:
    name = ""
    email = ""
    pin = ""
    roomNo = 0
    roomType = ""
    expenditures = 0
    myOrderedFoods = []

    def __init__(self, nameR, emailR, pinR, no, typeRoom, expen):
        self.name = nameR
        self.email = emailR
        self.pin = pinR
        self.roomNo = no
        self.roomType = typeRoom
        self.expenditures = expen
        self.myOrderedFoods = []

    def addOrderedFood(self, name, quantity, price):
        orderfood = OrderedFoods(name, int(quantity), int(price))
        self.myOrderedFoods.append(orderfood)


class OrderedFoods:
    namefood = ""
    quantity = 0
    price = 0

    def __init__(self, name, quantity, price):
        self.namefood = name
        self.quantity = quantity
        self.price = price


class workers:
    name = ""
    job = ""
    salary = ""

    def __init__(self, name, job, salary):
        self.name = name
        self.job = job
        self.salary = salary


class Foods:
    name = ""
    price = 0
    quantity = 0

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = int(price)
        self.quantity = int(quantity)


class Rooms:
    typeRoom = ""
    priceRoom = 0
    totalRooms = 0
    bookRooms = 0
    startingRoom = 0

    def __init__(self, typeR, priceR, totalR, book, sRoom):
        self.typeRoom = typeR
        self.priceRoom = priceR
        self.totalRooms = totalR
        self.bookRooms = book+sRoom
        self.startingRoom = sRoom

class RequestResidence:
    name = ""
    email = ""
    pin = ""
    def __init__(self,name,email,pin):
        self.name = name
        self.email = email
        self.pin = pin

class RequestJobs:
    name=""
    email=""
    job=""
    def __init__(self,name,email,job):
        self.name = name
        self.email = email
        self.job = job


id_list = []
worker_List = []
sms_List = []
complains = []
food_List = []
room_List = []
request_residence=[]
request_jobs=[]
MyEmail = ""
MyPin = ""
MyName = ""
MyObject = ""
managerEmail = ""
managerName = ""
managerPin = ""
ownerEmail = ""
ownerName = ""
ownerPin = ""

# Save Data of All Residents


def saveData():
    global id_list
    file_path = path+'/data/data.txt'
    myfile = open(file_path, 'w')
    myfile.close()
    for id in id_list:
        record = id.name+","+id.email+","+id.pin+"," + \
            str(id.roomNo)+","+id.roomType+","+str(id.expenditures)
        myfile = open(file_path, 'a')
        print(record, file=myfile, sep="\n")
    myfile.close()

# Load Data of All Residents


def loaddata():
    file_path = path+'/data/data.txt'
    myfile = open(file_path, 'r')
    records = myfile.read().splitlines()
    for record in records:
        name = ""
        email = ""
        password = ""
        roomno = ""
        roomtype = ""
        expen = ""
        i = 0
        while(record[i] != ","):
            name = name + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            email = email + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            password = password + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            roomno = roomno + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            roomtype = roomtype + record[i]
            i = i+1
        i = i+1
        for x in range(i, len(record)):
            expen = expen + record[x]
        person = Id(name, email, password, int(roomno), roomtype, int(expen))
        id_list.append(person)

# Save Data of All Residents Requests


def saveDataRequestsResidents():
    global request_residence
    file_path = path+'/data/residenceRequests.txt'
    myfile = open(file_path, 'w')
    myfile.close()
    for id in request_residence:
        record = id.name+","+id.email+","+id.pin
        myfile = open(file_path, 'a')
        print(record, file=myfile, sep="\n")
    myfile.close()

# Load Data of All Residents Requests


def loaddataReqestsResidence():
    file_path = path+'/data/residenceRequests.txt'
    myfile = open(file_path, 'r')
    records = myfile.read().splitlines()
    for record in records:
        name = ""
        email = ""
        password = ""
        i = 0
        while(record[i] != ","):
            name = name + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            email = email + record[i]
            i = i+1
        i = i+1
        for x in range(i, len(record)):
            password = password + record[x]
        requests = RequestResidence(name, email, password)
        request_residence.append(requests)


# Save Data of All Jobs Requests


def saveDataRequestsJobs():
    global request_jobs
    file_path = path+'/data/jobRequests.txt'
    myfile = open(file_path, 'w')
    myfile.close()
    for id in request_jobs:
        record = id.name+","+id.email+","+id.job
        myfile = open(file_path, 'a')
        print(record, file=myfile, sep="\n")
    myfile.close()

# Load Data of All Jobs Requests


def loaddataReqestsJobs():
    file_path = path+'/data/jobRequests.txt'
    myfile = open(file_path, 'r')
    records = myfile.read().splitlines()
    for record in records:
        name = ""
        email = ""
        job = ""
        i = 0
        while(record[i] != ","):
            name = name + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            email = email + record[i]
            i = i+1
        i = i+1
        for x in range(i, len(record)):
            job = job + record[x]
        requests = RequestJobs(name, email, job)
        request_jobs.append(requests)



# Save Data of Manager


def saveDataManager():
    global managerEmail
    global managerName
    global managerPin
    file_path = path+'/data/dataManager.txt'
    myfile = open(file_path, 'w')
    myfile.close()
    record = managerName+","+managerEmail+","+managerPin
    myfile = open(file_path, 'a')
    print(record, file=myfile, sep="\n")
    myfile.close()

# Load Data of Manager


def loaddataManager():
    global managerName
    global managerEmail
    global managerPin
    file_path = path+'/data/dataManager.txt'
    myfile = open(file_path, 'r')
    records = myfile.read().splitlines()
    name = ""
    email = ""
    password = ""
    i = 0
    for record in records:
        while(record[i] != ","):
            name = name + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            email = email + record[i]
            i = i+1
        i = i+1
        for x in range(i, len(record)):
            password = password + record[x]
    managerName = name
    managerEmail = email
    managerPin = password

# Save Data of Owner


def saveDataOwner():
    global ownerEmail
    global ownerName
    global ownerPin
    file_path = path+'/data/dataOwner.txt'
    myfile = open(file_path, 'w')
    myfile.close()
    record = ownerName+","+ownerEmail+","+ownerPin
    myfile = open(file_path, 'a')
    print(record, file=myfile, sep="\n")
    myfile.close()

# Load Data of Owner


def loaddataOwner():
    global ownerName
    global ownerEmail
    global ownerPin
    file_path = path+'/data/dataOwner.txt'
    myfile = open(file_path, 'r')
    records = myfile.read().splitlines()
    name = ""
    email = ""
    password = ""
    i = 0
    for record in records:
        while(record[i] != ","):
            name = name + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            email = email + record[i]
            i = i+1
        i = i+1
        for x in range(i, len(record)):
            password = password + record[x]
    ownerName = name
    ownerEmail = email
    ownerPin = password

# Save Messages


def saveSms():
    global sms_List
    file_path = path+'/data/messages.txt'
    myfile = open(file_path, 'w')
    myfile.close()
    for sms in sms_List:
        record = sms
        myfile = open(file_path, 'a')
        print(record, file=myfile, sep="\n")
    myfile.close()


def loadSms():
    file_path = path+'/data/messages.txt'
    myfile = open(file_path, 'r')
    records = myfile.read().splitlines()
    for record in records:
        if record != "":
            sms_List.append(record)

# Save Complains


def saveComplains():
    global complains
    file_path = path+'/data/complains.txt'
    myfile = open(file_path, 'w')
    myfile.close()
    for complain in complains:
        record = complain
        myfile = open(file_path, 'a')
        print(record, file=myfile, sep="\n")
    myfile.close()


def loadComplains():
    file_path = path+'/data/complains.txt'
    myfile = open(file_path, 'r')
    records = myfile.read().splitlines()
    for record in records:
        if record != "":
            complains.append(record)

# Save Worker Data


def saveWorkerData():
    global worker_List
    file_path = path+'/data/workers.txt'
    myfile = open(file_path, 'w')
    myfile.close()
    for worker in worker_List:
        record = worker.name+","+worker.job+","+worker.salary
        myfile = open(file_path, 'a')
        print(record, file=myfile, sep="\n")
    myfile.close()


def loadWokerData():
    global worker_List
    file_path = path+'/data/workers.txt'
    myfile = open(file_path, 'r')
    records = myfile.read().splitlines()
    for record in records:
        name = ""
        job = ""
        salary = ""
        i = 0
        while(record[i] != ","):
            name = name + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            job = job + record[i]
            i = i+1
        i = i+1
        for x in range(i, len(record)):
            salary = salary + record[x]
        worker = workers(name, job, salary)
        worker_List.append(worker)

# Save Data of All Foods


def saveDataFood():
    global food_List
    file_path = path+'/data/foods.txt'
    myfile = open(file_path, 'w')
    myfile.close()
    for food in food_List:
        record = food.name+","+str(food.price)+","+str(food.quantity)
        myfile = open(file_path, 'a')
        print(record, file=myfile, sep="\n")
    myfile.close()

# Load Data of All Foods


def loadfoodData():
    file_path = path+'/data/foods.txt'
    myfile = open(file_path, 'r')
    records = myfile.read().splitlines()
    for record in records:
        name = ""
        price = ""
        quantity = ""
        i = 0
        while(record[i] != ","):
            name = name + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            price = price + record[i]
            i = i+1
        i = i+1
        for x in range(i, len(record)):
            quantity = quantity + record[x]
        food = Foods(name, price, quantity)
        food_List.append(food)

# Save Data of All Rooms


def saveDataRooms():
    global room_List
    file_path = path+'/data/rooms.txt'
    myfile = open(file_path, 'w')
    myfile.close()
    for room in room_List:
        record = room.typeRoom+","+str(room.priceRoom)+","+str(
            room.totalRooms)+","+str(room.bookRooms)+","+str(room.startingRoom)
        myfile = open(file_path, 'a')
        print(record, file=myfile, sep="\n")
    myfile.close()

# Load Data of All Rooms


def loaddataRooms():
    file_path = path+'/data/rooms.txt'
    myfile = open(file_path, 'r')
    records = myfile.read().splitlines()
    for record in records:
        typeR = ""
        priceR = ""
        totalR = ""
        bookR = ""
        startingR = ""
        i = 0
        while(record[i] != ","):
            typeR = typeR + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            priceR = priceR + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            totalR = totalR + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            bookR = bookR + record[i]
            i = i+1
        i = i+1
        for x in range(i, len(record)):
            startingR = startingR + record[x]
        room = Rooms(typeR, int(priceR), int(
            totalR), int(bookR), int(startingR))
        room_List.append(room)

# Save Data of All Ordered Foods


def saveOrerdedFoods():
    global id_list
    file_path = path+'/data/orderedProducts.txt'
    myfile = open(file_path, 'w')
    myfile.close()
    for myid in id_list:
        orderlistfoods = []
        orderlistfoods = myid.myOrderedFoods
        for myfood in orderlistfoods:
            record = myfood.namefood+"," + \
                str(myfood.quantity)+","+str(myfood.price) + \
                ","+myid.name+","+str(myid.pin)
            myfile = open(file_path, 'a')
            print(record, file=myfile, sep="\n")
    myfile.close()

# Load Data of All Ordered Foods


def loadOrderedFoods():
    global id_list
    file_path = path+'/data/orderedProducts.txt'
    myfile = open(file_path, 'r')
    records = myfile.read().splitlines()
    for record in records:
        namef = ""
        quantityf = ""
        pricef = ""
        name = ""
        pin = ""
        i = 0
        while(record[i] != ","):
            namef = namef + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            quantityf = quantityf + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            pricef = pricef + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            name = name + record[i]
            i = i+1
        i = i+1
        for x in range(i, len(record)):
            pin = pin + record[x]
        for myid in id_list:
            if(myid.name == name and myid.pin == pin):
                myid.addOrderedFood(namef, quantityf, pricef)


@app.route("/")
def Page():
    return render_template("mainLoginPage.html")

# Owner Pages


@app.route("/loginowner")
def login1():
    return render_template("Owner/loginOwner.html")


def totalexpenditures():
    total = 0
    for myid in id_list:
        total = total+float(myid.expenditures)
    return total


def totalsalaries():
    total = 0
    for worker in worker_List:
        total = total+float(worker.salary)
    return total


@app.route("/ownerhome")
def owner():
    return render_template("Owner/owner.html", variable=ownerEmail, residents=len(id_list), workers=len(worker_List), totalincome=totalexpenditures(), totalsalary=totalsalaries())


@app.route("/createAccountManager")
def AccountManager():
    return render_template("Owner/registerManager.html")


@app.route("/sendMessage")
def sendMessageManager():
    global ownerEmail
    return render_template("Owner/sendMessageToManager.html", variable=ownerEmail)


@app.route("/recieveMessage")
def recieveMessageManager():
    global sms_List
    return render_template("Owner/recieveMessageOwner.html", variable=ownerEmail, smsList=sms_List)


@app.route("/residentsDetail")
def ResidentsDetail():
    return render_template("Owner/residentDetail.html", variable=ownerEmail, My_List=id_list)


@app.route("/workersDetail")
def Workers():
    return render_template("Owner/workersDetail.html", variable=ownerEmail, MyList=worker_List)


@app.route("/room")
def MyownerRooms():
    return render_template("Owner/roomsDetail.html", variable=ownerEmail, myList=room_List)


@app.route("/sendMessageByOwner", methods=['POST', 'GET'])
def smsSend():
    global ownerEmail
    if request.method == "POST":
        sms = request.form['sms']+",owner"
        sms_List.append(sms)
        saveSms()
    return render_template("Owner/sendMessageToManager.html", variable=ownerEmail)


@app.route("/owner", methods=['POST', 'GET'])
def ownerVerfiy():
    password = request.form['pin']
    global MyEmail
    MyEmail = request.form['myemail']
    if verifyowner(MyEmail, password):
        return render_template("Owner/owner.html", variable=ownerEmail, residents=len(id_list), workers=len(worker_List), totalincome=totalexpenditures(), totalsalary=totalsalaries())
    else:
        return render_template("Owner/loginOwner.html")


def verifyowner(email, password):
    global ownerEmail
    global ownerPin
    if email == ownerEmail and password == ownerPin:
        return True
    return False


@app.route("/profileowner")
def profile1():
    return render_template("Owner/profileOwner.html", email=ownerEmail, name=ownerName, pin=ownerPin)


@app.route("/profilemanagerOwner")
def profile23():
    return render_template("Owner/profileManager.html", email=managerEmail, name=managerName, pin=managerPin)


@app.route("/signupmanager", methods=['POST', 'GET'])
def managerForm():
    global managerName
    global managerEmail
    global managerPin
    managerName = request.form['name1']+" "+request.form['name2']
    managerEmail = request.form['email']
    managerPin = request.form['password']
    saveDataManager()
    return render_template("Owner/owner.html", variable=ownerEmail, residents=len(id_list), workers=len(worker_List), totalincome=totalexpenditures(), totalsalary=totalsalaries())
    
@app.route("/registerMyOwner")
def register():
    return render_template("Owner/registerOwner.html")

@app.route("/myregisterOwner", methods=['POST', 'GET'])
def createAcoount23():
    global ownerEmail
    global ownerName
    global ownerPin
    name = request.form['name1']+" "+request.form['name2']
    email = request.form['email']
    pin = request.form['password']
    ownerName=name
    ownerEmail=email
    ownerPin=pin
    saveDataOwner()
    return render_template("Owner/loginOwner.html")

@app.route("/forgotpinowner")
def Pin():
    return render_template("Owner/forgotpinowner.html")


@app.route("/changepasswordowner")
def loadchangepagepassword():
    global ownerEmail
    return render_template("Owner/changeownerpin.html", variable=ownerEmail)


@app.route("/changePinMyOwner", methods=['POST', 'GET'])
def changeownerMypin():
    global ownerEmail
    email = request.form['owneremail']
    pin = request.form['ownerpin']
    if(verifyemail(email, pin)):
        saveDataOwner()
        return render_template("Owner/owner.html", variable=ownerEmail, residents=len(id_list), workers=len(worker_List), totalincome=totalexpenditures(), totalsalary=totalsalaries())
    else:
        return render_template("Owner/changeownerpin.html", variable=ownerEmail)


@app.route("/frogotPinOwner", methods=['POST', 'GET'])
def changeMyOwnerPassword():
    email = request.form['myemail']
    password = request.form['pin']
    if verifyemail(email, password):
        saveDataOwner()
        return render_template("Owner/loginOwner.html")
    else:
        return render_template("Owner/forgotpinowner.html")


def verifyemail(email, password):
    global ownerEmail
    global ownerPin
    if email == ownerEmail:
        ownerPin = password
        return True
    return False

# Manager Pages


@app.route("/profilemanager")
def profile2():
    return render_template("Manager/profileManager.html", email=managerEmail, name=managerName, pin=managerPin)


@app.route("/loginmanager")
def login2():
    return render_template("Manager/loginManager.html")


@app.route("/managerhome")
def manager():
    return render_template("Manager/manager.html", variable=managerEmail,totalresidents=len(id_list),totalworkers=len(worker_List),totalfoods=len(food_List),types=len(room_List))



@app.route("/sendMessageManager")
def sendMessageOwner():
    return render_template("Manager/sendMessageToOwner.html", variable=managerEmail)


@app.route("/recieveMessageManager")
def recieveMessageMYManager():
    return render_template("Manager/recieveMessageManager.html", variable=managerEmail, smsList=sms_List)


@app.route("/createAccountresident")
def Account():
    return render_template("Manager/registerResident.html")


@app.route("/registerResident", methods=['POST', 'GET'])
def createAcoount():
    name = request.form['name1']+" "+request.form['name2']
    email = request.form['email']
    pin = request.form['password']
    person = Id(name, email, pin, 0, "None", 0)
    id_list.append(person)
    saveData()
    return render_template("Manager/manager.html", variable=managerEmail,totalresidents=len(id_list),totalworkers=len(worker_List),totalfoods=len(food_List),types=len(room_List))



@app.route("/addWorker")
def Woker():
    return render_template("Manager/WorkerAdd.html")


@app.route("/addFood")
def Food():
    return render_template("Manager/foodAdd.html")


@app.route("/residents")
def ResidentDetail():
    return render_template("Manager/residentDetail.html", variable=managerEmail, My_List=id_list)

@app.route("/deleteResident",methods=['POST','GET'])
def delete1():
    global complains
    if request.method=="POST":
        idx=request.form['myindex']
        idx=int(idx)-1
        name=id_list[idx].name
        for record in complains:
            nameResident=""
            i=0
            while(record[i] != ","):
                i = i+1
            i = i+1
            for x in range(i,len(record)):
                nameResident = nameResident + record[x]
            if(nameResident==name):
                complains.pop(complains.index(record))
                saveComplains()
        id_list.pop(idx)
        saveOrerdedFoods()
        saveData()
    return render_template("Manager/residentDetail.html", variable=managerEmail, My_List=id_list)

@app.route("/workers")
def Worker():
    return render_template("Manager/workersDetail.html", variable=managerEmail, MyList=worker_List)

@app.route("/deleteWorker",methods=['POST','GET'])
def delete2():
    if request.method=="POST":
        index=request.form['myindex']
        index=int(index)-1
        worker_List.pop(index)
        saveWorkerData()
    return render_template("Manager/workersDetail.html", variable=managerEmail, MyList=worker_List)

@app.route("/Rooms")
def MyRoom():
    return render_template("Manager/roomsDetail.html", variable=managerEmail, myList=room_List)

@app.route("/deleteRoom",methods=['POST','GET'])
def delete3():
    if request.method=="POST":
        index=request.form['myindex']
        index=int(index)-1
        room_List.pop(index)
        saveDataRooms()
    return render_template("Manager/roomsDetail.html", variable=managerEmail, myList=room_List)

@app.route("/foods")
def MyFoods():
    return render_template("Manager/foodDetail.html", variable=managerEmail, MyList=food_List)

@app.route("/deleteFood",methods=['POST','GET'])
def delete4():
    if request.method=="POST":
        index=request.form['myindex']
        index=int(index)-1
        food_List.pop(index)
        saveDataFood()
    return render_template("Manager/foodDetail.html", variable=managerEmail, MyList=food_List)

@app.route("/complains")
def Mycomplains():
    global complains
    return render_template("Manager/recievedComplains.html", variable=managerEmail, listcomplains=complains)


@app.route("/addworker", methods=['POST', 'GET'])
def Workersadd():
    global managerEmail
    name = request.form['name1']+" "+request.form['name2']
    job = request.form['job']
    salary = request.form['salary']
    worker = workers(name, job, salary)
    worker_List.append(worker)
    saveWorkerData()
    return render_template("Manager/manager.html", variable=managerEmail,totalresidents=len(id_list),totalworkers=len(worker_List),totalfoods=len(food_List),types=len(room_List))


@app.route("/manager", methods=['POST', 'GET'])
def managerVerfiy():
    password = request.form['pin']
    global MyEmail
    MyEmail = request.form['myemail']
    if verifymanager(MyEmail, password):
        return render_template("Manager/manager.html", variable=managerEmail,totalresidents=len(id_list),totalworkers=len(worker_List),totalfoods=len(food_List),types=len(room_List))
    else:
        return render_template("Manager/loginManager.html")


def verifymanager(email, password):
    global managerEmail
    global managerPin
    if email == managerEmail and password == managerPin:
        return True
    return False


@app.route("/sendMessageByManager", methods=['POST', 'GET'])
def smsSendManger():
    global managerEmail
    if request.method == "POST":
        sms = request.form['sms']+",admin"
        sms_List.append(sms)
        saveSms()
    return render_template("Manager/sendMessageToManager.html", variable=managerEmail)


@app.route("/addFastFood", methods=['POST', 'GET'])
def fastFood():
    name = request.form['name1']+" "+request.form['name2']
    quantity = request.form['quantity']
    price = request.form['price']
    food = Foods(name, price, quantity)
    food_List.append(food)
    saveDataFood()
    return render_template("Manager/foodDetail.html", variable=managerEmail, MyList=food_List)


@app.route("/changepasswordmanager")
def loadchangepagepasswordmanager():
    global managerEmail
    return render_template("Manager/changemanagerpin.html", variable=managerEmail)


@app.route("/forgotmanagerpin")
def managerforgotpin():
    return render_template("Manager/forgotpinmanager.html")


@app.route("/changePinMyManager", methods=['POST', 'GET'])
def changemanagerMypin():
    global managerEmail
    email = request.form['manageremail']
    pin = request.form['managerpin']
    if(verifyemailmanager(email, pin)):
        saveDataManager()
        return render_template("Manager/manager.html", variable=managerEmail,totalresidents=len(id_list),totalworkers=len(worker_List),totalfoods=len(food_List),types=len(room_List))
    else:
        return render_template("Manager/changemanagerpin.html", variable=managerEmail)


@app.route("/frogotPinManager", methods=['POST', 'GET'])
def changeMyManagerPassword():
    email = request.form['myemail']
    password = request.form['pin']
    if verifyemailmanager(email, password):
        saveDataManager()
        return render_template("Manager/loginManager.html")
    else:
        return render_template("Manager/forgotpinmanager.html")


def verifyemailmanager(email, password):
    global managerEmail
    global managerPin
    if email == managerEmail:
        managerPin = password
        return True
    return False

@app.route("/requestsResidents")
def requests1():
    return render_template("Manager/requestResidence.html", variable=managerEmail, MyList=request_residence)

@app.route("/deleteResidentapply",methods=['POST','GET'])
def delete11():
    if request.method=="POST":
        index=request.form['myindex']
        index=int(index)-1
        request_residence.pop(index)
        saveDataRequestsResidents()
    return render_template("Manager/requestResidence.html", variable=managerEmail, MyList=request_residence)

@app.route("/requestsJobs")
def requests2():
    return render_template("Manager/requestsJobs.html", variable=managerEmail, MyList=request_jobs)

@app.route("/deleteJob",methods=['POST','GET'])
def delete22():
    if request.method=="POST":
        index=request.form['myindex']
        index=int(index)-1
        request_jobs.pop(index)
        saveDataRequestsJobs()
    return render_template("Manager/requestsJobs.html", variable=managerEmail, MyList=request_jobs)

@app.route("/changinRoom")
def ChangeRoom():
    return render_template("Manager/Rooms.html", variable=managerEmail)


@app.route("/addanewmyRoom", methods=['POST', 'GET'])
def NewRoom():
    if request.method == "POST":
        typeR = request.form['typeR']
        priceR = request.form['priceR']
        totalR = request.form['totalR']
        startingR = request.form['startingR']
        room = Rooms(typeR, int(priceR), int(totalR), 0, int(startingR))
        room_List.append(room)
        saveDataRooms()
    return render_template("Manager/roomsDetail.html", variable=managerEmail, myList=room_List)


# Login Resident

@app.route("/login")
def residentLogin():
    return render_template("Resident/loginResident.html")

@app.route("/profileresident")
def profile3():
    return render_template("Resident/profileResident.html", email=MyEmail, name=MyName, pin=MyPin)


@app.route("/resident")
def resident():
    global MyObject
    yourcomplains = calculatecomplains()
    return render_template("Resident/resident.html", variable=MyEmail, roomtype=MyObject.roomType, roomno=MyObject.roomNo, expen=MyObject.expenditures, yourcomplains=yourcomplains)


def calculatecomplains():
    global MyName
    yourcomplains = 0
    for complain in complains:
        i = 0
        i = complain.find(",")
        i = i+1
        name = complain[i:len(complain)]
        if name == MyName:
            yourcomplains = yourcomplains+1
    return yourcomplains


@app.route("/getRoom")
def allotmet():
    return render_template("Resident/allotmentofRoom.html", variable=MyEmail, roomlist=room_List)


@app.route("/orderfood")
def FastFood():
    return render_template("Resident/orderFood.html", variable=MyEmail, foodList=food_List)


@app.route("/orderfooddetail")
def FastFoodDetail():
    global MyObject
    return render_template("Resident/orderedfoods.html", variable=MyEmail, foodList=MyObject.myOrderedFoods)


@app.route("/foodDetail")
def FoodDetail():
    return render_template("Resident/foodDetails.html", variable=MyEmail, MyList=food_List)


@app.route("/sendComplains")
def complainssend():
    return render_template("Resident/sendComplains.html", variable=MyEmail)


@app.route("/sendComplain", methods=['POST', 'GET'])
def compalinsend():
    global MyName
    if request.method == "POST":
        complain = request.form['sms']+","+MyName
        complains.append(complain)
        saveComplains()
    return render_template("Resident/sendComplains.html", variable=MyEmail)


@app.route("/success", methods=['POST', 'GET'])
def loginVerfiy():
    global MyPin
    global MyObject
    MyPin = request.form['pin']
    global MyEmail
    MyEmail = request.form['myemail']
    if verify(MyEmail, MyPin):
        yourcomplains = calculatecomplains()
        return render_template("Resident/resident.html", variable=MyEmail, roomtype=MyObject.roomType, roomno=MyObject.roomNo, expen=MyObject.expenditures, yourcomplains=yourcomplains)
    else:
        return render_template("Resident/loginResident.html")


def verify(email, password):
    global MyName
    global MyObject
    for id in id_list:
        if email == id.email and password == id.pin:
            MyName = id.name
            MyObject = id
            return True
    return False


@app.route("/forgotpinresident")
def changepin():
    return render_template("Resident/changeresidentpin.html", variable=MyEmail)


@app.route("/changepinresident")
def residentpin():
    return render_template("Resident/forgot-pin-resident.html")


@app.route("/changePinMyResident", methods=['POST', 'GET'])
def changeResidentMypin():
    global MyEmail
    global MyObject
    email = request.form['residentemail']
    pin = request.form['residentpin']
    if(verifyemailResident(email, pin)):
        saveData()
        yourcomplains = calculatecomplains()
        return render_template("Resident/resident.html", variable=MyEmail, roomtype=MyObject.roomType, roomno=MyObject.roomNo, expen=MyObject.expenditures, yourcomplains=yourcomplains)
    else:
        return render_template("Resident/changeresidentpin.html", variable=managerEmail)


@app.route("/frogotPinResident", methods=['POST', 'GET'])
def changeMyResidentPassword():
    email = request.form['myemail']
    password = request.form['pin']
    if verifyemailResident(email, password):
        saveData()
        return render_template("Resident/loginResident.html")
    else:
        return render_template("Resident/forgot-pin-resident.html")


def verifyemailResident(email, password):
    global id_list
    for id in id_list:
        if email == id.email:
            id.pin = password
            return True
    return False


@app.route("/getnewRoom", methods=['POST', 'GET'])
def Myroom():
    global MyObject
    email = request.form['myemail']
    password = request.form['pin']
    roomtype = request.form['room']
    if verifyroom(email, password, roomtype):
        saveData()
        saveDataRooms()
        yourcomplains = calculatecomplains()
        return render_template("Resident/resident.html", variable=MyEmail, roomtype=MyObject.roomType, roomno=MyObject.roomNo, expen=MyObject.expenditures, yourcomplains=yourcomplains)
    else:
        return render_template("Resident/allotmentofRoom.html", variable=MyEmail, roomlist=room_List)


def verifyroom(email, password, roomtype):
    global id_list
    global room_List
    for myid in id_list:
        if(myid.email == email and myid.pin == password and myid.roomType == "None"):
            for room in room_List:
                if(room.typeRoom == roomtype):
                    myid.expenditures = myid.expenditures+(room.priceRoom)
                    room.bookRooms = room.bookRooms+1
                    if(room.totalRooms == room.bookRooms):
                        room.bookRooms = room.startingRoom
                    myid.roomNo = room.bookRooms
                    myid.roomType = room.typeRoom
                    return True
    return False


@app.route("/orderfoodnow", methods=['POST', 'GET'])
def ordermyfood():
    email = request.form['email']
    password = request.form['pin']
    food = request.form['food']
    quantity = request.form['quantity']
    if verifyemailforFood(email, password, food, quantity):
        global MyObject
        saveOrerdedFoods()
        return render_template("Resident/orderedfoods.html", variable=MyEmail, foodList=MyObject.myOrderedFoods)
    else:
        return render_template("Resident/orderFood.html", variable=MyEmail, foodList=food_List)


def verifyemailforFood(email, password, foodname, quantity):
    global id_list
    global food_List
    price = 0
    for food in food_List:
        if(food.name == foodname and (int(food.quantity)-int(quantity)) >= 0):
            price = food.price
            food.quantity = food.quantity-int(quantity)
            saveDataFood()
            for myid in id_list:
                if(myid.email == email and myid.pin == password):
                    myid.addOrderedFood(foodname, quantity, price)
                    myid.expenditures = myid.expenditures + \
                        (int(quantity)*int(price))
                    saveData()
                    return True
    return False

# Other People


@app.route("/peoplehome")
def people():
    return render_template("people.html")


@app.route("/applyresidence")
def peopleApply1():
    return render_template("ResidenceApply.html")


@app.route("/applyjob")
def peopleApply2():
    return render_template("ApplyJob.html")

@app.route("/applyResidence",methods=['POST','GET'])
def apply1():
    if request.method=="POST":
        name=request.form['name1']+" "+request.form['name2']
        email = request.form['email']
        password = request.form['pin']
        requests = RequestResidence(name, email, password)
        request_residence.append(requests)
        saveDataRequestsResidents()
        return render_template("people.html")
    return render_template("ResidenceApply.html")


@app.route("/applyJob",methods=['POST','GET'])
def apply2():
    if request.method=="POST":
        name=request.form['name1']+" "+request.form['name2']
        email = request.form['email']
        job=request.form['job']
        requests = RequestJobs(name, email, job)
        request_jobs.append(requests)
        saveDataRequestsJobs()
        return render_template("people.html")
    return render_template("ApplyJob.html")

if __name__ == "__main__":
    loaddata()
    loadOrderedFoods()
    loaddataManager()
    loaddataOwner()
    loadSms()
    loadComplains()
    loadWokerData()
    loadfoodData()
    loaddataReqestsJobs()
    loaddataReqestsResidence()
    loaddataRooms()
    app.run(debug=True,host="0.0.0.0")
