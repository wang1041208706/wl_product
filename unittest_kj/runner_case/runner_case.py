import unittest
from HTMLTestRunnerNew import HTMLTestRunner
import time
test_dir=r'D:\project_python\wl\unittest_kj\test_case\\'
discover=unittest.defaultTestLoader.discover(test_dir,pattern="test_*.py")
# now=time.strftime("%Y-%m-%d %H-%M-%S")
rpath=r'D:\project_python\wl\unittest_kj\report\test_report.html'
fp=open(rpath,'wb')
runner=HTMLTestRunner(stream=fp,title="测试报告",description="产品管理",tester='王磊')
runner.run(discover)
