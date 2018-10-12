import pandas as pd
import datetime
import numpy as np

"""
如果传递现有的ExcelWriter对象，则表单将添加到现有工作簿中
这可用于将不同的DataFrame保存到一个工作簿中
详见https://pandas.pydata.org/pandas-docs/stable/style.html
"""

def red_the_next_month(data, color='red'):
    base_date = datetime.datetime.now() + datetime.timedelta(days=30)
    try:
        d = datetime.datetime.strptime(data, '%Y.%m.%d')
        if d < base_date:
            return 'color: {}'.format(color)
        else:
            return 'color: black'
    except:
        return 'color: black'

excel_writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')
# data = {"project_scope":"1","customer_conflict":[{"search_name":"swartz","conflict_info":[{"pro_main_part_name":"swartz","conflict_num":1,"project_ids":["1535443249371504477"],"conflict_info":["主体冲突"],"project_info":[{"project_id":"1535443249371504477","project_name":"走审批关联子项目后不显示","project_scope":4,"project_status":1,"create_date":"2018-08-28T16:00:49","participants_info":[{"user_id":"1520904869718334248","user_name":"ht8011"},{"user_id":"1520905223879998662","user_name":"黄婷8014"},{"user_id":"1527644338009955682","user_name":"李凤麒"}],"role":"相同方"}],"first_add_time":"2018-08-28T16:00:49"}],"source_role":"原告"}],"project_conflict":{"source_role":"原告","customer_name":"li","conflict_info":[{"project_id":"1535101860060458695","project_name":"法规及规范和健康","project_scope":1,"project_status":6,"create_date":"2018-08-24T17:11:00","participants_info":[{"user_id":"1517465390551671625","user_name":"ht8005"},{"user_id":"1520904869718334248","user_name":"ht8011"},{"user_id":"1520905223879998662","user_name":"黄婷8014"},{"user_id":"1527644338009955682","user_name":"李凤麒"}],"role":"相同方"}]},"report_date":"2018-08-31T10:32:16","report_id":"1535682736711545872"}
# data = {
#     'col1': [1, 2, 3, 4, 5],
#     'col2': ['test', '', '', '', ''],
# }
group_id = [
    '1531209924395021679',
    0,
    '123456asdfasdf',
]
group_name = [
    '湖北华徽律师事务所',
    '事务所',
    'askjdfhkajhslkdjfhkljashdf',
]
group_manager = [
    '张三丰（18200113456）\r\n王二（18200113456）',
    'asdf(123)',
    '356a4sd6f54a65sd4f',
]
group_members = [
    '李飞（18200113456）\r\n郝思四（18200113456）\r\n王万里（18200113456）',
    'asdf ',
    '01 28730417234987 ',
]
add_time = [
    '2017.09.10',
    '2016.12.45',
    '2016.12.20',
]
expiration_time = [
    '2018.9.10',
    '2016.12.31',
    '2019.12.31',
    # datetime.date.today(),
    # datetime.date.today() + datetime.timedelta(days=1),
    # datetime.date.today() + datetime.timedelta(days=2),
]
attr = [
    '团队',
    '',
    '测试',
]
saler = [
    '殷组长',
    'zhou',
    0
]
after_saler = [
    '遥遥大人',
    'li',
    'aslkdfjalksjdf',
]
remark = [
    '赠送2月',
    'null',
    '备注',
]

data = {
    '团队ID': group_id,
    '团队名称': group_name,
    '团队管理员': group_manager,
    '团队成员': group_members,
    '创建时间': add_time,
    '到期时间': expiration_time,
    '属性': attr,
    '销售负责人': saler,
    '售后负责人': after_saler,
    '备注': remark,
}

df1 = pd.DataFrame({'temp': ['法蝉团队信息表']})
df1.to_excel(excel_writer, header=False, index=False)

