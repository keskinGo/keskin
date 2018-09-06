import pandas as pd

"""
如果传递现有的ExcelWriter对象，则表单将添加到现有工作簿中
这可用于将不同的DataFrame保存到一个工作簿中
"""

excel_writer = pd.ExcelWriter('test.xlsx')
data = {"project_scope":"1","customer_conflict":[{"search_name":"swartz","conflict_info":[{"pro_main_part_name":"swartz","conflict_num":1,"project_ids":["1535443249371504477"],"conflict_info":["主体冲突"],"project_info":[{"project_id":"1535443249371504477","project_name":"走审批关联子项目后不显示","project_scope":4,"project_status":1,"create_date":"2018-08-28T16:00:49","participants_info":[{"user_id":"1520904869718334248","user_name":"ht8011"},{"user_id":"1520905223879998662","user_name":"黄婷8014"},{"user_id":"1527644338009955682","user_name":"李凤麒"}],"role":"相同方"}],"first_add_time":"2018-08-28T16:00:49"}],"source_role":"原告"}],"project_conflict":{"source_role":"原告","customer_name":"li","conflict_info":[{"project_id":"1535101860060458695","project_name":"法规及规范和健康","project_scope":1,"project_status":6,"create_date":"2018-08-24T17:11:00","participants_info":[{"user_id":"1517465390551671625","user_name":"ht8005"},{"user_id":"1520904869718334248","user_name":"ht8011"},{"user_id":"1520905223879998662","user_name":"黄婷8014"},{"user_id":"1527644338009955682","user_name":"李凤麒"}],"role":"相同方"}]},"report_date":"2018-08-31T10:32:16","report_id":"1535682736711545872"}
df1 = pd.DataFrame(data)
df1.to_excel(excel_writer,
             sheet_name='sheet_name',  # sheet的名字
             float_format=str,  # 浮点数的格式
             columns=None,  # 要写的列
             header=True,  # 布尔值或者字符串列表：要写的列名，如果给出了字符串列表，则假定它是列名的别名
             index=True,  # 布尔值（默认是True），写行名（索引）
             index_label=None,
             startrow=0,
             startcol=0,
             engine=None,
             merge_cells=True,
             encoding=None,
             inf_rep='inf',
             verbose=True,
             freeze_panes=None,  # 整数元组（长度为2）：指定要冻结的最底行和最右列
             )
excel_writer.save()
