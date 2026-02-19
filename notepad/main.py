import json
from datetime import datetime

def save_notes():
    with open("notes.json","w") as file:
        json.dump(notes,file)


def load_notes():
    global notes
    try:
        with open("notes.json","r")as file:
                    notes=json.load(file)
    except:
        notes=[]
    
notes=[]
def add_note(title,content):
    now = datetime.now()
    now.strftime("%Y-%m-%d %H:%M")
    note={"title":title,
    "content":content,
    "date": now.strftime("%Y-%m-%d %H:%M"),
        "update": now.strftime("%Y-%m-%d %H:%M"),
   "important":False}
    notes.append(note)
    save_notes()

def delete_notes(index):
    notes.pop(index)
    save_notes()

def edit_note(index,value1,value2):
    now = datetime.now()
    notes[index]["title"]=value1
    notes[index]["content"]=value2
    notes[index]["update"] = now.strftime("%Y-%m-%d %H:%M")
    save_notes()


def search(keywords):
    found=False
    for note in notes:
        if keywords.lower() in note["title"].lower():
            print(f"{note['title']} | {note['content']} | Done: {note['date']}")
            found = True

    if not found:
        print("not found!")
    


def mark_important(index):
    notes[index]["important"]=True

    save_notes()

def show_note():
    if notes==[]:
        print("empty")

    else:
         for i,note in enumerate(notes):
              print(f"{i} | {note['title']} | {note['content']} | {note['date']}")


def show_important():
    found = False
    for i,note in enumerate(notes):
        if note["important"]:
            print(f"{i} | ⭐ {note['title']} | {note['content']} | {note['date']}")
            found = True
    if not found:
        print("no important notes!")
    save_notes()

def sort_notes(by="date"):
    global notes
    notes.sort(key=lambda x: x[by], reverse=True)
    save_notes()

    save_notes()

load_notes()

while True:
    print("1 add note")
    print("2 delete note")
    print("3 search")
    print("4 show notes")
    print("5 mark important")
    print("6 show important")
    print("7 sort by date")
   
    print("0 exit")
    select=input("select number:")
    
    if select=="1":
        title=input("enter title:")
        content=input("enter content:")
        print("added")
        add_note(title,content)
        

    elif select=="2":
        index = int(input("enter number: "))
        if 0 <= index < len(notes):
            delete_notes(index)
            print("deleted!")
        else:
             print("❌ invalid index!")





    elif select=="3":
         title=input("enter title:")
         search(title)

    elif select == "4":
        show_note()



    elif select=="5":
        index = int(input("enter number: "))
        if 0 <= index < len(notes):
            mark_important(index)
            print("note marked as important ⭐")
        else:
            print("❌ invalid index!")


    elif select=="6":
        show_important()


    elif select=="7":
        sort_notes()
        print("Notes sorted by date ✅")



    elif select == "0":
        break

    else:
        print("invalid choice ❌")
