from unittest_kj.com.log_in import *
import unittest
from HTMLTestRunnerNew import HTMLTestRunner

class EncasementManage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login=Login()
        cls.login.login()
        cls.login.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[5]/a/span[1]').click()

    @classmethod
    def tearDownClass(cls):
        cls.login.web.close()
        cls.login.web.quit()

    # @unittest.skip('s')
    def test_001_porduct_single_encasement(self):
        self.login.click(['/html/body/section/aside/div/ul/li[5]/ul/li[1]/a'])
        self.login.send_keys(['/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/textarea','//*[@id="minbox"]'],["900639123",'1234567899'])
        self.login.click(['/html/body/section/section/section/div/div/section/div/form/div[4]/div/button'])
        self.assertEqual('装箱成功！',self.login.web.find_element_by_xpath('/html/body/div[3]/div').text,msg="测试失败")

    def test_002_small_to_big(self):
        self.login.click(['/html/body/section/aside/div/ul/li[5]/ul/li[2]/a'])
        self.login.send_keys(['/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/textarea','//*[@id="bigbox"]'],['1234567899','199507'])
        self.login.click(['/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input','//*[@id="laydate_today"]','/html/body/section/section/section/div/div/section/div/form/div[4]/div/button'])
        self.assertEqual('信息',self.login.web.find_element_by_xpath('/html/body/div[3]/div').text,msg="测试失败")

    def test_003_big_list_manage(self):
        self.login.click(['/html/body/section/aside/div/ul/li[5]/ul/li[4]/a'])
        self.login.send_keys(['/html/body/section/section/section/div/div/section/div/form/div[1]/input'],['199507'])
        self.login.click(['/html/body/section/section/section/div/div/section/div/form/button','/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[6]/span','/html/body/div[4]/div[3]/a[1]'])
        self.assertEqual('已取消装箱！',self.login.web.find_element_by_xpath('/html/body/div[3]/div').text,msg="测试失败")

    def test_004_small_list_manage(self):
        self.login.click(['/html/body/section/aside/div/ul/li[5]/ul/li[3]/a'])
        self.login.send_keys(['/html/body/section/section/section/div/div/section/div/form/div[1]/input'],['1234567899'])
        self.login.click(['/html/body/section/section/section/div/div/section/div/form/button','/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[7]/a'])
        self.login.send_keys(['/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input'],['12333'])
        self.login.click(['/html/body/section/section/section/div/div/section/div/form/div[4]/div/button'])
        self.assertEqual('修改装箱成功！',self.login.web.find_element_by_xpath('/html/body/div[3]/div').text,msg="测试失败")

    def test_005_small_list_manage(self):
        self.login.click(['/html/body/section/aside/div/ul/li[5]/ul/li[3]/a'])
        self.login.send_keys(['/html/body/section/section/section/div/div/section/div/form/div[1]/input'],['1234567899'])
        self.login.click(['/html/body/section/section/section/div/div/section/div/form/button','/html/body/section/aside/div/ul/li[5]/ul/li[3]/a','/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[7]/span','/html/body/div[4]/div[3]/a[1]'])
        self.assertEqual('装箱已被取消！',self.login.web.find_element_by_xpath('/html/body/div[3]/div').text,msg="测试失败")

    def test_006_encasement_recor_manage(self):
        self.login.click(['/html/body/section/aside/div/ul/li[5]/ul/li[5]/a','//*[@id="chk[]"]','//*[@id="del"]'])
        self.alert=self.login.web.switch_to.alert
        self.alert.accept()
        self.assertEqual('批量删除成功！',self.login.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='测试失败')

if __name__ == '__main__':
    # unittest.main()
    suite=unittest.TestSuite()
    suite.addTest(EncasementManage('test_001_porduct_single_encasement'))
    suite.addTest(EncasementManage('test_002_small_to_big'))
    suite.addTest(EncasementManage('test_003_big_list_manage'))
    suite.addTest(EncasementManage('test_004_small_list_manage'))
    suite.addTest(EncasementManage('test_005_small_list_manage'))
    suite.addTest(EncasementManage('test_006_encasement_recor_manage'))
    rpath=r'D:\project_python\wl\unittest_kj\report\test_report_EncasementManage.html'
    f=open(rpath,"wb")
    run=HTMLTestRunner(stream=f,title="测试报告",description="ww666",tester='wl')
    run.run(suite)

