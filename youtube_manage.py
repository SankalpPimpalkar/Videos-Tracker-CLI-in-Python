import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("-"*50)
    print("# Your videos \n")
    for index,video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} duration: {video['time']}")
    print("-"*50)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name':name, 'time':time})
    save_data(videos)
    list_all_videos(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video number to update: "))

    if 1 <= index <= len(videos):
        new_name = input("Enter updated name for video: ")
        new_time = input("Enter updated time for video: ")
        
        videos[index - 1] = {'name': new_name, 'time': new_time}
        save_data(videos)
        list_all_videos(videos)
        
    else:
        print("Enter valid video number")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video number to delete: "))
    
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data(videos)
        list_all_videos(videos)
        
    else:
        print("Enter valid video number")

def main():
    videos = load_data()

    while True:
        print("Youtube Manager | Choose your option")
        print("1. Get All Youtube Videos")
        print("2. Add a youtube video")
        print("3. Update video details")
        print("4. Delete a youtube video")
        print("5. Exit")
        
        choice = int(input("Enter your option: "))

        match choice:
            case 1:
                list_all_videos(videos)
            
            case 2:
                add_video(videos)
            
            case 3:
                update_video(videos)

            case 4:
                delete_video(videos)

            case 5:
                break

            case _:
                print("Invalid Option")

if __name__ == "__main__":
    main()