# import pandas as pd
#
# col = ['SceneNumber', 'StartTime (Seconds)',
#        'StartTime (TimeStamp)', 'EndTime (Seconds)', 'EndTime (TimeStamp)',
#        'Path', 'Top3Predictions', 'Score']
# res = pd.DataFrame(columns=col)
# df = pd.read_csv("xxx.csv")
# # print(df.columns)
# scene = pd.read_csv("Scenes/scenes1.csv")
# # print(scene.columns)
#
# for ind, row in scene.iterrows():
#     #df[(df['column1'] > 20) & (df['column2'] < 50)]
#     rr = df[(df['StartTime'] >= row['StartTime (Seconds)']) & (df['EndTime'] <= row['EndTime (Seconds)'])]
#     # rr = df[(df['StartTime'] >= 0) & (df['EndTime'] <= 44)]
#     print(rr['Top3Predictions'].tolist())
#     print(rr['Score'].tolist())
#     print("_____________________________")
#     tmp = [row['SceneNumber'], row['StartTime (Seconds)'],
#            row['StartTime (TimeStamp)'], row['EndTime (Seconds)'], row['EndTime (TimeStamp)'],
#            row['Path'], "||".join(rr['Top3Predictions'].tolist()),
#            "||".join(rr['Score'].tolist())]
#     le = len(res)
#     res.loc[le] = tmp
#
# res.to_csv("uu.csv")




from pytube import YouTube

def download_youtube_video(video_url, file_name):
    try:
        youtube = YouTube(video_url)
        stream = youtube.streams.get_highest_resolution()
        file_path = f"tmp.mp4"
        stream.download(output_path="", filename=file_name)
        print("Video downloaded successfully!")
        print("Saved as:", file_path)
    except Exception as e:
        print("An error occurred:", str(e))

def main():
    video_url = 'https://www.youtube.com/watch?v=vf1TgInvRVE'
    file_name = 'tmp.mp4'  # Specify your desired file name
    download_path = 'Scenes'

    download_youtube_video(video_url, file_name)

if __name__ == "__main__":
    main()


