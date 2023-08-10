import sProcess
import argparse
import shutil
import os

if __name__ == '__main__':
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('-i', '--input_video', action='store', type=str, required=True)
    my_parser.add_argument('-w', '--window', action='store', type=int, required=True)
    my_parser.add_argument('-s', '--open_api_key', action='store', type=str, required=True)
    args = my_parser.parse_args()
    video_path = args.input_video
    window = args.window
    open_api_key = args.open_api_key
    current_directory = os.getcwd()  # Get the current working directory
    destination_file = os.path.join(current_directory, "tmp.mp4")
    shutil.copy(video_path, destination_file)
    obj = sProcess.SummarizeProcess()
    summaryDF = obj.start_process(video_path, open_api_key, window)
    summaryDF.to_csv("videoSummary.csv")
