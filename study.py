import random
import time

qSFI = []
with open("SFI.txt", "r", encoding="utf-8") as f:
    for line in f:
        # 1. Remove the invisible "newline" at the end
        line = line.strip()
        
        # 2. Skip empty lines so your program doesn't crash
        if not line:
            continue
            
        # 3. Split the line at the pipe symbol
        if "|" in line:
            question, answer = line.split("|")
            
            # 4. Add it to your list as a dictionary
            qSFI.append({"q": question, "a": answer})

qID = [
    {"q": "Ejemplo XXXV", "a": "Don Juan Manuel, Medieval"},
    {"q": "El Romance del Rey Moro" ,"a": "Ano'nimo, Medieval"},
    {"q": "El Lazarillo de tormes", "a": "Ano'nimo, XVI"},
    {"q": "Los Presagios", "a": "Informantes de Sahagu'n, XVI"},
    {"q": "Se ha Perdido el Pueblo Mexicatl", "a": "Ano'nimo(recopilados por Miguel Leo'n-Portilla), XVI"},
    {"q": "Segunda Carta de Relacion", "a": "Herna'n Corte's, XVI"},
    {"q": "Soneto XXII (En tanto que rosa y azucena)", "a": "Garcilaso de la vega, XVI"},
    {"q": "Mientras por Competir con tu cabello", "a": "Go'ngora, XVII, Culteranismo"},
    {"q": "Mire' los muros de la patria mi'a", "a": "Quevedo, XVII, Conceptismo"},
    {"q": "Hombres necio que acusa'is", "a": "Sor Juana Ine's de La Cruz, XVII"},
    {"q": "Don Quijote", "a": "Miguel de Cervantes, XVII"},
    {"q": "El Burlador de Sevilla", "a": "Tirso de Molina, XVII"},
    {"q": "En una Tempestad", "a": "Jose' Mari'a Heredia, XIX"},
    {"q": "Volvera'n las oscuras golondrinas", "a": "Be'quer"},
    {"q": "Las medias rojas", "a": "Emilia Pardo Baza'n"},
    {"q": "San Manuel Bueno, Ma'rtir", "a": "Miguel de Unamuno, gen de 98"},
    {"q": "He Andado Muchos Caminos", "a": "Antonio Machado, gen de 98"},
    {"q": "Nuestra Ame'rica", "a": "Jose' Marti, gen de 98'"},
    {"q": "A Roosevelt", "a": "Rube'n Dari'o, gen de 98"},
    {"q": "El Hijo", "a": "Horacio Quiroga, gen de 98"},
    {"q": "La Casa de Bernarda Alba", "a": "Federico Garci'a Lorca, XX"},
    {"q": "Prendimiento de Antonito el Camborio en el camino a sevilla", "a": "Federico Garci'a Lorca, XX"},
    {"q": "Historia de un Hombre que se convirtio' en perro", "a": "Osvaldo Dragu'n, XX"},
    {"q": "Walking Around", "a": "Pablo Neruda, XX"},
    {"q": "Balada de los dos abuelos", "a": "Nicola's Guille'n, XX"},
    {"q": "Mujer Negra", "a": "Nancy Morejo'n, XX"},
    {"q": "A Julia De Burgos", "a": "Julia de Burgos, XX"},
    {"q": "Peso Ancestral", "a": "Alfonsina Storni, XX"},
    {"q": "Borges y Yo", "a": "Jorge Luis Borges, el Boom"},
    {"q": "El Sur", "a": "Jorge Luis Borges, el Boom"},
    {"q": "No oyes ladrar los perros", "a": "Juan Rulfo, el Boom"},
    {"q": "Chac Mool", "a": "Carlos Fuentes, el Boom"},
    {"q": "La noche boca arriba", "a": "Julio Corta'zar, el Boom"}, 
    {"q": "La siesta del martes", "a": "Gabriel Garci'a Ma'rquez, el Boom"},
    {"q": "El ahogado mas hermoso del mundo", "a": "Gabriel Garci'a Ma'rquez, el Boom"},
    {"q": "Dos Palabras", "a": "Isabel Allende, el Boom"},
    {"q": "El Caballo Mago", "a": "Sabine Ulibarri', contemp"},
    {"q": "Y no se lo trago la tierra", "a": "Toma's Rivera, contemp"},
    {"q": "La Noche Buena", "a": "Toma's Rivera, contemp"},
    {"q": "Como la vida misma", "a": "Rosa Montero"}
    ]

mAPSL = {
    "ACC" : "acc",
    "ID"  : qID,
    "VOC" : "voc"
        }
mAPW = {
    "SFI" : qSFI,
    "T"   : "t"
        }
m1 = {
    "APW"  : mAPW,
    "APSL" : mAPSL
        }

state = m1



while(state != "quit"):
    if isinstance(state, dict):
        for opt in state:
            print(opt)
    
    inp = input(">")

    if isinstance(state, dict):
        if inp in state:
            state = state[inp]
    
    if isinstance(state, list):
        random.shuffle(state)
        start_time = time.time()
        score = 0
        for card in state:
            print("\n" + "="*20)
            user_answer = input(card["q"] + "\n> ")
            
            #clear screen
            print("\033[H\033[J", end="")

            # .strip() removes accidental spaces, .lower() ignores Capitalization
            if user_answer.strip().lower() == card["a"].lower():
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong. The answer was: {card['a']}")
                   
        end_time = time.time()
        print(f"\nFinished! Final Score: {score}/{len(state)} Time: {end_time-start_time}")
