import pandas as pd
url = 'http://mops.twse.com.tw/server-java/t164sb01?step=1&CO_ID=1216&SYEAR=2017&SSEASON=1&REPORT_ID=C' ## 公開資訊觀測站的財報
dfs = pd.read_html(url) ## 回傳DataFrame類別的陣列
df = dfs[1]
print(df)
print('------------------------------')
# 簡單的操作pandas教學
## 只查看前面五行
print(df.head(5))
print('------------------------------')
# 查看所有的columns
columns = df.columns
print(columns)
print('------------------------------')
## 僅查看取特定column
showColumns = [columns[0], columns[1]]
print(df[showColumns].head())
print('------------------------------')
## 僅查看特定的row
print(df.xs(5))  ##不可指派內容
print(df.loc[5])  ##可指派內容
print('------------------------------')
## 存檔
df.to_csv('{csv-IFRS單一公司案例文件預覽及下載}', index=False)
df.to_json('{json-IFRS單一公司案例文件預覽及下載}')