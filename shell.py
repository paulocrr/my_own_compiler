import geometry
#Ejecucion del Shell
while True:
    
    text = input('geometry >> ')
    if text.strip() == "": continue
    result, error = geometry.run('<stdin>',text)

    if error: print(error.as_string())
    elif result: print(result)