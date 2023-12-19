# Inner class / Nested class - class inside a class

class Customer:

    def __init__(self,id,name,bdno,bstreet,bcity,bcountry,bpin,sdno,sstreet,scity,scountry,spin):
        self.custid = id
        self.name = name
        self.baddr = self.Address(bdno,bstreet,bcity,bcountry,bpin)
        self.saddr = self.Address(sdno,sstreet,scity,scountry,spin)

    class Address:
        def __init__(self,dno,street,city,country,pin):
            self.dno = dno
            self.street = street
            self.city = city
            self.country = country
            self.pin = pin

        def display(self):
            print(self.dno)
            print(self.street)
            print(self.city)
            print(self.country)
            print(self.pin)

c1 = Customer(1,'Arun',123,'Billing Street','bcity','bcountry',600001,456,'sstreet','scity','scountry',600005)

c1.baddr.display()
c1.saddr.display()