"""
    产品管理web页面测试
"""
from selenium import webdriver
import time
from unittest_kj.com.log_in import *
import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from ddt import ddt,data,unpack
from unittest_kj.test_data.read_data import *

@ddt
class ProdectManage(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.dl = Login()
        self.dl.login()
        self.dl.web.implicitly_wait(20)

    @classmethod
    def tearDownClass(self):
        self.dl.web.close()
        self.dl.web.quit()

    # @unittest.skip("已过")
    @data(*ReadData().read_data())
    @unpack
    def test_add_prodect_001(self,xpath1,xpath2,xpath3,xpath4,xpath5,xpath6,xpath7,xpath8):
        self.dl.web.find_element_by_xpath(xpath1).click()
        self.dl.web.find_element_by_xpath(xpath2).click()
        self.dl.web.find_element_by_xpath(xpath3).send_keys("生蚝")
        self.dl.web.find_element_by_xpath(xpath4).send_keys("888888888")
        self.dl.web.find_element_by_xpath(xpath5).send_keys('888888888')
        self.dl.web.find_element_by_xpath(xpath6).send_keys("营养品")
        self.dl.web.find_element_by_xpath(xpath7).click()
        self.assertIn("产品新增成功！", self.dl.web.find_element_by_xpath(xpath8).text, msg="失败")

    # @unittest.skip("已过")
    # def test_add_prodect_002(self):
    #     """
    #         验证编号重复是否可以新增产品
    #     """
    #     self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[1]/a/span[1]').click()
    #     self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[1]/ul/li[1]/a').click()
    #     self.dl.web.find_element_by_xpath( '/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').send_keys("西红柿")
    #     self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').send_keys("888888888")
    #     self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input').send_keys('66666666')
    #     self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[8]/div/div/div[2]/iframe').send_keys("营养品")
    #     self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[9]/div/button').click()
    #     self.assertEqual("产品编号有重复!", self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text, msg="失败")
    #
    # # @unittest.skip("已过")
    # def test_add_prodect_003(self):
    #     """
    #     验证条形码重复是否可以新增产品
    #     """
    #     self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[1]/a/span[1]').click()
    #     self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[1]/ul/li[1]/a').click()
    #     self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').send_keys("西红柿")
    #     self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').send_keys("666666666")
    #     self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input').send_keys('888888888')
    #     self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[8]/div/div/div[2]/iframe').send_keys("蔬菜")
    #     self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[9]/div/button').click()
    #     self.assertIn("产品条码有重复!", self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text, msg="失败")
    #
    # # @unittest.skip("已过")
    # def test_delete_prodect_004(self):
    #     """
    #     验证删除产品
    #     """
    #     self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[1]/a/span[1]').click()
    #     self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[1]/ul/li[2]/a').click()
    #     self.dl.web.find_element_by_xpath('/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[8]/span').click()
    #     self.dl.web.find_element_by_xpath('/html/body/div[4]/div[3]/a[1]').click()
    #     self.assertIn("产品删除成功！", self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text, msg="失败")
    #
    # # @unittest.skip("已过")
    # def test_update_prodect_005(self):
    #     """
    #     验证修改产品
    #     """
    #     self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[1]/a/span[1]').click()
    #     self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[1]/ul/li[2]/a').click()
    #     self.dl.web.find_element_by_xpath('/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[8]/a').click()
    #     self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[2]/div/section/div/form/div[1]/div[1]/input').clear()
    #     self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[2]/div/section/div/form/div[1]/div[1]/input').send_keys("联盟")
    #     self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[2]/div/section/div/form/div[2]/div[1]/input').clear()
    #     self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[2]/div/section/div/form/div[2]/div[1]/input').send_keys("110")
    #     self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[2]/div/section/div/form/div[3]/div[1]/input').clear()
    #     self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[2]/div/section/div/form/div[3]/div[1]/input').send_keys("110")
    #     time.sleep(2)
    #     self.dl.web.iframe = self.dl.web.find_elements_by_tag_name("iframe")[0]
    #     self.dl.web.switch_to.frame(self.dl.web.iframe)
    #     self.dl.web.find_element_by_xpath('/html/body').clear()
    #     time.sleep(2)
    #     self.dl.web.switch_to.default_content()
    #     self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[2]/div/section/div/form/div[8]/div/div/div[2]/iframe').send_keys("游戏6666")
    #     time.sleep(2)
    #     self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[2]/div/section/div/form/div[9]/div/button').click()
    #     self.assertIn("产品更新成功", self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text, msg="失败")


if __name__ == '__main__':
    unittest.main()
    # suite=unittest.TestSuite()
    # suite.addTest(ProdectManage('test_add_prodect_001'))
    # suite.addTest(ProdectManage('test_add_prodect_002'))
    # suite.addTest(ProdectManage('test_add_prodect_003'))
    # suite.addTest(ProdectManage('test_delete_prodect_004'))
    # suite.addTest(ProdectManage('test_update_prodect_005'))
    # rpath=r'D:\project_python\wl\unittest_kj\report\test_report.html'
    # fp=open(rpath,'wb')
    # run=HTMLTestRunner(stream=fp,title="测试报告",description="产品管理",tester='王磊')
    # run=unittest.TextTestRunner()
    # run.run(suite)

