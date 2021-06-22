from unittest_kj.com.log_in import *
import unittest



class ProdectManage(unittest.TestCase):
    def setUp(self):
        self.dl = Login()
        self.dl.login()

    def tearDown(self):
        self.dl.web.close()
        self.dl.web.quit()

    def test_001(self):
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/a/span[1]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/ul/li[1]/a').click()
        list_address=['/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input','/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input']
        list_argument=['woi','666']
        self.dl.send_keys(list_address,list_argument)
        list_address1=['/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/select/option[1]','/html/body/section/section/section/div/div/section/div/form/div[4]/div/button']
        self.dl.click(list_address1)
        self.assertEqual('操作成功！', self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text, msg="测试失败")

if __name__ == '__main__':
    unittest.main()