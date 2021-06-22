import unittest
from unittest_kj.com.log_in import *

class CertificateManage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login=Login()
        cls.login.login()
        cls.login.web.implicitly_wait(20)
        cls.login.click(['/html/body/section/aside/div/ul/li[2]/a/span[1]','/html/body/section/aside/div/ul/li[9]/a/span[1]'])

    @classmethod
    def tearDownClass(cls):
        # pass
        cls.login.web.close()
        cls.login.web.quit()

    def test_001_add_certificate(self):
        self.login.click(['/html/body/section/aside/div/ul/li[9]/ul/li[1]/a'])
        self.login.send_keys(['/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input','//*[@id="zsbg"]'],['博士毕业证','/upload/image/20170603/20170603193613_20104.jpg'])
        self.login.click(['/html/body/section/section/section/div/div/section/div/form/div[3]/div/button'])
        self.assertEqual('新增成功！',self.login.web.find_element_by_xpath('/html/body/div[3]/div').text,msg="测试失败")

    def test_002_certificate_manage(self):
        self.login.click(['/html/body/section/aside/div/ul/li[9]/ul/li[2]/a'])
        self.login.send_keys(['/html/body/section/section/section/div/div/section/div/form/div/input'],['博士毕业证'])
        self.login.click(['/html/body/section/section/section/div/div/section/div/form/button'])
        self.login.click(['/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[5]/a[2]'])
        self.login.send_keys(['/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input'],['最最高级代理'])
        self.login.click(['/html/body/section/section/section/div/div/section/div/form/div[3]/div/button'])
        self.assertEqual('证书分类更新成功！', self.login.web.find_element_by_xpath('/html/body/div[3]/div').text, msg="测试失败")

    def test_003_certificate_update(self):
        self.login.click(['/html/body/section/aside/div/ul/li[9]/ul/li[2]/a'])
        self.login.send_keys(['/html/body/section/section/section/div/div/section/div/form/div/input'],['最最高级代理'])
        self.login.click(['/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[5]/a[1]','/html/body/section/section/section/div[1]/div/section/div/a[2]'])
        self.login.send_keys(['/html/body/section/section/section/div/div/section/div/form/div[1]/div/textarea'],['牛B啊'])
        self.login.click(['/html/body/section/section/section/div/div/section/div/form/div[7]/div/button'])
        self.assertEqual('成功新增文本！', self.login.web.find_element_by_xpath('/html/body/div[3]/div').text, msg="测试失败")

    def test_004_certificate_delete(self):
        self.login.click(['/html/body/section/aside/div/ul/li[9]/ul/li[2]/a'])
        self.login.send_keys(['/html/body/section/section/section/div/div/section/div/form/div/input'], ['最最高级代理'])
        self.login.click(['/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[5]/span','/html/body/div[4]/div[3]/a[1]'])
        self.assertEqual('删除成功！', self.login.web.find_element_by_xpath('/html/body/div[3]/div').text, msg="测试失败")


if __name__ == '__main__':
    unittest.main()