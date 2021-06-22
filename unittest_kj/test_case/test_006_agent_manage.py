import unittest
from unittest_kj.com.log_in import *
from HTMLTestRunnerNew import HTMLTestRunner

class AgentManage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.login=Login()
        cls.login.login()
        cls.login.web.implicitly_wait(20)
        cls.login.web.maximize_window()
        cls.login.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[8]/a/span[1]').click()

    @classmethod
    def tearDownClass(cls):
        cls.login.web.close()
        cls.login.web.quit()

    def test_001_add_agent(self):
        self.login.click(['/html/body/section/aside/div/ul/li[8]/ul/li[1]/a'])
        self.login.send_keys(['/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input','/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input','//*[@id="phone"]','/html/body/section/section/section/div/div/section/div/form/div[4]/div[1]/input','/html/body/section/section/section/div/div/section/div/form/div[5]/div[1]/input','/html/body/section/section/section/div/div/section/div/form/div[6]/div[1]/input'],['wl110110','wl','19729292929','19729292929','123456','104120123'])
        self.login.send_keys(['/html/body/section/section/section/div/div/section/div/form/div[8]/div[1]/input','/html/body/section/section/section/div/div/section/div/form/div[9]/div[1]/input'],['陕西省省长','6103299268635656'])
        self.login.click(['/html/body/section/section/section/div/div/section/div/form/div[21]/div/button'])
        self.assertEqual('恭喜！代理新增成功！',self.login.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='测试失败')

    def test_002_agent_manage(self):
        self.login.click(['/html/body/section/aside/div/ul/li[8]/ul/li[2]/a'])
        self.login.send_keys(['/html/body/section/section/section/div/div/section/div/form/div[1]/input'],['wl110110'])
        self.login.click(['/html/body/section/section/section/div/div/section/div/form/button','/html/body/section/section/section/form/div/div/section/table/tbody/tr/td[11]/a'])
        self.login.send_keys(['/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input'],['wl110'])
        self.login.click(['/html/body/section/section/section/div/div/section/div/form/div[22]/div/button'])
        self.assertEqual('恭喜，代理商修改成功！',self.login.web.find_element_by_xpath('/html/body/div[3]/div').text,msg="测试失败")

    def test_003_agent_manage(self):
        self.login.click(['/html/body/section/aside/div/ul/li[8]/ul/li[2]/a'])
        self.login.send_keys(['/html/body/section/section/section/div/div/section/div/form/div[1]/input'], ['wl110'])
        self.login.click(['/html/body/section/section/section/div/div/section/div/form/button','//*[@id="chk[]"]','/html/body/section/section/section/form/div/div/section/header/button[2]',])
        self.alert=self.login.web.switch_to.alert
        self.alert.accept()
        self.assertEqual('删除代理成功！',self.login.web.find_element_by_xpath('/html/body/div[3]/div').text,msg="测试失败")

    def test_004_add_agent_rank(self):
        self.login.click(['/html/body/section/aside/div/ul/li[8]/ul/li[3]/a'])
        self.login.send_keys(['/html/body/section/section/section/div/div/section/div/form/div[1]/input'],['最高级'])
        self.login.click(['/html/body/section/section/section/div/div/section/div/form/div[2]/select/option[2]',
                          '/html/body/section/section/section/div/div/section/div/form/div[3]/select/option[2]',
                          '/html/body/section/section/section/div/div/section/div/form/div[4]/select/option[2]',
                          '/html/body/section/section/section/div/div/section/div/form/div[5]/select/option[2]',
                          '/html/body/section/section/section/div/div/section/div/form/div[6]/select/option[2]',
                          '/html/body/section/section/section/div/div/section/div/form/div[7]/select/option[2]',
                          '/html/body/section/section/section/div/div/section/div/form/div[9]/select/option[2]',
                          '/html/body/section/section/section/div/div/section/div/form/div[10]/select/option[2]',
                          '/html/body/section/section/section/div/div/section/div/form/div[11]/select/option[2]',
                          '/html/body/section/section/section/div/div/section/div/form/div[12]/select/option[2]',
                          '/html/body/section/section/section/div/div/section/div/form/button'
                          ])
        self.assertEqual('新增代理级别成功！',self.login.web.find_element_by_xpath('/html/body/div[3]/div').text,msg="测试失败")

    def test_005_delete_agent_rank(self):
        self.login.click(['/html/body/section/aside/div/ul/li[8]/ul/li[3]/a','/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[14]/a[2]'])
        self.assertEqual('删除成功！',self.login.web.find_element_by_xpath('/html/body/div[3]/div').text,msg="测试失败")

if __name__ == '__main__':
    # unittest.main()

    suite=unittest.TestSuite()
    suite.addTest(AgentManage('test_004_add_agent_rank'))
    runner=unittest.TextTestRunner()
    runner.run(suite)
