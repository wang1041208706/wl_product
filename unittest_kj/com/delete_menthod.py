import requests

class Delete():
    def test_login_01(self):
        self.url = "http://123.57.140.190/manage/?act=adminlogin"
        self.header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        self.body = {
            "Username": "admin",
            "Password": "admin999",
            "Submit": "管理登录"
        }
        self.response = requests.post(url=self.url, data=self.body, headers=self.header)
        return self.response.cookies["PHPSESSID"]

    def test_delete_product_012(self,id):
        self.url2 = "http://123.57.140.190/manage/list_cp.php?"
        self.head = {
            "act": "delete_pro",
            "id": id
        }
        self.header2 = {
            "Cookie": "PHPSESSID=" + self.test_login_01()
        }
        self.response = requests.get(url=self.url2, params=self.head, headers=self.header2)