import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_json('user_study.json')
df = data.groupby('user_id').sum().head(100)


def data_plot():
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    
    ax.set_xlabel('User ID')
    ax.set_ylabel('Study Time')
    ax.set_title('StudyData')
    ax.plot(df.index, df.minutes)

    plt.show()
    return ax
if __name__ == '__main__':
    data_plot()
