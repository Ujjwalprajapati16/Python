from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://<userna,e>:<password>@cluster0.frdknt4.mongodb.net/")
# I have to remove url before uploding code in githun
 
db = client["ytmanager"]
video_collection = db["videos"]

# print(video_collection)

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, new_name, new_time):
    video_collection.update_one({'_id':ObjectId(video_id)},{"$set": {"name": new_name, "time": new_time}})

def delete_video(video_id):
    video_collection.delete_one({'_id': ObjectId(video_id)})
    # have to fix this

def main():
    while True:
        print("\n Youtube manage app with DB")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit app")
        choice = input("Enter your choice: ")
        # print(videos)
        
        match choice:
            case "1":
                list_videos()
            case "2":
                name = input("Enter the video name : ")
                time = input("Enter the video time : ")
                add_video(name, time)
            case "3":
                video_id = input("Enter the video id : ")
                name = input("Enter the updated video name : ")
                time = input("Enter the updated video time : ")
                update_video(video_id, name, time)
            case "4":
                video_id = input("Enter the video id : ")
                delete_video(video_id)
            case "5":
                print("Exit the app")
                break
            case _:
                print("Invalid choice!!!")
                

if __name__ == "__main__":
    main()