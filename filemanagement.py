import json

def load_data():
    try:
        with open('youtube.txt','r')as file:
           test = json.load(file)
           return test
    except FileNotFoundError:
        return[]
def save_data_helper(videos):
    with open('youtube.txt','w')as file:
        json.dump(videos,file)

        

def  list_all_vidoes(videos):
    print('\n')
    print("*"*70)
    for index , videos in enumerate(videos,start=1):
        print(f"{index}.{videos['name']}, Duration {videos['time']}")
    print('\n')
    print("*"*70)

def add_video(videos):
    name = input("Enter video name : ")
    time = input("Enter video Time : ")
    videos.append({'name':name , 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_vidoes(videos)
    index = int(input("Enter a video number to Update "))
    if 1 <= index <= len(videos):
        name = input("Enter New Video Name : ")
        time = input("Enter New Video Time : ")
        videos[index-1]={'name' : name , 'time' : time}
        save_data_helper(videos)
    else:
        print("Invalid Index!!!")

def delete_video(videos):
    list_all_vidoes(videos)
    index = int(input("Enter the video number that you want to delete : "))

    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("invalid syntax!!!")
    
def main():
    videos = load_data()
    while True:
        print("\nYoutube Management ")
        print("1: List all Youtube Videos ")
        print("2: Add a Youtube Video ")
        print("3: Update a Youtube Video details ")
        print("4: Delete a Youtube Video ")
        print("5: Exit ")
        choice = input("Enter Your Choice : ")
        match choice:
          case '1':
               list_all_vidoes(videos)
          case '2':
               add_video(videos)
          case '3':
               update_video(videos)
          case '4':
               delete_video(videos)
          case '5': 
            break
          case _:
            print("invalid choice")
if  __name__ ==  "__main__":
    main()