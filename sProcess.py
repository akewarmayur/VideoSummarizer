import pandas as pd
from sceneDetection.sceneDetection import SceneDetection
from asr.video2asr import ASR
from summary.generateSummary import Summary


class SummarizeProcess:

    def __int__(self):
        pass

    def start_process(self, video_path, api_key, window):
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
