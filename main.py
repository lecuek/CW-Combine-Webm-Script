import os
from datetime import datetime
import random, string
def list_webm_files(directory):
    webm_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".webm"):
                filepath = os.path.join(root, file)
                modified_time = os.path.getmtime(filepath)
                webm_files.append((filepath, modified_time))
    # Sort files by modified time
    webm_files.sort(key=lambda x: x[1])
    return webm_files

def generate_ffmpeg_concat_string(webm_files):
    concat_string = ""
    for file, _ in webm_files:
        concat_string += f"file '{file}'\n"
    return concat_string

if __name__ == "__main__":
    print("Enter directory to be scanned :")
    current_directory = input()
    webm_files = list_webm_files(current_directory)
    if webm_files:
        ffmpeg_concat_string = generate_ffmpeg_concat_string(webm_files)
        print(ffmpeg_concat_string)
        filename = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        if os.path.exists(filename+".txt") :
            f = open(filename+".txt", "a")
            f.truncate(0)
            f.close()
        f = open(filename+".txt", "x")
        print(f"{filename+".txt"} created, writing contents")
        f.writelines(ffmpeg_concat_string)
        print("wrote", ffmpeg_concat_string)
        f.close()
        print("Successfully gathered the files")
        print("ffmpeg command line : ", f"ffmpeg -f concat -safe 0 -i {filename}.txt -c copy {filename}.webm")

    else:
        print("No .webm files found in said directory and subdirectories.")