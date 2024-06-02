import sqlite3

conn = sqlite3.connect('youtube_video_db')

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''') 

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        if(len(row) == 0):
            print("No videos found!!!")
            break
        # print(row)
        print(f"{row[0]} : {row[1]} : {row[2]}")

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?,?)", (name, time))
    conn.commit()
    print("Video added successfully!!!")

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()
    print("Video updated successfully!!!")

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id =?", (video_id,))
    conn.commit()
    print("Video deleted successfully!!!")

def main():
    while True:
        print("\n Youtube manage app with DB")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit app")
        choice = input("Enter your choice : ")
        
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter your video name : ")
            time = input("Enter video time : ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter video ID to update : ")
            name = input("Enter your video name : ")
            time = input("Enter video time : ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter video ID to update : ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice!!!")
    
    conn.close()

if __name__ == '__main__':
    main()
