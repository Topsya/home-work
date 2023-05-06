from importlib.metadata import files
import shutil
import os
import re
import sys
import Path 

# Таблиця 
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l


def normalize():
#  приймає на вхід рядок та повертає рядок;
 new_name = ""
    # здійснює транслітерацію кириличних символів на латиницю;
 new_name  = file.translate(TRANS)               
  # замінює всі символи, крім літер латинського алфавіту та цифр, на символ '_'; 
 new_name  = re.sub(r'\W+','_',new_name)

 return  new_name 
# транслітерація може не відповідати стандарту, але бути читабельною;
# великі літери залишаються великими, а маленькі — маленькими після транслітерації.


# потрібно запустити скрипт командою python sort.py /user/Desktop/Мотлох
# os.rename('filename.txt', 'new_filename.txt')
 # sorter_files(Motloh):  
from pathlib import Path 
papka = Path("/user/Desktop/Мотлох")
def rename():
    for file in os.listdir(papka):
       if file.is_file(): 
        file = os.rename(f'{file }', f'{normalize(file)} ')
    return   file 
               
   
def move_files():
  
   imeges = ['jpeg', 'png', 'jpg', 'svg']
   documents = ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx']
   audio = ['mp3', 'ogg', 'wav', 'amr']
   video = ['avi', 'mp4', 'mov', 'mkv']
   archives = ['zip', 'gz', 'tar']
   fails = os.listdir("/user/Desktop/Мотлох")  
   for file in files :
      extension = file.split(".")
      razresh = []
      razresh += extension[1]
      list_vse_razresh = list(set(razresh))  
      if  len(extension) > 1 and extension[1].lower() in imeges :
         old_path = r'/user/Desktop/Мотлох' + file
         new_path = r'/user/Desktop/Мотлох' + "/images/" + file
         shutil.move(old_path,new_path)  
      elif  len(extension) > 1 and extension[1].lower() in documents :
         old_path = r'/user/Desktop/Мотлох' + file
         new_path = r'/user/Desktop/Мотлох' + "/documents/" + file
         shutil.move(old_path,new_path)
      elif  len(extension) > 1 and extension[1].lower() in audio :
         old_path = r'/user/Desktop/Мотлох' + file
         new_path = r'/user/Desktop/Мотлох' + "/audio/" + file
         shutil.move(old_path,new_path)  
      elif  len(extension) > 1 and extension[1].lower() in video :
         old_path = r'/user/Desktop/Мотлох' + file
         new_path = r'/user/Desktop/Мотлох' + "/video/" + file
         shutil.move(old_path,new_path)  
      elif  len(extension) > 1 and extension[1].lower() in archives :
         old_path = r'/user/Desktop/Мотлох' + file
         new_path = r'/user/Desktop/Мотлох' + "/archives/" + file
         shutil.move(old_path,new_path)


list_music =  os.listdir('/user/Desktop/Мотлох/audio/') 
list_video = os.listdir('/user/Desktop/Мотлох/video/') 
list_foto = os.listdir('/user/Desktop/Мотлох/images/') 
list_doc  = os.listdir('/user/Desktop/Мотлох/documents/') 
list_archiv =os.listdir('/user/Desktop/Мотлох/archives/') 
list_neizvestnie = os.listdir('/user/Desktop/Мотлох') 

print ({ 
              'list_music':  list_music,
              'list_video': list_video,
              'list_foto': list_foto,
              'list_doc': list_doc,
              'list_archiv': list_archiv,
              'list_vse_razresh': list_vse_razresh,
              'list_neizvestnie': list_neizvestnie,
            })
    
# Список файлів в кожній категорії (музика, відео, фото та ін.)
# Перелік усіх відомих скрипту розширень, які зустрічаються в цільовій папці.
# Перелік всіх розширень, які скрипту невідомі.