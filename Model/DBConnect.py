import mysql.connector

class DBConnect:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(user='root', password='Minh191000', host ='127.0.0.1', port=3306, database = 'qlns', auth_plugin='mysql_native_password')
        except Exception as e:
            print(e)
            self.cnx = None
    def connect(self):
        if self.cnx is not None:
            if self.cnx.is_connected():
                return self.cnx.cursor()
        else:
            print(" Không thể kết nối tới DB")
    def commit(self):
        return self.cnx.commit()