path = input("\nEnter Destination Path: ")
option = input("Please Press L for Low Quality and for High Quality Press H: ")
def Low(video):
    Video_Low_Quality=video.streams[0]
    print("\nTitle:",Video_Low_Quality.title)
    print("Video Size:",(int(Video_Low_Quality.get_filesize())//1024)//1024,"MB")
    print("Video Resolution:",Video_Low_Quality.resolution)
    print("Video Extension:",Video_Low_Quality.extension)
    print("\nDownloading Progress...\n")
    Video_Low_Quality.download(filepath=path)  # downloading start at resuming
    print("\nDownload Complete...\n")

def High(video):
    Video_High_Quality=video.streams[1]
    print("\nTitle:",Video_High_Quality.title)
    print("Video Size:",(int(Video_High_Quality.get_filesize())//1024)//1024,"MB")
    print("Video Resolution:",Video_High_Quality.resolution)
    print("Video Extension:",Video_High_Quality.extension)
    print("\nDownloading Progress...\n")
    Video_High_Quality.download(filepath=path)  # downloading start at resuming
    print("\nDownload Complete...\n")

try:
    f = open("Link.txt", "r")
    for i in f.read().split("\n"):
        import pafy
        url = i
        video = pafy.new(url)
        if option == 'l' or option == "L":
            Low(video)
        elif option == 'h' or option == "H":
            High(video)
        else:
            print("Please press correct key and select video quality")
            break
except ValueError:
    print("\nPlease Paste Youtube Video Link on Link.txt File\nBecause Link.txt File is Empty")