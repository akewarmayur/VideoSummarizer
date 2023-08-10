import pandas as pd

col = ['SceneNumber', 'StartTime (Seconds)',
       'StartTime (TimeStamp)', 'EndTime (Seconds)', 'EndTime (TimeStamp)',
       'Path', 'Top3Predictions', 'Score']
res = pd.DataFrame(columns=col)
df = pd.read_csv("xxx.csv")
# print(df.columns)
scene = pd.read_csv("Scenes/scenes1.csv")
# print(scene.columns)

for ind, row in scene.iterrows():
    #df[(df['column1'] > 20) & (df['column2'] < 50)]
    rr = df[(df['StartTime'] >= row['StartTime (Seconds)']) & (df['EndTime'] <= row['EndTime (Seconds)'])]
    # rr = df[(df['StartTime'] >= 0) & (df['EndTime'] <= 44)]
    print(rr['Top3Predictions'].tolist())
    print(rr['Score'].tolist())
    print("_____________________________")
    tmp = [row['SceneNumber'], row['StartTime (Seconds)'],
           row['StartTime (TimeStamp)'], row['EndTime (Seconds)'], row['EndTime (TimeStamp)'],
           row['Path'], "||".join(rr['Top3Predictions'].tolist()),
           "||".join(rr['Score'].tolist())]
    le = len(res)
    res.loc[le] = tmp

res.to_csv("uu.csv")
