class Employee:
    __id = 0
    __name = ""
    __phone = ""
    __address = ""
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_phone(self):
        return self.__phone
    def get_address(self):
        return self.__address
    
    def set_id(self, id):
        self.__id = id
    def set_name(self, name):
        self.__name = name
    def set_phone(self, phone):
        self.__phone = phone
    def set_address(self, address):
        self.__address = address

    def obj_person(self):
        obj =  dict(id=self.__id,name=self.__name,phone=self.__phone,address=self.__address)
        return obj