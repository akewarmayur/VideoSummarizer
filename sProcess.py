import pandas as pd
from sceneDetection.sceneDetection import SceneDetection
from asr.video2asr import ASR
from summary.generateSummary import Summary
from pytube import YouTube


class SummarizeProcess:

    def __int__(self):
        pass

    def download_youtube_video(self, video_url, file_name):
        try:
            youtube = YouTube(video_url)
            stream = youtube.streams.get_highest_resolution()
            file_path = f"tmp.mp4"
            stream.download(output_path="", filename=file_name)
            print("Video downloaded successfully!")
            print("Saved as:", file_path)
        except Exception as e:
            print("An error occurred:", str(e))

    def start_process(self, video_path, api_key, window, link):
        if link:
            file_name = 'tmp.mp4'  # Specify your desired file name
            try:
                self.download_youtube_video(video_path, file_name)
                video_path = 'tmp.mp4'
            except Exception as e:
                print("Exception in downloading youtube video, Please try different link")
        audioFeaturesDF = pd.read_csv("summary/audioFeatures.csv")
        summaryResult = pd.DataFrame(columns=["Scene", "Summary"])
        objScene = SceneDetection()
        objASR = ASR()
        objSummary = Summary()
        sceneswithAF = objScene.detect_scenes(video_path, window, "True")
        """
        ['SceneNumber', 'StartTime (Seconds)',
               'StartTime (TimeStamp)', 'EndTime (Seconds)', 'EndTime (TimeStamp)',
               'Path', 'Top3Predictions', 'Score']
        """
        for ind, row in sceneswithAF.iterrows():
            asrDF = objASR.video2srt(row['Path'])
            text = ":".join(asrDF["Text"].tolist())
            summary = objSummary.generateSummary(api_key, text, sceneswithAF, audioFeaturesDF)
            le = len(summaryResult)
            summaryResult.loc[le] = [row['SceneNumber'], summary]
        return summaryResult
