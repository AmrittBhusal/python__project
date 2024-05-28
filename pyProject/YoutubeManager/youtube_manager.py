import json
def load_data():
    try:
        with open ('youtube.txt','r')as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_data_helper(videos):
    with open ('youtube.txt','w')as file:
        return json.dump(videos,file)
def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index,video in enumerate(videos,start=1):
        print(f"{index}.{video['name']} Duration:{video['time']}")
    print("\n")
    print("*" * 70)
def Add_videos(videos):
    name = input('Enter your videos:')
    time = input('Enter video time:')
    videos.append({'name':name, 'time':time})
    save_data_helper(videos)
def UPdate_videos(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number to update:"))
    if 1<=index<=len(videos):
        name=input("Enter the new video name:")
        time=input("Enter the new time:")
        videos[index-1]={'name':name,'time':time}
        save_data_helper(videos)
    else:
        print('invalid index selected')
def Delete_videos(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number to be deleted:"))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
def main():
    videos=load_data()
    while True:
        print("\n Youtube Manager | choose an option")
        print("1.List all youtube videos")
        print("2.Add youtube video")
        print("3.Update a youtube video details")
        print("4.Delete a youtube video")
        print("5.Exit the app")
        Choice=input("Enter your choice:")
        # print(videos)

        match Choice:
            case '1':
                list_all_videos(videos)
            case '2':
                Add_videos(videos)
            case '3':
                UPdate_videos(videos)
            case '4':
                Delete_videos(videos)
            case '5':
                break
            case _:
                print("invalid choice")
if __name__ == "__main__":
    main()