from PIL import Image
import os


# Переименование фото файлов
for f in os.listdir("../Alum_App/all"):
    if f.endswith(".jpg"):
        i = Image.open(f)

        fn, fext = os.path.splitext(f)
        i.save("300/all_"+f+"".format(fn, fext))