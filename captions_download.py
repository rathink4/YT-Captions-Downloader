import os
import sys
from youtube_transcript_api import YouTubeTranscriptApi

def createTextFile(video_id, dest):
    '''
    Every youtube video has the following url
    E.g. - https://www.youtube.com/watch?v=Gjnup-PuquQ

    Now the id for the video is the string after ?v= (in this example - Gjnup-PuquQ)

    Hence, using the .get_transcript() method, you can get a list of dictionaries.

    The result returned is dictionary with the following key-value pair: -
    text : caption (string)
    start : display start time (num)
    duration: how long the caption is displayed (num)

    '''

    # You can pass multiple video ids to this method to get transcripts of multiple videos
    srt = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
    file = os.path.join(dest, video_id+".txt")

    with open(file, "w") as f:
        for i in srt:
            f.write(i["text"]+"\n")


def createDirectory(dest):
    if not os.path.exists(dest):
        os.mkdir(dest)

def main(url):
    start_index = url.find("?v=")
    start_index += 3
    video_id = url[start_index:]
    dest = os.path.join(os.getcwd(), "Texts")
    createDirectory(dest)
    createTextFile(video_id, dest)


if __name__ == '__main__':
    args = sys.argv

    if len(args) != 2:
        raise Exception("Pass the url which you want the caption for")
    
    url = args[1]
    main(url)