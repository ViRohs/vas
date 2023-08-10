import os
import json

if os.path.exists("local.py"):
    import local

firebaseConfig = json.loads(os.environ["FIREBASECONFIG"])



import pyrebase

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
storage = firebase.storage()


# 棋譜が存在するかどうか
def exsits_kifu(kifu):
    data = db.child("kifu").order_by_child("id").equal_to(kifu.id).get().val()
    return len(data) > 0

# 棋譜情報を取得
def get_kifu(kifu_id):
    data = list(db.child("kifu").order_by_child("id").equal_to(kifu_id).get().val().items())[0]
    return data

def get_all_kifu():
    data = db.child("kifu").get().val()
    return data

# 棋譜情報をアップロード
def upload_kifu(kifu):
    if exsits_kifu(kifu):
        raise Exception("kifu already exists")
    data = {
        "id":kifu.id,
        "first_player":kifu.first_player,
        "second_player":kifu.second_player,
        "move_count":kifu.move_count,
    }
    #print(data)
    db.child("kifu").push(data)

def upload_image(path):
    storage.child(path).put(path)

# def upload_image(directory,path):
#     storage.child(directory+"/"+path).put(path)


def getimages(kifu_id,move_count):

    image_urls = []
    for i in range(0,move_count+1):
        path = kifu_id+"/"+str(i)+".png"
        image_url = storage.child(path).get_url(None)
        #print(image_url)
        image_urls.append(image_url)

    return image_urls[1:]

    # images = list(storage.child(directory).list_files())
    # print(images[0].name)
    # print(images[0].path)
    # print(images[0].id)
    # print(images[0].self_link)
    # print(images[0].media_link)
    # print(images[0].path_helper)
    # print(images[0].updated)

#upload_image("test.png")
