import pygwalker as pyg
import pandas as pd
import matplotlib.pyplot as plt

@pyg.walk
def select_data():
    data = pyg.walk(x_query="Please click on the x-axis values of the data points you want to select.",
                    y_query="Please click on the y-axis values of the data points you want to select.")
    return data

@pyg.walk
def display_graph(data):
    # 選択されたデータをDataFrameに変換
    df_wide = pd.DataFrame(data, columns=['x', 'y'])

    # wide formatからlong formatに変換
    df_long = df_wide.melt(var_name='variable', value_name='value')

    # グラフの作成と表示
    plt.figure(figsize=(8, 6))
    plt.scatter(df_long['variable'], df_long['value'])
    plt.xlabel('Variable')
    plt.ylabel('Value')
    plt.title('Selected Data Points')
    plt.show()

    pyg.display()

if __name__ == '__main__':
    data = select_data()
    display_graph(data)
