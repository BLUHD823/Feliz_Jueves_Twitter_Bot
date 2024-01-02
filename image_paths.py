import json
json_path = 'data_image.json'

def open_json(json_path):
    with open(json_path,'r') as archivo:
        datos = json.load(archivo)
        return datos

def get_path(datos,number):
    for paths in datos:
        for name,path in paths.items():
            #print(f"{name}:{path}")
            if number in[1,2,3,4] :
                title = "image_"+ str(number)
                if name == title:
                    image_path = path
                    return image_path
            elif number in[5,6,7]:
                title = "image_" + str(number)
                if name == title:
                    image_path = path
                    return image_path
            
