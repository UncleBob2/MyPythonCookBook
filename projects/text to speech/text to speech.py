from gtts import gTTS  # this Google Text to Speech Online Required
import os
import subprocess

data = open("alice.txt", "r")
my_text = data.read().replace("'", "").replace("\n", "").replace("'", "")

language = "en"

output = gTTS(text=my_text, lang=language, slow=False)
data.close()
output.save("alice.mp3")
print("Conversion Completed")

return_code = subprocess.call(["afplay", "alice.mp3"])
