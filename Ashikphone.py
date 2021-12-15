class phone_Contacts:                                                                                   
    
    def __init__(self,Firstname,Lastname,Phone_number,Email_ID,Groups,):                             
        self.firstname=Firstname
        self.lastname=Lastname
        self.phonenumber=Phone_number
        self.emailid=Email_ID
        self.groups=Groups
        
        
    def open_phcontacts(self):
        print("Phone Contacts")
    
        
    def firstname_verification(self):
        if type(self.firstname) == str:
            if len(self.firstname) <= 15:                                                                               
                print("Firstnameame verified")
            else:
                raise ValueError("Firstnameame should contain lesser than or equal to 15 letters")
        else:
            raise TypeError("Firstname should contain letters only")
        
    def lastname_verification(self):
        if type(self.lastname) == str:
            if len(self.lastname) <= 15:                                                                                
                print("Lastnameame verified")
            else:
                raise ValueError("Lastnameame should contain lesser than or equal to 15 letters")
        else:
            raise TypeError("Lastname should contain letters only")
        
    def phonenumber_verification(self):
        if (len(self.phonenumber)==10):
            if type(int(self.phonenumber)) == int:                                                                           
                print("Phone number verified")
            else:
                raise TypeError("Phone number should contain only integers ")
        else:
            raise ValueError("phone number should not be grater than or lesser than 10")
        
    def emailid_verification(self):
        if type(self.emailid) == str:                                                                                   
            if len(self.emailid) <= 25:                                                                              
                print("Emailid verified")
            else:
                raise ValueError("Emailid should not contain more than 25 values")
        else:
            raise TypeError("Invalid emailid")    
        

    def printgroupname(self):
        print("Groups:",self.groups)
   


