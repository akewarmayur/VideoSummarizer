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
    obj = sProcess.SummarizeProcess()
    link = False
    video_extensions = ['.mp4', '.avi', '.mkv', '.mov']  # Add more extensions as needed
    if not any(video_path.lower().endswith(ext) for ext in video_extensions):
        link = True
        summaryDF = obj.start_process(video_path, open_api_key, window, link)
        summaryDF.to_csv("videoSummary.csv")
    else:
        current_directory = os.getcwd()  # Get the current working directory
        destination_file = os.path.join(current_directory, "tmp.mp4")
        shutil.copy(video_path, destination_file)
        summaryDF = obj.start_process("tmp.mp4", open_api_key, window, link)
        summaryDF.to_csv("videoSummary.csv")
