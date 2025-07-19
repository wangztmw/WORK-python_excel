import re

str = "北京, 西瓜，晴天, 白天，不要去散步"

# 使用正则表达式进行分词
split_result = re.split(r'[，, ]', str)
# 打印分词结果
print(split_result)

if "晴天" in split_result:
    print("晴天")


import pandas as pd

# 示例DataFrame
df = pd.DataFrame({
    'city': ['北京', '上海', '广州'],
    'weather': ['晴天', None, '雨天']
})

# 转换weather列为字符串列表
# weather_list = df['weather'].fillna('').astype(str).tolist()
# weather_list = df['weather'].fillna('').tolist()
weather_list = df['weather'].tolist()
print(weather_list)  # 输出：['晴天', '', '雨天']

# 临时将df表格作为数组进行判断
if '晴天' in list(df['weather']):
    print("临时将df作为数据进行分析：可行！")

if '晴天' in df['weather']:
    print("将df作为数据进行分析：可行！")
else:
    print("直接使用df表格进行in分析则不行！")