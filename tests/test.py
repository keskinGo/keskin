import pandas as pd
import datetime
import itertools


def the_font_color(data):
    """
    普通文字黑色
    最近一个月红色，其他日期蓝色
    :param data:
    :return:
    """
    base_date = datetime.datetime.now() + datetime.timedelta(days=30)
    try:
        d = datetime.datetime.strptime(data, '%Y/%m/%d')
        if d > base_date:
            return 'color: red; background-color:blue'
        else:
            return 'color: blue'
    except:
        return 'color: black'


excel_writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')

# 第一行，客户图片（在后期单独添加）

# 第二~四行
title = {
    'title': ['重庆金牧（成都）律师事务所——房屋诉讼纠纷案的工作报告',
              '导出范围：2018.02.20-2018.03.20',
              "项目编号：(2015)川民初字第123号\r\n项目名称：房屋诉讼纠纷案\r\n客户名称：平安银行股份有限公司\r\n案由：民间借贷\r\n项目主办：张三丰\r\n项目成员：王二、李四、麻子\r\n立案时间：2018/10/30"]
}
df1 = pd.DataFrame(title, columns=['title'])

df1.style.applymap(lambda x: 'font-family:"等线"').to_excel(excel_writer,
                                                          # df1.to_excel(excel_writer,
                                                          sheet_name='Sheet1',
                                                          header=False,
                                                          index=False,
                                                          startrow=1)

# 正文内容
stage = [
    '一、咨询签约阶段',
    '二、调查取证阶段',
]
task_name = [
    [
        '1、与当事人沟通',
        '2、签订委托材料',
    ],
    [
        '4、test',
    ]
]
task_describe = [
    [
        '委托方式分为三种，一是后收费，二是先收费，三是复合收费',
        '以受害人本人签字为准，否则需要补签。'
    ],
    [
        '123lkjas;ldkfj'
    ]
]
status = [
    [
        '已完成',
        '未完成'
    ],
    [
        '已完成'
    ]
]
assign_date = [
    [
        '2018/08/25',
        '2018/08/26'
    ],
    [
        '2019/01/01'
    ]
]
end_date = [
    [
        '2018/08/25',
        '2018/08/26'
    ],
    [
        '2019/01/01'
    ]
]
finish_date = [
    [
        '2018/09/13',
        '2018/12/14'
    ],
    [
        '2019/01/02'
    ]
]
task_people = [
    [
        """张三丰（1.5h)
王二：(2h)
李麻子：(3h)""",
        """张三丰（1.5h)
王二：(2h)
李麻子：(3h)"""
    ],
    [
        """张三丰（1.5h)
王二：(2h)
李麻子：(3h)"""
    ]
]
totle_wh = [
    [
        '6.5h',
        '6.6h'
    ],
    [
        '3.3h'
    ]
]
comments = [
    [
        '谢小侯爷 2017-12-28 09:30:05\r\n南方日报讯 为贯彻落实中办、国办有关通知精神\r\n谢小侯爷 2017-12-28 09:55:19\r\n我扶贫济困送温暖等活动，关心和保障好贫困户',
        """张三丰 2017-12-28 09:30:05
南方日报讯 为贯彻落实中办、国办有关通知精神，切实做好2018党委、政府要统筹安排好走访慰问、
王麻子 2017-12-28 09:55:20
优抚对象等的基本生活，开展农民工工资支付情况专项检查，严厉打"""
    ],
    [
        """张三丰 2017-12-28 09:30:05
阿三地方"""
    ]
]
document = [
    [
        """案源转化之谈判.key
案源转化之谈判.pptx""",
        """元甲版委托代理合同.docx
全权授权委托书.docx"""
    ],
    [
        '文件.txt'
    ]
]
# '\u2610'　表示方框
check_infos = [
    [
        """□ 禁止夸大承诺，按照话术沟通
□ 好的技术客户
□ 谈判话术较多，详见元甲学院培训课程
□ 好几十""",
        """□ 委托合同3份（盖章后交对方一份），必签，其他几份委托书，可后补
□ 立案授权委托书3份"""
    ],
    [
        '\u2610 洗刷刷'
    ]
]
# 数据准备
data = {
    '任务名称': list(itertools.chain.from_iterable(task_name)),
    '任务描述': list(itertools.chain.from_iterable(task_describe)),
    '状态': list(itertools.chain.from_iterable(status)),
    '指派时间': list(itertools.chain.from_iterable(assign_date)),
    '截止时间': list(itertools.chain.from_iterable(end_date)),
    '完成时间': list(itertools.chain.from_iterable(finish_date)),
    '任务执行人': list(itertools.chain.from_iterable(task_people)),
    '总工时': list(itertools.chain.from_iterable(totle_wh)),
    '评论': list(itertools.chain.from_iterable(comments)),
    '任务附件': list(itertools.chain.from_iterable(document)),
    '任务检查项': list(itertools.chain.from_iterable(check_infos)),
}

