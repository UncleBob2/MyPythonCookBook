import os
import subprocess


current_path = os.path.dirname(__file__)  # Where your .py file is located
# resource_path = os.path.join(current_path, "Media")  # The resource folder path
# image_path = os.path.join(resource_path, "bubbles")  # The image folder path


print(os.getcwd())
print("current_path", current_path)
# print("resource_path", resource_path)
# print("image_path", image_path)
soundPath1 = os.path.join(current_path, "bounce.wav")
soundPath2 = os.path.join(current_path, "out.wav")
print(soundPath2)

sound1 = subprocess.call(["afplay", soundPath1])
sound2 = subprocess.call(["afplay", soundPath2])