Ashik=phone_Contacts("Dawoud","Ahsik","6382421835","ahsikdawoud@gmail.com","Family")
Ashik.open_phcontacts()
Ashik.firstname_verification()
Ashik.lastname_verification()
Ashik.phonenumber_verification()
Ashik.emailid_verification()
Ashik.printgroupname()



        
phone=[{"Firstname":"Amma","Lastname":"S","Phno":9952853238,"Email_id":"amma@gmail.com","Groups":"Family"},            
       {"Firstname":"Sheik","Lastname":"Alavudeen","Phno":9442030861,"Email_id":"sheik@gmail.com","Groups":"Family"},
       {"Firstname":"Yasin","Lastname":"D","Phno":9150148146,"Email_id":"yasin@gmail.com","Groups":"Friends"},
       {"Firstname":"Dawoud","Lastname":"S","Phno":6382421835,"Email_id":"dawoud@gmail.com","Groups":"Friends"},
       {"Firstname":"Suhail","Lastname":"Y","Phno":7945217876,"Email_id":"suhail@gmail.com","Groups":"Friends"},
       {"Firstname":"abshal","Lastname":"M","Phno":9745831987,"Email_id":"abshal@gmail.com","Groups":"Friends"},
       {"Firstname":"Mufa","Lastname":"K","Phno":9553311754,"Email_id":"mufa@gmail.com","Groups":"Friends"},
       {"Firstname":"Bahubali","Lastname":"P","Phno":9987647581,"Email_id":"bahu@gmail.com","Groups":"Friends"},
       {"Firstname":"Nifan","Lastname":"K","Phno":9745880765,"Email_id":"nifan@gmail.com","Groups":"Friends"},
       {"Firstname":"Babu","Lastname":"B","Phno":9987784538,"Email_id":"babu@gmail.com","Groups":"Friends"},
       {"Firstname":"Deepti","Lastname":"D","Phno":9654958752,"Email_id":"deepti@gmail.com","Groups":"Family"},
       {"Firstname":"Cibi","Lastname":"D","Phno":9765091234,"Email_id":"cibi@gmail.com","Groups":"Friends"},
       {"Firstname":"Deepan","Lastname":"Kumar","Phno":9911560926,"Email_id":"deepan@gmail.com","Groups":"Family"},
       {"Firstname":"Deepak","Lastname":"Kumar","Phno":9760243567,"Email_id":"deepak@gmail.com","Groups":"Friends"},
       {"Firstname":"Sovtha","Lastname":"S","Phno":7609125846,"Email_id":"sovtha@gmail.com","Groups":"v"},
       {"Firstname":"Dhaslim","Lastname":"L","Phno":6345126709,"Email_id":"dhaslim@gmail.com","Groups":"Friends"},
       {"Firstname":"Mano","Lastname":"P","Phno":9813245753,"Email_id":"mano@gmail.com","Groups":"Friends"},
       {"Firstname":"Mani","Lastname":"G","Phno":8547654908,"Email_id":"mani@gmail.com","Groups":"Friends"},
       {"Firstname":"Fathima","Lastname":"Z","Phno":9987654448,"Email_id":"fathima@gmail.com","Groups":"Friends"},
       {"Firstname":"Divya","Lastname":"K","Phno":9987968454,"Email_id":"divya@gmail.com","Groups":"Family"},
       {"Firstname":"Gokul","Lastname":"Raj","Phno":9815645678,"Email_id":"gokul@gmail.com","Groups":"Friends"},
       {"Firstname":"Gopal","Lastname":"Krishna","Phno":9987654457,"Email_id":"gopal@gmail.com","Groups":"Friends"},
       {"Firstname":"Malli","Lastname":"R","Phno":997868765,"Email_id":"malli@gmail.com","Groups":"Friends"},
       {"Firstname":"Alisha","Lastname":"L","Phno":9987667854,"Email_id":"alisha@gmail.com","Groups":"Family"},
       {"Firstname":"Sinan","Lastname":"N","Phno":9856985245,"Email_id":"sinan@gmail.com","Groups":"Friends"},
       {"Firstname":"Nela","Lastname":"V","Phno":9813232145,"Email_id":"nela@gmail.com","Groups":"Friends"},
       {"Firstname":"Prasanth","Lastname":"H","Phno":9987968234,"Email_id":"Prasanth@gmail.com","Groups":"Friends"},
       {"Firstname":"Hari","Lastname":"L","Phno":7899654987,"Email_id":"hari@gmail.com","Groups":"Friends"},
       {"Firstname":"Indhu","Lastname":"Mathi","Phno":9987968234,"Email_id":"indhu@gmail.com","Groups":"Friends"},
       {"Firstname":"Dinesh","Lastname":"Kumar","Phno":9813287654,"Email_id":"dinesh@gmail.com","Groups":"Friends"},
       {"Firstname":"Aysha","Lastname":"T","Phno":9002136547,"Email_id":"aysha@gmail.com","Groups":"Family"},
       {"Firstname":"John","Lastname":"S","Phno":9838564210,"Email_id":"john@gmail.com","Groups":"Friends"},
       {"Firstname":"sarath","Lastname":"M","Phno":9987755220,"Email_id":"sarath@gmail.com","Groups":"Friends"},
       {"Firstname":"Jesima","Lastname":"Y","Phno":9786541023,"Email_id":"jesima@gmail.com","Groups":"Family"},
       {"Firstname":"Jailani","Lastname":"P","Phno":9987321045,"Email_id":"jailani@gmail.com","Groups":"Friends"},
       {"Firstname":"Kannan","Lastname":"L","Phno":9813245678,"Email_id":"kannan@gmail.com","Groups":"Family"},
       {"Firstname":"Dharama","Lastname":"Raj","Phno":9875640123,"Email_id":"dharma@gmail.com","Groups":"Friends"},
       {"Firstname":"Salman","Lastname":"Farish","Phno":7894561230,"Email_id":"salman@gmail.com","Groups":"Family"},
       {"Firstname":"Anand","Lastname":"Raj","Phno":9632587410,"Email_id":"anand@gmail.com","Groups":"Friends"},
       {"Firstname":"Suresh","Lastname":"N","Phno":9813453217,"Email_id":"suresh@gmail.com","Groups":"Friends"},
       {"Firstname":"Mano","Lastname":"Ranjini","Phno":9856980765,"Email_id":"mano@gmail.com","Groups":"Family"},
       {"Firstname":"Afshar","Lastname":"A","Phno":6383888349,"Email_id":"appu@gmail.com","Groups":"Friends"},
       {"Firstname":"Madhu","Lastname":"Mathi","Phno":9874561230,"Email_id":"madhu@gmail.com","Groups":"Friends"},
       {"Firstname":"Meera","Lastname":"Bhai","Phno":8925311304,"Email_id":"meera@gmail.com","Groups":"Family"},
       {"Firstname":"Banu","Lastname":"Amma","Phno":9677733481,"Email_id":"banu@gmail.com","Groups":"Family"},]


for i in phone:                                                                                                               
    for j,k in i.items():                                                                                                     
        print(f"{j}:{k}")

    
