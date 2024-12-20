from bson import ObjectId
import pymongo
import os
URL = "mongodb://localhost:27017"

client = pymongo.MongoClient(URL)
db = client["video-manager"]
videos = db["videos"]

print(videos)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def list_all_videos():
    videos_list = videos.find()
    print('-'*50)
    print('# Your videos')
    for video in videos_list:
        print(f"{video['_id']} {video['name']} | {video['time']} |")
    print('-'*50)

def add_video(name,time):
    videos.insert_one({"name":name, "time":time})
    list_all_videos()

def update_video(video_id, name, time):
    videos.update_one(
        {'_id': ObjectId(video_id)},
        {"$set": {'name': name , 'time': time}}
    )
    list_all_videos()

def delete_video(video_id):
    videos.delete_one({'_id': ObjectId(video_id)})
    list_all_videos()

def main():
    while True:
        print("Video Manager with Mongodb | Choose your option")
        print("-"*50)
        print("1. Get All Youtube Videos")
        print("2. Add a youtube video")
        print("3. Update video details")
        print("4. Delete a youtube video")
        print("5. Exit")
        
        
        choice = int(input("Enter your option: "))

        match choice:
            case 1:
                clear_terminal()
                list_all_videos()
            
            case 2:
                clear_terminal()
                name = input("Enter name of video: ")
                time = input("Enter time of video: ")
                
                add_video(name,time)
            
            case 3:
                clear_terminal()
                video_id = input("Enter video id: ")
                name = input("Enter name of video: ")
                time = input("Enter time of video: ")
                update_video(video_id, name,time)

            case 4:
                clear_terminal()
                video_id = input("Enter video id: ")
                delete_video(video_id)

            case 5:
                clear_terminal()
                break

            case _:
                print("Invalid Option")


if __name__ == "__main__":
    main()