"""
    装箱管理:测试产品单个装箱
"""
from unittest_kj.com.log_in import *
import unittest

class SuYuanManage(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.login=Login()
        self.login.login()
        self.login.web.implicitly_wait(20)
        self.login.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[4]/a/span[1]').click()

    @classmethod
    def tearDownClass(self):
        self.login.web.close()
        self.login.web.quit()

    # @unittest.skip("s")
    def test_add_suyuan_example_001(self):
        """
        正常增加溯源实例
        """
        self.login.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[4]/ul/li[1]/a').click()
        self.login.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').send_keys('溯源实例')
        self.login.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div/div/div[2]/iframe').send_keys('溯源实例不懂')
        self.login.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[3]/div/button').click()
        self.assertIn('恭喜，溯源增加成功！',self.login.web.find_element_by_xpath('/html/body').text,msg="测试失败")

    # @unittest.skip("s")
    def test_suyuan_example_manage_select_002(self):
        self.login.click(['/html/body/section/aside/div/ul/li[4]/ul/li[2]/a'])
        self.login.send_keys(['//*[@id="key"]'],['溯源实例'])
        self.login.click(['/html/body/section/section/section/div/div/section/div/form/button'])
        self.assertEqual('溯源实例',self.login.web.find_element_by_xpath('/html/body/section/section/section/form/div/div/section/table/tbody/tr/td[3]/b').text,msg='测试失败')

    # @unittest.skip("s")
    def test_suyuan_example_manage_update_003(self):
        list_address1=['/html/body/section/aside/div/ul/li[4]/ul/li[2]/a','/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[5]/a']
        self.login.click(list_address1)
        list_address2=['/html/body/section/section/section/div[2]/div/section/div/form/div[1]/div[1]/input']
        list_argument=['wl']
        self.login.send_keys(list_address2,list_argument)
        self.login.web.iframe = self.login.web.find_elements_by_tag_name("iframe")[0]
        self.login.web.switch_to.frame(self.login.web.iframe)
        self.login.web.find_element_by_xpath('/html/body').clear()
        time.sleep(2)
        self.login.web.switch_to.default_content()
        self.login.web.find_element_by_xpath('/html/body/section/section/section/div[2]/div/section/div/form/div[2]/div/div/div[2]/iframe').send_keys("游戏6666")
        list_address3=['/html/body/section/section/section/div[2]/div/section/div/form/div[3]/div/button']
        self.login.click(list_address3)
        self.assertEqual('溯源更新成功！',self.login.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='测试失败')

    # @unittest.skip("s")
    def test_suyuan_example_manage_single_delete_004(self):
        list_address=['/html/body/section/aside/div/ul/li[4]/ul/li[2]/a','/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[5]/span','/html/body/div[4]/div[3]/a[1]']
        self.login.click(list_address)
        self.assertEqual('删除成功！',self.login.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='测试失败')

    # @unittest.skip("s")
    def test_suyuan_example_manage_volume_delete_005(self):
        list_address=['/html/body/section/aside/div/ul/li[4]/ul/li[2]/a','//*[@id="chk[]"]','//*[@id="del"]']
        self.login.click(list_address)
        self.alter=self.login.web.switch_to.alert
        self.alter.accept()
        time.sleep(2)
        self.alter1 = self.login.web.switch_to.alert
        self.a=self.alter1.text
        self.alter1.accept()
        self.assertEqual('批量删除成功',self.a,msg="测试失败")

    # @unittest.skip("s")
    def test_suyuan_example_manage_record_delete_006(self):
        list_address=['/html/body/section/aside/div/ul/li[4]/ul/li[4]/a','/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[3]/span','/html/body/div[4]/div[3]/a[1]']
        self.login.click(list_address)
        self.assertEqual('删除成功！',self.login.web.find_element_by_xpath('/html/body/div[3]/div').text,msg="测试失败")

if __name__ == '__main__':
    unittest.main()



