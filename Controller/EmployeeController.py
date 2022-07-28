"xử lý thao tác logic ,các tính toán dữ liệu"
import json
import re
from turtle import update
from unicodedata import name
from Model.DBConnect import DBConnect
from flask import request,jsonify
from Model.Employee import Employee
import pandas as pd


class EmployeeManagment:
    def __init__(self) -> None:
        self.db = DBConnect()
        self.conn = self.db.connect()
    def add_employee(self):
        if request.method == 'POST':
            data = request.get_json()
            if data is not None:
                name = data.get('name')
                phone = data.get('phone')
                address = data.get('address')
                employee = Employee()
                employee.set_name(name)
                employee.set_phone(phone)
                employee.set_address(address)
            try:
                add_employee = ("INTO employee" "(name, phone, address)" "VALUES(%s,%s,%s)")
                data_emp = (employee.get_name(),employee.get_phone(),employee.get_address())
                self.conn.execute(add_employee,data_emp)
                self.db.commit()
                return jsonify({"status":200,"data":data})
            except Exception as e:
                return jsonify({"status":404,"data":{}})


    def update_employee(self):
        if request.method == "PUT":
            data  = request.get_json()
            check_exist = "SELECT * FROM  employee WHERE id ='" + str(data.get('id')) + "'"
            print(check_exist)
            self.conn.execute(check_exist)
            # lay 1 ban ghi
            record = self.conn.fetchone()
            if record is None:
                return jsonify({"message": "Không tìm thấy bản ghi"})
            else:
                if data is not None:
                    name = data.get('name')
                    phone = data.get('phone')
                    address = data.get('address')
                    employee = Employee()
                    employee.set_name(name)
                    employee.set_phone(phone)
                    employee.set_address(address)
                try:
                    update_employee = ("UPDATE employee SET name=%s, phone=%s, address=%s WHERE id='"+ str(data.get('id')) + "'")
                    data_emp = (employee.get_name(),employee.get_phone(),employee.get_address())
                    self.conn.execute(update_employee,data_emp)
                    self.db.commit()
                    return jsonify({"status":200,"data":data}) 
                except Exception as e:
                    return jsonify({"status":404,"data":{}})
            

    # show all 
    def show_all_data(self):
        list_result = []
        self.conn.execute("SELECT * FROM employee ")
        """
        Lấy 1 bản ghi : fetchone()
        Lấy all bản ghi : fetchall()
        """
        records = self.conn.fetchall()
        for item in records:
            employee = Employee()
            employee.set_id(item[0])
            employee.set_name(item[1])
            employee.set_phone(item[2])
            employee.set_address(item[3])
            list_result.append(employee.obj_person())
        return jsonify({"status":200,"data":list_result})
    # import excel

    def import_excel(self):
        if  request.method == "POST":
            try:
                f = request.files["file"]
                if f is not None:
                    df = pd.DataFrame(pd.read_excel(f))
                    # print(df)
                    len_data = len(df)
                    for i in range(0,len_data):
                        row = df.loc[i]
                        add_employee = ("INSERT INTO employee " "(name,phone,address)" "values(%s,%s,%s)")
                        data_emp = (str(row["name"]),str(row["phone"]),str(row["address"]))
                        self.conn.execute(add_employee,data_emp)
                        self.db.commit()
            except Exception as e:
                return jsonify({"status":404,"message":str(e)})
        return jsonify({"status":200,"message" : "Tải Lên Thành Công"})
    # Phân trang
    def paging(self):
        page = int(request.args.get("page")) if request.args.get("page") is not None else 1
        result_per_page = int(request.args.get("result_per_page")) if request.args.get("result_per_page") is not None else 5
        data_query = (result_per_page,(page-1)*result_per_page)
        self.conn.execute("SELECT * FROM employee limit %s offset %s",data_query)
        """
        limit - > giới hạn số lượng bản ghi trả về 
        offset  -> chỉ định hàng nào bắt đầu lấy ra khi trích xuất dữ liệu
        bản ghi trên 1 trang có 10 dòng
        (result_per_page,(page-1)*result_per_page)
        limit = 5 ,offset = (1-1)*5 => bắt đầu từ 0
        """
        list_result = []
        records = self.conn.fetchall()
        for item in records:
            employee = Employee()
            employee.set_id(item[0])
            employee.set_name(item[1])
            employee.set_phone(item[2])
            employee.set_address(item[3])
            list_result.append(employee.obj_person())
        obj_result = {
            'page':page,
            "result_per_page":result_per_page,
            "total":len(list_result),
            "data":list_result  
        }
        return obj_result
    #send email
    def send_email(self):
        import smtplib
        from email.mime.text import MIMEText
        # trình bày nội dung email  
        from email.mime.multipart import MIMEMultipart
        
        try:
            msg = MIMEMultipart()
            msg['From'] = "minh2k3k4k@gmail.com"
            msg['to'] = "tienloctao@gmail.com"
            msg['Subject'] = ' test send email '
            msg['msg'] = "t dang config email"
            message = "hello Looc"
            msg.attach(MIMEText(message))
            mailserver = smtplib.SMTP('smtp.gmail.com',587)
            mailserver.ehlo()
            mailserver.starttls()
            mailserver.ehlo()
            #login to gmail
            mailserver.login('Minh2k3k4k@gmail.com','rrttllzndikhvrix')
            mailserver.sendmail('Minh2k3k4k@gmail.com','tienloctao@gmail.com',msg.as_string())
            mailserver.quit()
            return jsonify({"status":200,"message":"Send email"})
        except Exception as e:
            return jsonify({"status":404,"message":str(e)})

