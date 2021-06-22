"""
    防伪码管理：测试防伪码的生成,查询,修改,以及删除
"""
import unittest
from unittest_kj.com.log_in import *
import pyautogui
from selenium import webdriver


class SecurityCodeManage(unittest.TestCase):
     @classmethod
     def setUpClass(self):
         self.dl=Login()
         self.dl.login()
         self.dl.web.implicitly_wait(20)

     @classmethod
     def tearDownClass(self):
         pass
         # self.dl.web.close()
         # self.dl.web.quit()

     # @unittest.skip("已过")
     def test_volume_increase_security_code_001(self):
         self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[2]/ul/li[1]/a').click()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input').send_keys('wl')
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[6]/div[1]/input').send_keys('2')
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[7]/div[1]/div/span').click()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[7]/div[1]/div/div[2]/div/div[2]/div[3]').click()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[8]/div[1]/div/span').click()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[8]/div[1]/div/div[2]/div/div[2]/div[3]').click()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[9]/div[1]/select/option[1]').click()
         self.dl.web.find_element_by_xpath('//*[@id="tj"]').click()
         self.assertEqual('恭喜，已成功生成2个防伪码！',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg="测试失败")

     # @unittest.skip("已过")
     def test_single_increase_security_code_002(self):
         self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[2]/ul/li[2]/a').click()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').clear()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').send_keys('2021060902')
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').clear()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').send_keys("wl66666676")
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input').clear()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input').send_keys('11111112')
         # self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[4]/div[2]').click()
         # self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[4]/div[1]/div/div[2]/div/div[2]/div[3]').click()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[7]/div/button').click()
         self.assertEqual('恭喜，成功生成一个防伪码！',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg="测试失败")

     @unittest.skip("生成批次号码重复可以生成防伪码")
     def test_single_increase_security_code_003(self):
         '''
            验证生成批次号重复是否可以生成新的防伪码
         '''
         self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[2]/ul/li[2]/a').click()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').clear()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').send_keys('2021060902')
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').clear()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').send_keys("wl6666668")
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input').clear()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input').send_keys('11111112')
         # self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[4]/div[2]').click()
         # self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[4]/div[1]/div/div[2]/div/div[2]/div[3]').click()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[7]/div/button').click()
         self.assertEqual('生成批次号重复',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg="测试失败")

     # @unittest.skip("已过")
     def test_single_increase_security_code_004(self):
         """
         验证防伪码号重复是否可以生成新的防伪码
         """
         self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[2]/ul/li[2]/a').click()
         self.dl.web.find_element_by_xpath( '/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').clear()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').send_keys('2021060904')
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').clear()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').send_keys("wl6666667")
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input').clear()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input').send_keys('1111112')
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[7]/div/button').click()
         self.assertEqual('防伪码有重复！!', self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text, msg="测试失败")

     # @unittest.skip("已过")
     def test_single_increase_security_code_005(self):
         """
         验证物流码号重复是否可以生成新的防伪码
         """
         self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[2]/ul/li[2]/a').click()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').clear()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').send_keys('2021060905')
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').clear()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').send_keys("wl66666677")
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input').clear()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input').send_keys('1111112')
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[7]/div/button').click()
         self.assertEqual('物流码有重复！!', self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text, msg="测试失败")

     # @unittest.skip("已过")
     def test_volume_amend_security_code_006(self):
         """
         验证物流码批量修改防伪码
         """
         self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[2]/ul/li[3]/a').click()
         self.dl.web.find_element_by_xpath('//*[@id="txm"]').send_keys('1111112')
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[1]/div/section/div/form/div[2]/div[1]/div/span').click()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[1]/div/section/div/form/div[2]/div[1]/div/div[2]/div/div[2]/div[2]').click()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[1]/div/section/div/form/div[4]/div/button').click()
         self.assertEqual('批量修改成功',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg="测试失败")

     # @unittest.skip("已过")
     def test_volume_amend_security_code_state_007(self):
         self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[2]/ul/li[5]/a').click()
         self.dl.web.find_element_by_xpath('//*[@id="txm"]').send_keys('1111112')
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[1]/div/section/div/form/div[2]/div[1]/select/option[2]').click()
         # time.sleep(2)
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[1]/div/section/div/form/div[3]/div/button').click()
         self.assertEqual('操作成功！',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg="测试失败")

     # @unittest.skip("已过")
     def test_volume_delete_security_code_008(self):
         self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[2]/ul/li[4]/a').click()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[1]/div/section/div/form/div[1]/div[1]/div/div[1]').click()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[1]/div/section/div/form/div[1]/div[1]/div/div[2]/input').send_keys('2021060902')
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[1]/div/section/div/form/div[1]/div[1]/div/div[2]/div/div[2]/div[2]').click()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[1]/div/section/div/form/div[2]/div/button').click()
         self.assertIn('批次所属防伪码批量删除成功',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg="测试失败")

     # @unittest.skip("已过")
     def test_security_code_manage_list_volum_delete_009(self):
         self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[2]/ul/li[8]/a').click()
         self.dl.web.find_element_by_xpath('//*[@id="chkAll"]').click()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/form/div/div/section/header/button[1]').click()
         self.alert=self.dl.web.switch_to.alert
         self.alert.accept()
         self.assertEqual('防伪码批量删除成功',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg="测试失败")

     # @unittest.skip("已过")
     def test_security_code_manage_list_single_delete_010(self):
         """
         删除单条防伪码
         """
         self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[2]/ul/li[8]/a').click()
         self.dl.web.find_element_by_xpath('//*[@id="chk[]"]').click()
         self.dl.web.find_element_by_xpath('/html/body/section/section/section/form/div/div/section/header/button[1]').click()
         self.alert = self.dl.web.switch_to.alert
         self.alert.accept()
         self.assertEqual('防伪码批量删除成功', self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text, msg="测试失败")

     @unittest.skip("已过")
     def test_security_code_manage_011(self):
         """
         批量导出二维码
         """
         self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[2]/ul/li[8]/a').click()
         self.dl.click(['/html/body/section/aside/div/ul/li[2]/ul/li[7]/a','/html/body/section/section/section/div[1]/div/section/div/form/div[5]/div/button'])
         self.dl.web.current_window_handle
         windows = self.dl.web.window_handles
         self.dl.web.switch_to.window(windows[-1])
         self.dl.click(['/html/body/div[1]/div/a[1]/span/b'])
         pyautogui.moveTo(589,546)
         pyautogui.click()
         pyautogui.moveTo(909, 648)
         pyautogui.click()

if __name__ == '__main__':
    unittest.main()