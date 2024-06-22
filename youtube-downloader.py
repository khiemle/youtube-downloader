from pytube import YouTube
from sys import argv

def convertToMB(bytes):
    return round(bytes / 1024 / 1024, 2)

def isResolutionHigherThan720(stream):
    return int(stream.resolution[0:len(stream.resolution) - 1]) > 720

def on_complete(stream, file_handle):
    if file_handle is not None:
        print("Download complete")
    else:
        print("Download failed")
def on_progress(stream, chunk, bytes_remaining):
    print(f"Downloading... {convertToMB(bytes_remaining)} MB remaining")

link = argv[1]
yt = YouTube(link)
yt.register_on_complete_callback(on_complete)
yt.register_on_progress_callback(on_progress)
print(f"Title: {yt.title}")
print(f"Number of views: {yt.views}")
print(f"Length of video: {yt.length} seconds")
print(f"Rating: {yt.rating}")
print(f"Description: {yt.description}")

# Create a list to store the streams
stream_list = []
videoStreams = yt.streams.filter(only_video=True).order_by('resolution').desc()
for i, stream in enumerate(videoStreams):
    if isResolutionHigherThan720(stream):
        print(f'{i+1}. Resolution = {stream.resolution} - {stream.mime_type} - {stream.type} - {convertToMB(stream.filesize)} MB')
        stream_list.append(stream)

selection = int(input("Enter the number of the stream you want to download: ")) - 1

yd = stream_list[selection]
yd.download(f"Downloads/")






