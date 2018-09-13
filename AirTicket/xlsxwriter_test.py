import xlsxwriter


workbook = xlsxwriter.Workbook('hello.xlsx')  # excel名
worksheet = workbook.add_worksheet('第一个')  # sheet name

'''
add_format([properties])方法，用于在工作表中创建一个新的格式对象来格式化单元格
properties：为dict类型，为指定一个格式属性的字典
'''
str_format = workbook.add_format({
    'bold': 1,  # 加粗样式
    'border': 1,
    'align': 'center',
})

'''
write.string()：写入字符串类型数据
wirte_number()：写入数字型数据
write_blank()：写入空类型数据
write_formula()：写入公式型数据
write_datetime()：写入日期型数据
wirte_boolean()：写入逻辑型数据
write_url()：写入超链接型数据
'''
worksheet.write('A1', 'Hello World', str_format)
worksheet.write(0, 5, '1 and 1', str_format)


'''
set_row(row, height, cell_format, options)方法，用于设定行单元格的属性
row：指定行位置，起始下标为0；
height：为float类型，设定行高，单位像素；
cell_format：format类型，指定对象格式；
options，字典类型，设置行hidden（隐藏）、level（组合分级）、collpsed（折叠）
'''
worksheet.set_row(0, 50)


'''
set_column(first_col, last_col, width, cell_format, options)方法，用于设置一列或多列单元格的属性
first_col：整型，指定开始列位置，起始下标为0；
last_col：整型，指定结束列位置，起始下标为0；
width：float类型，设置列宽；
cell_format：format类型，指定格式对象；
options：dict类型，设置hidden（隐藏）、level（组合分级）、collpsed（折叠）；
'''
worksheet.set_column(0, 20, 20)


'''
insert_image(row, col, image[, options])方法，用于插入图片到指定的单元格，支持PNG，JPEG，BMP等多种格式。
row：行坐标，起始索引值为0；
col：列坐标，起始索引值为0；
image：string类型，是图片路径；
options：dict类型，是可选参数，用于指定图片位置，如URL等信息；
'''
# 插入图片

'''
chart类
chart类实图表组件，支持包括面积、条形图、柱状图、折线图、散点图等，
一个图表对象是通过Workbook的add_chart方法创建，通过{type, ‘图表类型’}字典来制定图表类型
'''
# 创建一个colum(柱形)图表
# chart = workbook.add_chart({'type': 'column'})
# worksheet.insert_chart(3, 1, chart)

'''
合并单元格
'''
worksheet.merge_range(3, 3, 6, 6, '合并单元格1', str_format)
worksheet.merge_range('B2:C6', '合并单元格2', str_format)

workbook.close()  # 关闭工作表
