import sqlite3
import os

conn = sqlite3.connect('videos.db')
cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
        )
    '''
    )

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear') 

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?, ?)", (name,time))
    conn.commit()
    list_all_videos()

def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    print("-"*50)
    print("# Your videos \n")
    for row in cursor.fetchall():
        print(f"{row[0]}. {row[1]} | {row[2]} |")
    print("-"*50)

def update_video(video_id, name,time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
    conn.commit()
    list_all_videos()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()
    list_all_videos()

def main():
    while True:
        print("Youtube Manager with Sqlite3 | Choose your option")
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
                video_id = int(input("Enter video id: "))
                name = input("Enter name of video: ")
                time = input("Enter time of video: ")
                update_video(video_id, name,time)

            case 4:
                clear_terminal()
                video_id = int(input("Enter video id: "))
                delete_video(video_id)

            case 5:
                clear_terminal()
                break

            case _:
                print("Invalid Option")

    conn.close()

if __name__ == "__main__":
    main()