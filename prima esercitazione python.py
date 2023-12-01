def perimetro_quadrato(lato): 
    return lato * 4

print("calcolare il perimetro del quadrato")
lato = int(input("inserisci la lunghezza del lato del quadrato: "))
perimetro = perimetro_quadrato(lato)
print(f"il perimetro del quadrato è: {perimetro}")

def perimetro_del_cerchio(raggio):
    return 2 * 3.14* raggio
print("calcolare il perimetro del cerchio")
raggio = float(input("inserire il raggio del cerchio: "))
perimetro = perimetro_del_cerchio(raggio)
print(f"il perimetro del cerchio è: {perimetro}")

def perimetro_del_rettangolo(base,altezza):
    return 2 * (base + altezza)
print("calcolare il perimetro del rettangolo")
base= int(input("inserire la base del rettangolo: "))
altezza = int(input("inserire l'altezza del rettangolo: "))
perimetro = perimetro_del_rettangolo(base, altezza)
print(f"il perimetro del rettangolo è: {perimetro}")