# 数据写入
df2 = pd.DataFrame(data, columns=['任务名称', '任务描述', '状态', '指派时间', '截止时间', '完成时间', '任务执行人',
                                  '总工时', '评论', '任务附件', '任务检查项'])

# 格式
df2.style. \
    set_properties(**{'font-family': '等线',
                      'vertical-align': 'middle',  # 垂直对齐方式
                      # 'text-align': 'center',
                      'white-space': 'pre-wrap',  # 自动换行
                      # 'font-style': 'italic',  # 字体样式
                      }). \
    applymap(the_font_color,
             # subset=pd.IndexSlice[0:2]  # 0--2行才做该判断
             ). \
    to_excel(excel_writer,
             # df2.to_excel(excel_writer,
             sheet_name='Sheet1',  # sheet的名字
             # float_format=str,  # 浮点数的格式
             # columns=None,  # 要写的列
             # header=False,  # 布尔值或者字符串列表：要写的列名，如果给出了字符串列表，则假定它是列名的别名
             index=False,  # 布尔值（默认是True），写行名（索引）
             # index_label=None,  # 字符串或列表，默认为None：索引列的列标签。如果给出None，并且header和index为True，则使用索引名称
             startrow=4,  # 起始行向下偏移行数
             startcol=1,  # 起始列向右偏移列数
             # engine=None,  # 使用的引擎：xlsxwriter
             # merge_cells=True,  # 布尔类型：将MultiIndex和Hierarchical Rows写为合并单元格
             # encoding=None,  # 生成excel文件的编码
             # inf_rep='inf',
             # verbose=True,
             # freeze_panes=None,  # 整数元组（长度为2）：指定要冻结的最底行和最右列
             )

workbook = excel_writer.book
worksheet = excel_writer.sheets['Sheet1']

# 第一列合并单元格
statge_format = workbook.add_format()
statge_format.set_font_name('等线')
worksheet.write('A5', '阶段')
begin_row = 6
for index, item in enumerate(task_name, 0):
    rows_len = len(item)
    if rows_len > 1:
        worksheet.merge_range('A{0}:A{1}'.format(begin_row, begin_row + rows_len - 1), stage[index], statge_format)
    else:
        worksheet.write('A{0}'.format(begin_row), stage[index], statge_format)
    begin_row += rows_len

# # 自动换行
# wrap_format = workbook.add_format()
# wrap_format.set_text_wrap()
# worksheet.set_column('A:L', None, wrap_format)

# 设置列宽
worksheet.set_column('A:A', 17)
worksheet.set_column('B:B', 16.88)
worksheet.set_column('C:C', 29.63)
worksheet.set_column('D:D', 8.63)
worksheet.set_column('E:F', 10.88)
worksheet.set_column('G:G', 9.88)
worksheet.set_column('H:H', 15.55)
worksheet.set_column('I:I', 13.25)
worksheet.set_column('J:J', 51.38)
worksheet.set_column('K:K', 23.75)
worksheet.set_column('L:L', 26.38)

# 设置行高
worksheet.set_row(0, 59.25)
worksheet.set_row(1, 43.5)
worksheet.set_row(2, 33)
worksheet.set_row(3, 135.75)

# 垂直方向居中对齐（无效）
row_format = workbook.add_format()
row_format.set_align('vcenter')
row_format.set_align('center')
worksheet.set_row(4, 20, row_format)

# 插入图片
worksheet.insert_image('A1', '27.jpg', {"x_offset": 2, "y_offset": 5, 'x_scale': 1, 'y_scale': 0.25})

excel_writer.save()
print('finish...')
