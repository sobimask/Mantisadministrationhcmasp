教务自动化

    需要优化：

         1.公共模块整合 （部分完成）
         2.集成airtest框架，部分定位使用图片识别 （暂不做）
         3.数据流优化： 项目 班型 商品 考期  （部分完成）
         4.数据保存优化到一个文件 （下周完成）



    框架重点
        
        ***数据流***
        基础配置（项目-考期配置-服务商） -> 产品配置（教材，课号，录播视频，建班，上架商品）->
        学生报名（报名，付款，转班，查询信息）->学服中心（支付单，管理学员信息，处理工单）->教学运营->财务管理



    数据依赖备注
            1.基础配置 a1文件 新建一二级项目name1，name2 保存用于a2文件增加项目下考期
              a2文件 修改后的考期 kaoqi 保存用于 产品管理a4，教务a5
              a4文件 新增服务商 service_provider  保存用于 a5文件选择服务商

            2.产品管理  a1文件 课程名mcurriculum_name  保存用于 a4,a7文件
              a2文件 录播视频 luboshipin 保存用于 a文件 选择录播文件
              3文件 录播课名称 recorded  保存用于 a7文件 选择录播课
              a3文件 录播模块名 lubomokuai 保存用于 a7文件 选择录播模块


    框架优点
            1.保证新环境无数据时，数据流的正常保存调用，无需手动添加
            2.保证每个运行数据重复的同时兼容上下数据依赖
            3.多处使用模糊搜索，UI定位不易变，降低维护成本
            4.一次性添加所有case，循环遍历，自动生成报告

    PS:URL已隐藏


        11-28修改
        1.公共包报名选择的课程
        2.转班选择的课程
        3.更改公共包
        4.赠送班型


        存在问题
        test_all test_b_student_center_apply_addservice.py 新增客服单，新环境没有抄送人选择