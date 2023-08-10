# VideoSummarizer
Summarize any input video using openAI API, Audio Features and Automatic Speech Recognition(ASR).

## Process
* Generate scenes from video using audio features
* Generate speech from each scene using ASR
* Pass the ASR and the generated audio features to openAI LLM and get the summary

#### You need to openAI API key to summarize video.
Get it from [here](https://platform.openai.com/account/api-keys)

### Quick Start
```commandline
python main.py --input_video "your_video" --window 4 --open_api_key "your_key"
```
* input_video : path of the video that you need to summarize
* window : threshold to generate scenes (window 4 is recommended)
* open_api_key : your openAI API key

### Input Video


### Output
```commandline
A man wearing brown pants is in a scene with loud music playing. There is also a sound of rail transport, vehicle, and gunfire. The man only has 12 bullets and suggests that they should count them down. He then expresses displeasure with the situation, exclaiming "Shit!", "No!", and "F**k!". It has been a bad day for him.
```

### Future Work:
* Process YouTube video link
* Addition of Image Features
* Use of Opensource LLM's like Vicuna, LLaMA, Falcon and others instead of openAI LLM

### Contribution
Please mail to **mayurakewar87@gmail.com** if you want to contribute to make the video summarizer better.