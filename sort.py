 # import Path 
from pathlib import Path
 
import shutil
import os

import re


#path = r'c:\user\Desktop\Мотлох'
# Таблиця 
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l


def normalize(file):
#  приймає на вхід рядок та повертає рядок;
 new_name = ""
    # здійснює транслітерацію кириличних символів на латиницю;
 new_name  = file.translate(TRANS)               
  # замінює всі символи, крім літер латинського алфавіту та цифр, на символ '_'; 
 new_name  = re.sub(r'\W+','_',new_name)

 return  new_name 
# транслітерація може не відповідати стандарту, але бути читабельною;
# великі літери залишаються великими, а маленькі — маленькими після транслітерації.


def move_files(path):
 # змінюємо назву
   for file in os.listdir(path):
       if file.is_file(): 
        file = os.rename(f'{file }', f'{normalize(file)} ')
    
   razresh = []
   imeges = ['jpeg', 'png', 'jpg', 'svg']
   documents = ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx']
   audio = ['mp3', 'ogg', 'wav', 'amr']
   video = ['avi', 'mp4', 'mov', 'mkv']
   archives = ['zip', 'gz', 'tar']
   Spisok = os.listdir(path)  
   for file in Spisok :
      extension = file.split(".")
      razresh += extension[1]   #збираю всі розширення
       
      if  len(extension) > 1 and extension[1].lower() in imeges :
         old_path = path + file
         new_path = path + "/images/" + file
         shutil.move(old_path,new_path)  
      elif  len(extension) > 1 and extension[1].lower() in documents :
         old_path = path + file
         new_path = path + "/documents/" + file
         shutil.move(old_path,new_path)
      elif  len(extension) > 1 and extension[1].lower() in audio :
         old_path = path + file
         new_path = path + "/audio/" + file
         shutil.move(old_path,new_path)  
      elif  len(extension) > 1 and extension[1].lower() in video :
         old_path = path + file
         new_path = path + "/video/" + file
         shutil.move(old_path,new_path)  
      elif  len(extension) > 1 and extension[1].lower() in archives :
         old_path = path + file
         new_path = path + "/archives/" + file
         shutil.move(old_path,new_path)
   return razresh

# list_vse_razresh = set(razresh) # залишаю лише унікальні розширення
# list_music =  os.listdir( path + "/audio/") 
# list_video = os.listdir('/user/Desktop/Мотлох/video/') 
# list_foto = os.listdir('/user/Desktop/Мотлох/images/') 
# list_doc  = os.listdir('/user/Desktop/Мотлох/documents/') 
# list_archiv =os.listdir('/user/Desktop/Мотлох/archives/') 
# list_neizvestnie = os.listdir('/user/Desktop/Мотлох')

# print ({ 
#               'list_music':  list_music,
#               'list_video': list_video,
#               'list_foto': list_foto,
#               'list_doc': list_doc,
#               'list_archiv': list_archiv,
#               'list_vse_razresh': list_vse_razresh,
#               'list_neizvestnie': list_neizvestnie,
#             })
     
# Список файлів в кожній категорії (музика, відео, фото та ін.)
# Перелік усіх відомих скрипту розширень, які зустрічаються в цільовій папці.
# Перелік всіх розширень, які скрипту невідомі.

path = Path(input('Введіть путь папки : '))
move_files (Path(path)) 