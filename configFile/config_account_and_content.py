# -*- coding: utf-8 -*-
import time
from selenium import webdriver
import datetime
from lib.randomphone import randomphone
#教务登录环境
administration_url="http://cshj3140.n4.bjmantis.cn"

#获取明日时间
today = datetime.date.today()
todayr= today.strftime('%Y-%m-%d %H:%M')
tomorrow = today + datetime.timedelta(days=1)
tomorrowr = tomorrow.strftime('%Y-%m-%d')
time.sleep(2)


#角色
name='admin'
#密码
password="qwer1234"
#=====================================================================学员中心
#学员中心报名信息
student_centre={
     'fapiao':'123456'+randomphone(),
     'freeze':'1331235'+str(randomphone()),                    #报名-冻结
     'return':'1331235'+str(randomphone()),                 #报名-退费
     'postpone':'1331235'+str(randomphone()),                  #报名-延期
     'time':'到期时间：2019-11-08',             #延期时间
     'transfer':'1331235'+str(randomphone()),                  #报名-转班
     'transfer_return':'1',                      #报名-转班-原班型退费
     'assessment2': '100',                      #转班应缴费用
     'paid2':'1',                                 #转班实缴费用
     'student':'1331239'+randomphone(),# 新增学员电话     报名电话        保持和新增电话一直
     'name':'测试'+randomphone(),            #用户姓名
     'namem':'测试'+randomphone(),           #修改基本信息，学员名称
     'assessment':'100',     #报名应缴费用
     'paid':'100',            #实缴费用
     'class1':'sd',    #报名班型
     'class2':'一级建造师包过',  #转班班型
     'site':'北京—酒仙桥—将台5号院-螳螂科技', #增加收货地址
     'invoice':'100',                           #发票金额
     'invoice_content':'单位发票'               #发票内容
}
#========================================================================学服中心
study_service={
     'addpayment': '1331235'+str(randomphone()),  # 订单管理-增加支付单
     'assessment': '2999',  # 增加支付单--报名应缴费用
     'paid': '1',  # 增加支付单--实缴费用
     'repair': '1',  # 增加支付单--支付单补缴费用
   #------------------------------------------------------------
    'cancellation':'1331235'+str(randomphone()),       #订单管理-作废
    'freeze':'1331234'+str(randomphone()),              #订单管理-冻结
   #------------------------------------------------------------
    'modify': '1331235'+str(randomphone()),             #订单管理-修改支付详情
    'modify_remark': '修改备注',        # 订单管理-修改支付详情备注
  #--------------------------------------------------------------
    'return': '1331235'+str(randomphone()),  # 订单管理-退费
    'return_money': '0.01',  # 订单管理-退费-扣费金额
  #---------------------------------------------------------------
    'transfer': '1331235'+str(randomphone()),  # 订单管理-转班
    'addpllay': '1331235'+str(randomphone()),  # 订单管理-增加报考
   #---------------------------------------------------------
    'textbook':'1331235'+str(randomphone())     #补发教材

}

#=========================================================================基础配置
configuration={
     'name1':'测试一级项目'+randomphone(),           #项目配置一级项目名称
     'name2':'测试二级项目'+randomphone(),             #项目配置--二级项目名称
     'exam':'测试修改一级项目'+randomphone(),             #考期-修改--一级项目
     'academy_name':'测试学院'+str(randomphone()),             #学院配置--新增学院名称
     'macademy_name':'测试修改学院'+str(randomphone()),       #学院配置--修改学院名称
     'service_provider':'测试服务商'+randomphone(),       #服务商配置--新增服务商
     'campus':'测试校区'+str(randomphone()),                  #校区配置---校区名称
     'C_project':'测试报考项目',                  #报考项目--新增报考规则名称
     'express':'测试快递',                         # 快递公司--新增快递公司名称
     'express_describe':'测试快递描述',       # 快递公司--修改快递公司描述
     'payment_way':'测试支付方式'+str(randomphone()),                      #支付配置--支付方式
     'cost_types':'支付类型'+str(randomphone()),                         #支付配置--支付类型
     'collection': '测试银行'+str(randomphone()),                    # 支付配置--收款机构
     'collection_remark': '测试银行'+randomphone(),            # 支付配置--收款机构-修改备注
     'work_order': '售后服务'+str(randomphone()),                    # 支付配置--工单类型-新增工单
}
#=======================================================================财务管理


financial_management={
          'reject':'1341236'+str(randomphone()),    #支付确认-驳回
          'affirm':'1341236'+str(randomphone()),    #支付确认-确认
          'invalid': '1341236'+str(randomphone()),  # 支付确认-作废

          'return': '1341236'+str(randomphone()),  # 退费记录-查看-确认退费
          'invoice': '1341236'+str(randomphone()),  # 发票管理-开票
}
#========================================================================教学运营
teaching_operation={
           'plan_name':'a计划'+str(randomphone()),     #新增- 计划名称
           'mplan_name': 'b计划'+str(randomphone()),   #修改- 计划名称

           'cpno_manage': '修改课次'+str(randomphone()),  # 课号管理——新增课次

           'recorded_broadcast': '录播课号'+str(randomphone()),  # 录播课号——修改课次

           'commodity_infrom': '商品维度标题'+str(randomphone()),       # 学员通知-商品维度-通知标题
           'cpno_infrom': '学员维度标题'+str(randomphone()),       # 学员通知-商品维度-通知标题

           'recorded_broadcast': '录播课号'+str(randomphone()),  # 课号管理——修改课次

           'present': '可不可以',  # 赠送服务--已有商品选择
           'name': 'qizhaojun',            # 赠送服务--已有商品选择


          }
#========================================================================产品管理
product_manage={
    'keci_name':'测试课次'+randomphone(),
    'lubomokuai_name':'录播模块'+randomphone(),
    'curriculum_name':'课程管理'+str(randomphone()), #课程管理-新建课程-课程名称
    'mcurriculum_name': '修改课程管理12'+str(randomphone()),  # 课程管理-新建课程-课程名称
    'module_name': '模块名称'+str(randomphone()),  # 课程管理-新建课程-模块名称
    'class_time': '课次名称' + str(randomphone()),  # 课程管理-新建课程-课次名称

    'recorded_name':'测试录播课'+str(randomphone()), #录播管理-新增-录播课程名称

    'data_name': '资源名称'+str(randomphone()),  # 资料管理-新增-新增资源名称

    'textbook_name': '测试教材'+str(randomphone()),  # 教材教辅-新增-新增教材名称
    'textbook_money': '99',  # 教材教辅-修改-修改教材价格

    'subjects_name': '毛概'+str(randomphone()),  # 科目配置-新增科目名称
    'msubjects_name': '邓论'+str(randomphone()),  # 科目配置-修改科目名称

    'quest_bank_name':'毛概题库'+str(randomphone()),   #题库管理-新增题库名称
    'mquest_bank_name': '邓论题库'+str(randomphone()),  # 题库管理-修改题库名称

    'class_type': '快速提升班'+str(randomphone()),  # 班型管理-新增班型名称
    'mclass_type': '快速提升班'+str(randomphone()),  # 班型管理-修改版型名称

    'commodity_name': '班型'+str(randomphone()),  # 商品管理-新增班型名称
    'commodity_minimum_price': '1',  # 商品管理-上架商品最低价格
    'commodity_sell_price': '100',  # 商品管理-上架商品出售价格
    'mcommodity_name': '班型'+str(randomphone()),  #      商品管理-修改商品名称

}
