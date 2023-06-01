import urllib.parse
import requests
import os

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "XiRadxbqqzSEAAt8bNoajRBagtFJjLqU" #Replace with your MapQuest key

def limpiar_consola():
    if os.name == "nt": #Windows
        os.system("cls")
    else: #Mac o Linux
        os.system("clear")

def call_number():
    while True:
        try:
            entrada = input("Ingresa el Valor: ")
            if entrada.isdigit():
                numero = int(entrada)
                return numero
            else:
                raise ValueError("Error. Ingresaste texto en vez de un numero")
        except ValueError as error:
            print(error)



while True:
    while True:
        orig = input("Starting Location: ")
        dest = input("Destination: ")
        print("Consumo del Vehiculo [Km/L]: ")
        kmveh = call_number()
        
        url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
        print("URL: " + (url))
        json_data = requests.get(url).json()
        json_status = json_data["info"]["statuscode"]
        if json_status == 0:
            print("API Status: " + str(json_status) + " = A successful route call.\n")
            break
        else:
            print("A ocurrido un error al parecer. Intentalo nuevamente")

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
    
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel [Km/L] " + str(kmveh))
        print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["distance"])/kmveh)))
        print("=============================================")
    
        #Narrativa del viaje
        #for each in json_data["route"]["legs"][0]["maneuvers"]:
        #    print(each)
            
    print("\n\nQuiere Buscar otra ubicacion: \n1) Si\n2) No")
    opc = call_number()
    if opc == 2:
        break
    else:
        limpiar_consola()
