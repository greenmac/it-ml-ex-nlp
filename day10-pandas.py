import pandas as pd

# df = pd.read_csv("<file_path>") # 讀取csv
# df = pd.read_json("{json-IFRS單一公司案例文件預覽及下載}") # 讀取json
# dfs = pd.read_html("<url or html text>") # 讀取pandas
# print(df)

# code_string = """ {'brand_name': nan,
#   'category_name': 'Home/Home Décor/Home Décor Accents',
#   'name': 'Leather Horse Statues',
#   'price': 35,
#   'shipping': 1}"""
# target_dict = eval(code_string)

# df = pd.DataFrame("<dist_variable_name>") # DataFrame 讀取 pandas

# 寫成csv檔
# df.to_csv('<file_path>', index=False, encoding='utf8') # index不寫上的話，很有可能下次讀檔近來他又幫你重建索引，所以一般我會習慣這樣寫，encoding則是因為中文版windows預設編碼回cp950(真的很討厭)，有一些字彙無法透過這個編碼儲存，像是"喆"或是"Naïve"中間那個有兩個點的i。

# 寫成json檔
# df.to_json('<file_path>', encoding='utf8')

#轉成python中的dist格式
# list(df.T.to_dict().values())