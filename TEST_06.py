# 跳过特定函数
# skipif(条件,理由=none)   条件最好是布尔类型的   true  flase
# 条件为true,跳过函数,条件为flase,不跳过
# 标记预期失败函数   xfail(true,reason=理由)  运行预期失败的函数  xpassed  断言成功
#                                          xfail  断言失败
import pytest
class Test:
    @pytest.mark.skipif(True,reason='leyi')
    def test_01(self):
        print('我是111111')
    # 跳过的如果符合预期断言,就会显示xpassed
    @pytest.mark.xfail(2>1,reason='haha')
    def test_02(self):
        print('我是222222')
        assert True

    # 跳过的如果不符合预期断言,就会显示xfail
    @pytest.mark.xfail(2>1,reason='xixi')
    def test_03(self):
        print('我是33333')
        assert False

    @pytest.mark.xfail(2 > 3, reason='xixi')
    def test_04(self):
        print('我是44444')
        assert False


