import pandas as pd

df = pd.read_csv("xx.csv")
top3predictions = df["Top3Predictions"].tolist()
top3predictionsScore = df["Score"].tolist()
top3predictionsScore1 = [float(i.split(":")[0]) for i in top3predictionsScore]
top3predictionsScore2 = [float(i.split(":")[1]) for i in top3predictionsScore]
print(top3predictions)
print(top3predictionsScore)
top1predictions = []
for i, j in enumerate(top3predictions):
    if top3predictionsScore1[i] >= 0.40:
        top1predictions.append(j.split(":")[0])
    else:
        if top3predictionsScore2[i] >= 0.20:
            top1predictions.append(j.split(":")[1])
        else:
            top1predictions.append(j.split(":")[0])
print(top1predictions)

df1 = pd.read_csv("summary/audioFeatures.csv")
# print(df1)
objects = []
actions = []
nature = []
music = []
for i in top1predictions:
    ee = df1[df1["display_name"] == i]["what"].tolist()[0]
    if ee == "Speech" or ee == "Other":
        prompt = ""
    else:
        if ee == "Music":
            music.append(i)
        elif ee == "Object":
            objects.append(i)
        elif ee == "Action":
            actions.append(i)
        else:
            nature.append(i)

prompt = []
if len(music) != 0:
    prompt.append("The scene has Music playing of " + ", ".join(list(set(music))))
if len(actions) != 0:
    prompt.append("In the scene someone is making a sound of " + ", ".join(list(set(actions))))
if len(objects) != 0:
    prompt.append("The scene has a sound of " + ", ".join(list(set(objects))))
if len(nature) != 0:
    prompt.append("The scene has a nature sound of " + ",".join(list(set(nature))))

final_prompt = ". ".join(prompt)
print(final_prompt)
