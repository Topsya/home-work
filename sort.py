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

path = Path(input('Введіть путь папки : '))
def normalize(file):
#  приймає на вхід рядок та повертає рядок;
 # new_name = ""
 name = file.split(".")[0]
 exis = file.split(".")[1]
    # здійснює транслітерацію кириличних символів на латиницю;
 new_name  = file.translate(TRANS)               
  # замінює всі символи, крім літер латинського алфавіту та цифр, на символ '_'; 
 ispravl = re.sub(r'\W','_',name)
      #  @"[^\w\.@-]"  "[$|@|&]"
 new_name  = f'{ispravl}.{exis}'
 
 return  new_name 
# транслітерація може не відповідати стандарту, але бути читабельною;
# великі літери залишаються великими, а маленькі — маленькими після транслітерації.


def move_files(path):
 #  print(os.listdir(path))
 # змінюємо назву
   for file in os.listdir(path):
        if os.path.isfile(file): 
          file = os.rename(os.path.join(path, file), os.path.join(path,normalize(file)))
    
   # razresh = []
   imeges = ['jpeg', 'png', 'jpg', 'svg']
   documents = ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx']
   audio = ['mp3', 'ogg', 'wav', 'amr']
   video = ['avi', 'mp4', 'mov', 'mkv']
   archives = ['zip', 'gz', 'tar']
   Spisok_papok = ('imeges','documents','audio','video','archives')
   
   # створюєм папки
   for folder in Spisok_papok:
      if not os.path.exists(f'{path}\\{folder}'):
         os.mkdir(f'{path}\\{folder}')

   Spisok = os.listdir(path)  
   for file in Spisok :
      #  if os.path.isfile(file):
         extension = file.split(".")
            #збираю всі розширення
     # razresh += extension[1]   
       
         if  len(extension) > 1 and extension[1].lower() in imeges :
            old_path = os.path.join(path, file)
            new_path = os.path.join(path,'imeges',file)
            shutil.move(old_path,new_path)  
         elif  len(extension) > 1 and extension[1].lower() in documents :
            old_path = os.path.join(path, file)
            new_path = os.path.join(path,'documents',file)
            shutil.move(old_path,new_path)
         elif  len(extension) > 1 and extension[1].lower() in audio :
            old_path = os.path.join(path, file)
            new_path = os.path.join(path,'audio',file)
            shutil.move(old_path,new_path)  
         elif  len(extension) > 1 and extension[1].lower() in video :
            old_path = os.path.join(path, file)
            new_path = os.path.join(path,'video',file)
            shutil.move(old_path,new_path)  
         elif  len(extension) > 1 and extension[1].lower() in archives :
            old_path = os.path.join(path, file)
            new_path = os.path.join(path,'archives',file)
            shutil.move(old_path,new_path)
    #  return razresh

  # list_vse_razresh = set(razresh) 
# # залишаю лише унікальні розширення
   list_music =  os.listdir(os.path.join(path,'audio')) 
   list_video = os.listdir(os.path.join(path,'video')) 
   list_foto = os.listdir(os.path.join(path,'imeges'))
   list_doc  = os.listdir(os.path.join(path,'documents'))
   list_archiv =os.listdir(os.path.join(path,'archives'))
   list_neizvestnie = path.glob('*.*')

   print ({  
              'list_music':  list_music,
              'list_video': list_video,
              'list_foto': list_foto,
              'list_doc': list_doc,
              'list_archiv': list_archiv,
     #         'list_vse_razresh': list_vse_razresh,
              'list_neizvestnie': list_neizvestnie,
            })
     
# Список файлів в кожній категорії (музика, відео, фото та ін.)
# Перелік усіх відомих скрипту розширень, які зустрічаються в цільовій папці.
# Перелік всіх розширень, які скрипту невідомі.


move_files (path)
