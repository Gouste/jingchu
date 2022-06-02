# -----------------------------
# -*- coding: utf-8 -*-
# @Time    : 2022/3/28 14:32
# @Author  : wk！
# @Project : UiTest
# @FileName: extend_utils
# @Software: PyCharm
# -----------------------------
import zmail
import re
from bs4 import BeautifulSoup
from pyotp import TOTP


class Utils:

    @staticmethod
    def get_email():
        # 登录服务器
        server = zmail.server('1806755030@qq.com', 'lbfwptfabavnddbh')  # 暂时只跑通了qq邮箱的邮件读取,126邮箱的无法读取
        # 获取指定条件的邮件

        mail = server.get_mails(subject='Activation Code（Sign Up）', sender='Kimpper', )  # 可能有缓存,所以下方多调用了一次获取邮件的接口
        # zmail.show(mail)
        mail = server.get_mails(subject='Activation Code（Sign Up）', sender='Kimpper', )
        # 看一看邮件内容
        # zmail.show(mail)
        # print(mail)  # 列表
        # 获取邮件文本内容
        # text_list = mail[0].get('Content_text')[0]
        # result1 = re.search(r"Code: (\d+)For", text_list, re.M | re.S).group(1)
        # 获取邮件的html内容,取最新的邮件
        html_info = mail[-1].get('content_html')[0]
        # print(type(html_info))
        # 解析html
        soup = BeautifulSoup(html_info, 'lxml')
        code = list(soup.stripped_strings)[3]
        # print(html_info)
        # re.compile()
        return code


if __name__ == '__main__':
    obj = Utils()
    text = obj.get_email()
    print(text)
