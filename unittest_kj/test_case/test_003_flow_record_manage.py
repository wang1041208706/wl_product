"""
    流程记录管理:测试流程记录的新增,查询,修改及删除
"""

import unittest
from unittest_kj.com.log_in import *

class FlowRecordManage(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.dl=Login()
        self.dl.login()
        self.dl.web.implicitly_wait(20)
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/a/span[1]').click()

    @classmethod
    def tearDownClass(self):
        self.dl.web.close()
        self.dl.web.quit()

    # @unittest.skip("已过")
    def test_add_flow_category_001(self):
        """
        验证正常增加流程类别
        """
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/ul/li[1]/a').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').send_keys('材料出库')
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').send_keys('110110')
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/select/option[1]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[4]/div/button').click()
        self.assertEqual('操作成功！',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg="测试失败")

    # @unittest.skip("已过")
    def test_add_flow_category_002(self):
        """
        验证流程类别名有重复是否可以增添流程成
        """
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/ul/li[1]/a').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').send_keys('材料出库')
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').send_keys('110110')
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/select/option[1]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[4]/div/button').click()
        self.assertEqual('流程类别名有重复!',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg="测试失败")

    # @unittest.skip("已过")
    def test_update_flow_category_003(self):
        """
        验证正常修改流程类别
        """
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/ul/li[2]/a').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[7]/a').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').clear()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').send_keys('材料买破烂')
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').clear()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').send_keys('120')
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[4]/div/button').click()
        self.assertEqual('更新成功！',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='测试失败')

    # @unittest.skip("已过")
    def test_delete_single_flow_category_004(self):
        """
        验证删除流程列类别
        """
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/ul/li[2]/a').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[7]/span').click()
        self.dl.web.find_element_by_xpath('/html/body/div[4]/div[3]/a[1]').click()
        self.assertEqual('删除成功！',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='测试失败')

    # @unittest.skip("已过")
    def test_delete_volume_flow_category_005(self):
        """
        验证批量删除流程列类别
        """
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/ul/li[2]/a').click()
        self.dl.web.find_element_by_xpath('//*[@id="chk[]"]').click()
        self.dl.web.find_element_by_xpath('//*[@id="del"]').click()
        self.alert=self.dl.web.switch_to.alert
        self.alert.accept()
        time.sleep(2)
        self.ale = self.dl.web.switch_to.alert
        self.a=self.ale.text
        self.ale.accept()
        self.assertEqual('批量删除成功', self.a ,msg='测试失败')

    # @unittest.skip("已过")
    def test_delete_single_flow_record_manage_006(self):
        """
        验证单个删除流程记录管理
        """
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/ul/li[4]/a').click()
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/ul/li[4]/a').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[8]/span').click()
        self.dl.web.find_element_by_xpath('/html/body/div[4]/div[3]/a[1]').click()
        self.assertEqual('删除成功！', self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text, msg='测试失败')

    # @unittest.skip("已过")
    def test_delete_volume_flow_record_manage_007(self):
        """
        验证批量删除流程记录管理
        """
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/ul/li[4]/a').click()
        self.dl.web.find_element_by_xpath('//*[@id="chk[]"]').click()
        self.dl.web.find_element_by_xpath('//*[@id="del"]').click()
        self.alert = self.dl.web.switch_to.alert
        self.alert.accept()
        self.assertEqual('批量删除成功！', self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text, msg='测试失败')


if __name__ == '__main__':
    unittest.main()