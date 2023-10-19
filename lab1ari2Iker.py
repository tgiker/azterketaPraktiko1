# Python 3 code to demonstrate the
# working of MD5 (byte - byte)
 
import hashlib

bilatzenHash = input("Sartu bilatu nahi duzu hash: ")
fitxategiURL = input("Sartu non dagoen fitxategia: ")
fitxategiIzena = input("Sartu fitxategiaren izen orokorra: ")
dokumentuIzena = ""

for i in range(1,47):
    oraingoHash = hashlib.md5(open(fitxategiURL+'\\'+fitxategiIzena+str(i)+'.jpg','rb').read()).hexdigest()
    if (oraingoHash == bilatzenHash):
        print('Hash lortuta! ' + oraingoHash)
        dokumentuIzena = 'imagen' + str(i) + '.jpg'
        print(dokumentuIzena)
        break


print("AMAIERA")