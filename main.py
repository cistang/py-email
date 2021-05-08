#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py.py    
@Contact :   tc.vip@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/26 12:42 下午   tc      1.0         None
'''

# import lib
import smtplib
from email.mime.text import MIMEText
import pymysql
import re
from datetime import date

d = date.today()
today_str = d.isoformat()
# 打开数据库连接
db = pymysql.connect(host="localhost", user="usr_bidinfo", password="20201203", database="db_bidinfo")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
ret_cont = ''
sql = 'select projname,originurl,constructlocation from tb_bidinfo where infodate="' + today_str + '"'
#是否有新上线招标信息
hasNewData=False
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    if not results:
        hasNewData=False
    else:
        hasNewData = True
        no_tmp = 1
        proj_num=len(results)
        for row in results:
            ret_cont = ret_cont +'<p>'+str(no_tmp)+"、"+'<a href="'+row[1] +'">'+row[0] + "</a></p>"
            no_tmp = no_tmp + 1
        title_tmp="今日上线"+str(proj_num)+"个项目"
        ret_cont=title_tmp+ret_cont
except pymysql.Error as e:
    ret_cont = str(e.args[0]) + str(e.args[1])

if hasNewData:
    mail_host="smtp.yeah.net"
    mail_user="bidinfo"
    mail_pass="FTFXMKFXVSQBMJSM"

    sender="bidinfo@yeah.net"
    receivers=['hangmu2004@126.com',"775828403@qq.com","zhijuntest@163.com"]

    #设置email信息
    #邮件内容设置
    message = MIMEText(ret_cont,'html','utf-8')
    #邮件主题
    message['Subject'] = title_tmp
    #发送方信息
    message['From'] = sender
    #接受方信息
    receivers_str=';'.join(receivers)
    message['To'] = receivers_str

    #登录并发送邮件
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host,465)
        #连接到服务器
        #smtpObj.connect()
        #登录到服务器
        smtpObj.login(mail_user,mail_pass)
        #发送
        smtpObj.sendmail(
            sender,receivers,message.as_string())
        #退出
        smtpObj.quit()
        print('send email successfully')
    except smtplib.SMTPException as e:
        print('error',e) #打印错误
else:
    print('today has no new data')