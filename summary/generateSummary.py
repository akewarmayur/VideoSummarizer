import openai


class Summary:

    def get_prompt(self, text, audioPredictionDF, audioFeaturesDF):
        top3predictions = audioPredictionDF["Top3Predictions"].tolist()[0].split("||")
        top3predictionsScore = audioPredictionDF["Score"].tolist()[0].split("||")
        top3predictionsScore1 = [float(i.split(":")[0]) for i in top3predictionsScore]
        top3predictionsScore2 = [float(i.split(":")[1]) for i in top3predictionsScore]
        top1predictions = []
        for i, j in enumerate(top3predictions):
            if top3predictionsScore1[i] >= 0.40:
                top1predictions.append(j.split(":")[0])
            else:
                if top3predictionsScore2[i] >= 0.20:
                    top1predictions.append(j.split(":")[1])
                else:
                    top1predictions.append(j.split(":")[0])
        objects = []
        actions = []
        nature = []
        music = []
        for i in top1predictions:
            ee = audioFeaturesDF[audioFeaturesDF["display_name"] == i]["what"].tolist()[0]
            if ee == "Speech" or ee == "Other":
                pass
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
        objects = ". ".join(prompt)
        prefix = ("you are a scene summarizer. Give summary of the given scene in easy to understand language that "
                  "contains all the necessary details.")
        prompt = f"{prefix} {objects}. Now directly summarize the following passage: {text}"
        return prompt

    def processText(self, text):
        text = text.replace('"', "'")
        text = text.replace(':', " ")
        return text

    def generateSummary(self, api_key, text, audioPredictionDF, audioFeaturesDF):
        # Initialize the OpenAI API client
        openai.api_key = api_key

        # Define a prompt for the conversation
        text = self.processText(text)
        prompt = self.get_prompt(text, audioPredictionDF, audioFeaturesDF)

        # Call the OpenAI API to generate a response
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can choose a different engine if needed
            prompt=prompt,
            max_tokens=2000  # Adjust the max_tokens parameter as needed
        )
        # Print the generated response
        summary = response.choices[0].text.strip()
        return summary


# obj = Summary()
# import pandas as pd
# text = "iuiu"
# audioPredictionDF = pd.read_csv("uu.csv")
# audioFeaturesDF = pd.read_csv("audioFeatures.csv")
# ss = obj.get_prompt(text, audioPredictionDF, audioFeaturesDF)
# print(ss)