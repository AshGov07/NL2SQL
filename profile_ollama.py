# # profiler.py

# import time


# class Profiler:

#     timings = {}

#     @staticmethod
#     def start(name):

#         Profiler.timings[name] = {
#             "start": time.time()
#         }

#     @staticmethod
#     def stop(name):

#         if name not in Profiler.timings:
#             return

#         Profiler.timings[name]["end"] = time.time()

#         Profiler.timings[name]["elapsed"] = (
#             Profiler.timings[name]["end"]
#             -
#             Profiler.timings[name]["start"]
#         )

#     @staticmethod
#     def get(name):

#         return Profiler.timings.get(
#             name,
#             {}
#         ).get(
#             "elapsed",
#             0
#         )





import time
import requests

MODEL = "qwen3:latest"

start = time.time()

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": MODEL,
        "prompt": "hello",
        "stream": False
    }
)

end = time.time()

print(f"First Call Time: {end-start:.2f} sec")