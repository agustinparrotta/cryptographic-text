import argparse
import numpy as np
from .utils import *


parser = argparse.ArgumentParser(
    description="""
        Final de Introducción a Python.
        Agustin Parrotta.
        Analisis criptografico de texto.
        Este script cifra o descifra un mensaje mediante el metodo de Cifrado Afin.
        Para cifrar un mensaje, se deben introducir las claves 'a' y 'b'.
        Para descifrar un mensaje, no es necesario introducir 'a' y 'b'.
        Tambien resuelve el ejercicio extra de descifrar mensaje_cifrado_10
        Tambien obtiene los graficos de distribucion de caracteres para los idiomas Español, Ingles, Aleman y Finlandes"""
)
parser.add_argument(
    "modo",
    type=str,
    help="cifrar, descifrar, extra, idiomas",
    choices=["cifrar", "descifrar", "extra", "idiomas"],
)
parser.add_argument(
    "archivo",
    type=str,
    help="Nombre del archivo donde se encuentra el mensaje para cifrar o descifrar",
    nargs="?",
)
parser.add_argument("a", type=int, nargs="?")
parser.add_argument("b", type=int, nargs="?")
args = parser.parse_args()


def exercise():
    fesp = "quijote_es.txt"
    feng = "quijote_en.txt"
    fdeu = "quijote_de.txt"
    ffin = "quijote_fi.txt"

    idiomas = get_language(
        ("Español", fesp), ("Ingles", feng), ("Aleman", fdeu), ("Finlandes", ffin)
    )

    if args.modo == "cifrar":
        msjCifrado = crypt(open_file(args.archivo), args.a, args.b)
        print(
            "El mensaje cifrado con las claves {} y {} es:\n{}".format(
                args.a, args.b, msjCifrado
            )
        )
        msjDescifrado = decrypt_analytical(msjCifrado, args.a, args.b)
        print(
            "El mensaje descifrado con las mismas claves {} y {} es:\n{}".format(
                args.a, args.b, msjDescifrado
            )
        )
    if args.modo == "descifrar":
        decrypt(args.archivo, args.a, args.b, idiomas)
    if args.modo == "extra":
        ejercicioExtra1("mensaje_cifrado_10.txt", idiomas["Español"], "quijote_es.txt")
    if args.modo == "idiomas":
        get_language(
            ("Español", fesp), ("Ingles", feng), ("Aleman", fdeu), ("Finlandes", ffin)
        )


def extra_exercise(file, idioma, fesp):

    mensaje = open_file(file)
    frecEnc = frequency(mensaje)

    dicc = np.arange(27)
    diccEnc = order_list(dicc, frecEnc)
    diccIdioma = order_list(dicc, idioma)

    # Al hacer la distribucion de caracteres del mensaje encriptado, observe que hay dos caracteres muy frecuentes en comparacion al resto. Por esa razon,
    # supuse que era un trabalengua, por lo cual esos dos caracteres tendrian que corresponderse a un espacio y a una vocal

    vocales = [0, 4, 8, 14, 20]
    coef = [0] * len(vocales)
    maximo = [0] * 4

    mensajeIdioma = open_file(fesp)
    masComunesEsp = freq_words(mensajeIdioma)
    masComunesEsp = [x[0] for x in masComunesEsp]

    for i, vocal in enumerate(vocales):
        maximo = try_key(
            maximo, mensaje, masComunesEsp, vocal, diccIdioma[0], diccEnc[0], diccEnc[1]
        )
    print("Las claves son: a={} b={}".format(maximo[0], maximo[1]))
    print("El mensaje es: ", maximo[3])
    return