df2 = pd.DataFrame(data, columns=['团队ID', '团队名称', '团队管理员', '团队成员', '创建时间', '到期时间', '属性', '销售负责人', '售后负责人', '备注'])
df2.style.applymap(red_the_next_month, subset=pd.IndexSlice[0:1]).to_excel(excel_writer,
             sheet_name='Sheet1',  # sheet的名字
             # float_format=str,  # 浮点数的格式
             # columns=None,  # 要写的列
             # header=True,  # 布尔值或者字符串列表：要写的列名，如果给出了字符串列表，则假定它是列名的别名
             index=False,  # 布尔值（默认是True），写行名（索引）
             # index_label=None,  # 字符串或列表，默认为None：索引列的列标签。如果给出None，并且header和index为True，则使用索引名称
             startrow=1,  # 起始行向下偏移行数
             # startcol=0,  # 起始列向右偏移列数
             # engine=None,  # 使用的引擎：xlsxwriter
             # merge_cells=True,  # 布尔类型：将MultiIndex和Hierarchical Rows写为合并单元格
             # encoding=None,  # 生成excel文件的编码
             # inf_rep='inf',
             # verbose=True,
             # freeze_panes=None,  # 整数元组（长度为2）：指定要冻结的最底行和最右列
             )

# workbook = excel_writer.book
# worksheet = excel_writer.sheets['Sheet1']
#
# # 标题格式
# title_format = workbook.add_format()
# title_format.set_bold()
# title_format.set_font_size(40)
# title_format.set_font_name('等线')
# title_format.set_right()
# title_format.set_bottom()
# title_format.set_center_across()  # 中心对齐
#
# worksheet.merge_range('A1:J1', '法蝉团队信息表', title_format)
# worksheet.set_row(0, 43.5)
#
# # # 列名格式
# cols_format = workbook.add_format()
# cols_format.set_bold()
# cols_format.set_font_size(40)
# cols_format.set_font_name('等线')
# # cols_format.set_border()
#
# worksheet.conditional_format('A2:J2',
#                              options={'type': 'no_errors', 'format': cols_format})
#
# # 内容格式
# content_format = workbook.add_format()
# content_format.set_text_wrap()  # 文本换行
# content_format.set_align('left')
# content_format.set_align('vcenter')
# content_format.set_border()
# content_format.set_font_size(40)
# content_format.set_font_color('blue')
#
# red_format = workbook.add_format()
# red_format.set_text_wrap()
# red_format.set_align('left')
# red_format.set_align('vcenter')
# red_format.set_border()
# red_format.set_font_size(40)
# red_format.set_font_color('red')
#
# content_len = len(group_id)
# now = datetime.datetime.now()
#
# worksheet.conditional_format('A3:J{}'.format(content_len+2),
#                              # options={'type': 'cell', 'criteria': '!=', 'value': 0,
#                              options={'type': 'no_errors',
#                                       'format': content_format})
#
# worksheet.conditional_format('A3:J{}'.format(content_len+2),
#                              # options={'type': 'cell', 'criteria': '!=', 'value': 0,
#                              options={'type': 'date',
#                                       'criteria': '>',
#                                       'value': now,
#                                       'format': red_format})
#
# worksheet.conditional_format('A3:J{}'.format(content_len+2),
#                              # options={'type': 'cell', 'criteria': '!=', 'value': 0,
#                              options={'type': 'date',
#                                       'criteria': '<=',
#                                       'value': now,
#                                       'format': red_format})
#
# # for row_num in range(2, 2 + content_len):
# #     worksheet.set_row(row_num, 45, content_format)
#
# worksheet.set_column('A:A', 27.63)
# worksheet.set_column('B:B', 19.63)
# worksheet.set_column('C:C', 20.88)
# worksheet.set_column('D:D', 21.38)
# worksheet.set_column('E:E', 10.5)
# worksheet.set_column('F:F', 10.5)
# worksheet.set_column('G:G', 8.38)
# worksheet.set_column('H:H', 11.63)
# worksheet.set_column('I:I', 11.13)
# worksheet.set_column('J:J', 8.38)

excel_writer.save()
print('finish...')
