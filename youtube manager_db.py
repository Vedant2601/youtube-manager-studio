import sqlite3
conn=sqlite3.connect('youtube_videos.db')
cursor=conn.cursor()

cursor.execute('''
            CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL
            )
    ''')



def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
        
def add_video(name, time):
    cursor.execute("INSERT INTO videos(name,time) VALUES(?,?)", (name, time))
    conn.commit()
    print("Video added successfully!")
    
def update_video( video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name=?, time=? WHERE id=?",(new_name, new_time, video_id))
    conn.commit()
    print("Video updated successfully!")
    
def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id=?", (video_id,)) #insert a comma after video_id to make it a tuple
    conn.commit()
    print("Video deleted successfully!")
    
def main():
    
    while True:
        print("\n Welcome to the YouTube Manager app with DB! | Choose an option:")
        print("1. list all Youtube video")
        print("2. Upload Video")
        print("3. update a youtube video details")
        print("4. Delete a Youtube video")
        print("5. Exit the app")
        choice= input("Enter your choice: ")

        if choice == "1":
            list_all_videos()
        elif choice == "2":
            name=input("Enter the title of the video: ")
            time=input("Enter the time of the video: ")
            add_video(name, time)
            print("Video added successfully!")
        elif choice == "3":
            video_id=input("Enter video id to update: ")
            name=input("Enter the title of the video: ")
            time=input("Enter the time of the video: ")
            update_video(video_id,name, time)
        elif choice =="4":
            video_id=input('Enter video id to delete: ')
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please try again.")
    conn.close()

if __name__ == "__main__":
    main()
