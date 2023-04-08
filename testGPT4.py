import openai
import json
import sys

# Encode non-english responses for correct display of characters e.g. Arabic, Urdu etc
sys.stdout.reconfigure(encoding='utf-8')
# keep the api key secret.  Do not disclose to anyone. Better not to hardcode but i am lazy
openai.api_key = "<Your Own API key.  Get it from your Open AI account>"

# first message shall always be in the "role" of "system". Here you provide guiding principals to the model
gpt_messages = [
    {"role": "system", "content":
     """You are virtual assistant.  You will only provide answers if those can not be used to harm or damage
     any individual person, group of people or any business entities"""}
]

while True:  # infinite loop until user enters "bye" as input
    user_input = input("Question: >> ")
    if user_input == "bye":
        print("Ciao !")
        break
    gpt_messages.append({"role": "user", "content": user_input})

    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=gpt_messages
    )
    return_message = str(completion.choices[0].message)
    # Parse JSON data
    parsed_answer = json.loads(return_message)
    # Extract "content" value
    content = parsed_answer['content']
    print(content)
    # append this answer in existing discussion
    gpt_messages.append({"role": "assistant", "content": content})
sys.exit()  # hard exit call to avoid running all the test code written below

# start of test code for image
response = openai.Image.create(
    prompt="3 cars racing and 4th car jumping over them on a flyover",
    n=1,
    size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)
sys.exit()
# end of test code for image
