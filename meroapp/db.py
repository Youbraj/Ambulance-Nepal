import mysql.connector as connector

class data:
    def __init__(self):
        self.con=connector.connect(
            host='localhost', 
            user='newuser', 
            password='password', 
            database='ambulancedb')
        
        #query='create table if not exists ambulances(id int primary key, name varchar(200), contact varchar(50), address varchar(200))'
        #query2='create table if not exists patients(id int primary key, name varchar(200),gender varchar(50), contact varchar(10), address varchar(100))'
        #cursor = self.con.cursor()
        # query3='create table queries(id int primary key, name varchar(30), contact varchar(20), email varchar(50), subject varchar(100), msg varchar(1000), date varchar(20))'
        # cursor = self.con.cursor()
        # cursor.execute(query3)
        #cursor.execute(query2)
        # print("Created")

    def insert_query(self, name, contact, email, subject, msg, date):
        query="insert into queries(name, contact, email,subject,msg,date) values('{}', '{}', '{}', '{}', '{}', '{}')".format(name,contact,email,subject,msg,date)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        
    def display_query(self):
        query="select * from queries"
        cur=self.con.cursor()
        cur.execute(query)
        return cur
        # print("ID   |   Name         |     gender    |         Contact      |       Address")
        # print("----------------------------------------------------------------------")
        # for row in cur:
        #     print("{}     {}           {}               {}".format(row[0],row[1],row[2], row[3]))
        



    def insert(self,name,contact, address):
        query="insert into ambulances(name, contact, address) values('{}', '{}', '{}')".format(name,contact, address)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        # print("New user added")
        # return self.fetch()
    def search(self,name_string):
        query = "select * from ambulances where name like '{}%'".format(name_string)
        cur = self.con.cursor()
        cur.execute(query)
        return cur
    def search_multi(self,name_string,address_string):
        query = "select * from ambulances where (name like '{}%') and (address like '{}%')".format(name_string,address_string)
        cur = self.con.cursor()
        cur.execute(query)
        return cur

    def searchbyaddress(self, address):
        query="select * from ambulances where address like '{}%'".format(address)
        cur=self.con.cursor()
        cur.execute(query)
        return cur
    
    def getbyid(self, id):
        query="select * from ambulances where id='{}'".format(id)
        cur=self.con.cursor()
        cur.execute(query)
        return cur

    def fetch(self):
        query="select * from ambulances"
        cur=self.con.cursor()
        cur.execute(query)
        #data=cur.fetchall()
        # #print(data)
        # print("ID   |   Name             |         Contact      |       Address")
        # print("----------------------------------------------------------------------")
        # for row in cur:
        #      print("{}     {}           {}               {}".format(row[0],row[1],row[2], row[3]))
        return cur
            
    def delete(self, id):
        query="delete from ambulances where id= {}".format(id)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        # print("Deleted")
        #self.fetch()
    def update(self, id, name, contact, address):
        query="update ambulances set name='{}', contact='{}', address='{}' where id= {}".format(name, contact, address, id)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        # print("Deleted")
        #self.fetch()     

    def check_existing_id(self, id):
        query="select * from ambulances where id like '{}'".format(id)
        cur = self.con.cursor()
        cur.execute(query)
        if (not cur == None):
            print("ID already exits")

    def insert_patient(self, id, name, gender, contact, address):
        query="insert into patients(id, name, gender, contact, address) values({}, '{}', '{}', '{}', '{}')".format(id,name,gender, contact, address)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def show_patient(self):
        query="select * from patients"
        cur=self.con.cursor()
        cur.execute(query)

        # print("ID   |   Name         |     gender    |         Contact      |       Address")
        # print("----------------------------------------------------------------------")
        # for row in cur:
        #      print("{}     {}       {}         {}               {}".format(row[0],row[1],row[2], row[3], row[4]))


    def delete_patient(self,id):
        query="delete from patients where id= {}".format(id)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()


    def update_patient(self, id, name, gender,contact, address):
        query="update patients set name='{}', gender='{}', contact='{}', address='{}' where id= {}".format(name, gender, contact, address, id)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def search_patient(self, name):
        query = "select * from doctors where name like '{}'".format(name)
        cur = self.con.cursor()
        cur.execute(query)
        #return cur
        print(cur)

    
#d = data()
#d.insert_query(8,"Ram", "95895945", "ram123@gmail.com","About office", "Where is the office", "2022-01-05" )
#d.display_query()
# d.insert(4, "Akhil Nepal Chiya Majdur Sangh", "9814952000", "Jhapa")
# d.insert(5, "Ambulance Lalitpur Municipality", "9841202641, 01-552700", "Pulchowk, Lalitpur")
# d.insert(6, "Ambulance Service Siddhartha Club", "061530200, 061521433", "Siddhartha Chowk, Pokhara")
# d.insert(7, "Sanjivini Ayurvedic Prakritik Chikitsaylaya", "9848554800", "Chitwan")
# # d.update(18, "Dr. Sushil", "9812345854", "Colon and Rectal Surgeon")
# # d.update(9, "Dr. Binod", "9812345752", "Allergist/Immunologist")
# #d.delete(1)
# # d.fetch()
# #d.update_patient(8, "Sanjana B.K.", "FEMALE", "9876543244", "Biratnagar")
# #d.show_patient()
# d.fetch()
#d.check_existing_id(5)
