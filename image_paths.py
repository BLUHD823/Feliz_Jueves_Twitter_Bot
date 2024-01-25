import json
json_path = 'data_image.json'

def open_json(json_path):
    with open(json_path,'r') as archivo:
        datos = json.load(archivo)
        return datos

def get_path(datos,number):
    for paths in datos:
        for name,path in paths.items():
            if 1 <= number <= 9:
                title = "image_" + str(number)
                if name == title:
                    image_path = path
                    return image_path
            
