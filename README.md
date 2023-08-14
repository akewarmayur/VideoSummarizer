# VideoSummarizer
Summarize any input video or an YouTube link using openAI API, Audio Features and Automatic Speech Recognition(ASR).

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
* input_video : path of the video or YouTube link that you need to summarize
* window : threshold to generate scenes (window 4 is recommended)
* open_api_key : your openAI API key

### Input Video



https://github.com/akewarmayur/VideoSummarizer/assets/31464781/566c5ff3-8d19-4a91-9795-d8e6e03a83ab


### Output
```commandline
A man wearing brown pants is in a scene with loud music playing. There is also a sound of rail transport, vehicle, and gunfire. The man only has 12 bullets and suggests that they should count them down. He then expresses displeasure with the situation, exclaiming "Shit!", "No!", and "F**k!". It has been a bad day for him.
```

#### Errors
* If you get this error `could not find match for ^\w+\W` then, you should go in the cipher.py file in `pytube` and replace the line 30, which is:
`var_regex = re.compile(r"^\w+\W")`
With this line:
`var_regex = re.compile(r"^\$*\w+\W")`


### Future Work:
* Use of Opensource LLM's like Vicuna, LLaMA, Falcon and others instead of openAI LLM

### Contribution
Please mail to **mayurakewar87@gmail.com** if you want to contribute to make the video summarizer better.
