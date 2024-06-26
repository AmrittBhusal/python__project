import sqlite3
con=sqlite3.connect('youtube.db')
cursor=con.cursor()
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
def add_videos(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES(?,?)",(name,time))
    con.commit()
def update_videos(video_id,new_name,new_time):
    cursor.execute("UPDATE videos set name=?,time=? where id=?",(new_name,new_time,video_id))
    con.commit()  
def delete_videos(delete_id):
    cursor.execute("DELETE FROM videos where id=?",(delete_id,))
    con.commit()
def main():
    while True:
        print("\n Youtube manager with DB|Choose an option")
        print("1.List all videos")
        print("2.Add videos")
        print("3.Update videos")
        print("4.Delete videos")
        print("5.Exit")
        choice=input("Enter your choice:")

        if choice=='1':
            list_all_videos()
        elif choice=='2':
            name=input("Enter the new video name:")
            time=input("Enter the new time:")
            add_videos(name,time)
        elif choice=='3':
            video_id=input("Enter the video number to updated: ")
            name=input("Enter the new update video name:")
            time=input("Enter the new update time:")
            update_videos(video_id,name,time)
        elif choice=='4':
            delete_id=input("Enter the video number to be delete:")
            delete_videos(delete_id)
        elif choice=='5':
            break
        else:
            print("invalid choice")

    con.close(  )
if __name__=="__main__":
    main()