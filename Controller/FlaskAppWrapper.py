from flask import request


class FlaskAppWrapper:
    # Khai báo các thành phần khởi tạo chương trình flask
    # config : cài đặt và thiết lập cho chương tình vd : kết nối database
    

    # hàm mặc định khi chạy class sẽ chạy vào hàm này
    # khai báo **configs để có thể thêm key và value nếu k biết số lượng là bao nhiêu
    def __init__(self, app , **configs) -> None:
        self.app = app # khởi tạo tên app
        self.configs(**configs) # truyền **configs xuống hàm configs
    
    # hàm lấy ra giữ liệu có trong **configs
    def configs(self, **configs):
        for config,value in  configs.items(): # lấy ra các key và value 
            self.app.config[config.upper()] = value # config nó với app

    """
    tạo ra các API URL: tên url, hàm xử lý, các phương thức: [GET, PUT, POST, DELTE]
    Sử dụng phương thức add_url_rule
    /blog/<int:post_id>
    /score/<float:score>
    /hello/<string:name>
    """

    # hàm khởi tạo các API url gồm tên url, hàm xử lý và các phương thức
    def add_enpoint(self, enpoint=None, enpoint_name = None, handler = None , methods = ["GET"], *args,**kwargs):
        self.app.add_url_rule(enpoint,enpoint_name,handler,methods=methods,*args,**kwargs)
    def run(self,**kwargs):
        self.app.run(**kwargs)