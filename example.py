import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio
pio.renderers.default = "colab"

weather_url = "https://www.data.jma.go.jp/obd/stats/data/mdrr/synopday/data1s.html"
df_list = pd.read_html(weather_url)

while True:
    target_id = input("1 - 5の中で数字を選んで")
    if target_id in ["1", "2", "3", "4", "5"]:
        break

    print("1 - 5の数字で入力して")

df = df_list[int(target_id)]

col_name_list = ["気温", "最高気温", "最低気温", "湿度"]
col_list = [3, 6, 8, 12]

df.index = df.iloc[:, 0]
target_df = df.iloc[3:, col_list]
target_df.columns = col_name_list

for col in col_name_list:
    target_df[col] = target_df[col].str.strip(')]')

target_df = target_df.astype('float')
file_name = input("ファイル名を入力")
prefecture_list = target_df.index
target_col = "最高気温"

plot_data = go.Bar(y=prefecture_list,
                   x=target_df.loc[:, target_col], orientation='h')
fig = go.Figure(plot_data)

fig.update_layout(title=target_col, width=700, height=1000)

fig.show()
target_df.to_csv("C:\\develop\\export\\" + file_name + ".csv")
