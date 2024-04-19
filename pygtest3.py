import pygwalker as pyg
import pandas as pd
import matplotlib.pyplot as plt
import io

@pyg.walk
def load_data():
    file_path = pyg.file_upload("Please upload a CSV file.")
    data = pd.read_csv(file_path)
    return data

@pyg.walk
def select_data(data):
    # データをpygwalkerのインターフェース上に散布図として表示
    selected_data = pyg.walk(
        data=data.to_dict(orient='list'),
        x_query="Please click on the x-axis values of the data points you want to select.",
        y_query="Please click on the y-axis values of the data points you want to select.",
        chart_type='scatter',
        x_title='X',
        y_title='Y',
        title='Scatter Plot'
    )
    
    return selected_data

@pyg.walk
def display_graph(data):
    # 選択されたデータをDataFrameに変換
    df_wide = pd.DataFrame(data, columns=['x', 'y'])

    # wide formatからlong formatに変換
    df_long = df_wide.melt(var_name='variable', value_name='value')

    # グラフの作成
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(df_long['variable'], df_long['value'])
    ax.set_xlabel('Variable')
    ax.set_ylabel('Value')
    ax.set_title('Selected Data Points')
    
    # グラフを画像として保存
    img_buffer = io.BytesIO()
    fig.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    
    # 画像をpygwalkerのインターフェース上に表示
    pyg.display(img_buffer)

if __name__ == '__main__':
    pyg.configure(verbose=True)
    data = load_data()
    selected_data = select_data(data)
    display_graph(selected_data)
