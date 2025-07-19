import pandas as pd

# 读取Excel文件
# df = pd.read_excel('1读取带中括号的column.xlsx', sheet_name='带中文括号的column')
# df = pd.read_excel('1读取带中括号的column.xlsx')
df = pd.read_excel('~/Downloads/book.xlsx', sheet_name='Sheet1')

# 输出所有列名
# print(df['（）哈哈'])
# print(df)
print(df['（）哈哈'])

# for it in df['（）哈哈']:
#     print(it)

# import pandas as pd
#
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
#
# # 数据载入到 DataFrame 对象
# df = pd.DataFrame(data)
#
# print(df)
# # 返回第一行
# print(df.iloc[0][0])
# # 返回第二行
# print(df.iloc[1])