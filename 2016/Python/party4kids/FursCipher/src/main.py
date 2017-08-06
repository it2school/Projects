#!python3
from vigenere_engine import VigenereEngine
from ceasarus_engine import CeasarusEngine


choise = input("Выберите способ шифрования. \n Введите:\n c - для использования шифра Цезаря.\n v - для использования шифра Виженера.\n")

if(choise=='c'):
    langChoise = input("Выберите язык текста: en - английский, ru - русский, de - немецкий.  ")
    word = input("Напишите фразу, которую хотите зашифровать на выбронном языке: ")   
    shift = int(input("Укажите ключ/сдвиг (число - например: 3) : "))
    ceasarus_engine = CeasarusEngine(shift, langChoise)        
    result =  ceasarus_engine.cipher(word)
    print("Зашифрованный текст:  ", result)

if(choise=='v'): 
    langChoise = input("Выберите язык текста: en - английский, ru - русский, de - немецкий.  ")
    word = input("Напишите фразу, которую хотите зашифровать на выбронном языке: ")  
    keyword = input("Укажите ключевое слово для шифрования на выбранном языке: ")
    engine = VigenereEngine(keyword, langChoise)
    result =  engine.cipher(word)
    print("Зашифрованный текст:  ", result)