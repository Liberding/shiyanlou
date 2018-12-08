import json
import pandas as pd
def analysis(file, user_id):
    try:
        df = pd.read_json(file)
    except ValueError:
        return 0, 0
    df_user_id = df[(df['user_id'] > (int(user_id)-1)) & (df['user_id'] < (int(user_id)+1))]
    #df_user_id_alone = df_user_id['user_id']
    df_minutes_alone = df_user_id['minutes']
    times = df_minutes_alone.count()
    minutes = df_minutes_alone.sum()
    return times, minutes
