import flask
"""
1. Cài đặt
pip install flask
2. Cấu trúc thư mục của 1 chương trình flask
- app.py -> file main chương trình chính để chạy
Thư mục Controller -> Chứa các thành phần xử lý logic, nghiệp vụ, tính toán,...
Thư mục Model -> chứa các đối tượng lưu trữ dữ liệu làm việc với db
Template -> Chứa các thành phần giao diện người dùng
Static -> chứa các thành phần về hình ảnh, âm thanh, các file css,...

3. API là gì? -> google
Có các phương thức
POST -> Thêm dữ liệu
PUT -> Cập nhật dữ liệu
GET -> Lấy dữ liệu
DELTE -> Xóa dữ liệu

"""


from flask import Flask
from Controller.FlaskAppWrapper import FlaskAppWrapper
from Controller.ViewController import ViewController
from Controller.EmployeeController import EmployeeManagment

flask_app = Flask(__name__)
app = FlaskAppWrapper(flask_app)
employee_controller = EmployeeManagment()

app.add_enpoint("/","index",ViewController().index)
app.add_enpoint('/add_employee',"add_employee",employee_controller.add_employee,methods=['POST'])
app.add_enpoint('/update_employee',"update_employee",employee_controller.update_employee, methods=["PUT"])
app.add_enpoint('/all_employee','all_employee',employee_controller.show_all_data,methods=["GET"])
app.add_enpoint('/import_excel_employee',"import_excel_employee",employee_controller.import_excel,methods=["POST"])
app.add_enpoint('/paging','paging',employee_controller.paging,methods=['GET'])
app.add_enpoint('/send_email_employee','send_email_employee',employee_controller.send_email,methods=['GET'])
if __name__ == "__main__":
    app.run(debug=True, port=8080)