import random
import time

qSFI = [
    {"q": "who was the last leader of the USSR", "a": "Mikhail S. Gorbachov"},
    {"q": "what alliance did the USSR form in reaction to NATO", "a":"The Warsaw Pact"},
    {"q": "what economic plan for europe was proposed by the united states and what was the USSR's counter", "a":"The Marshall Plan, COMECON"},
    {"q": "who founded the socialist party of peru", "a": "Jose Carlos Mariategui"},
    {"q": "What was the name of the revolutionary organization in peru", "a": "American Popular Revolutionary Alliance"},
    {"q": "Who founded the American Popular Revolutionary Alliance", "a": "Victor Raul Haya de la Torre"},
    {"q": "What mural did Diego Rivera paint as a critique of the United States", "a": "Portrait of America"},
    {"q": "Who invented 'dollar diplomacy'", "a": "William Howard Taft"},
    {"q": "What brizilian leader reformed his country under the slogan, 'Estado Novo'", "a": "Getulio Dornelles Vargas"},
    {"q": "What was the name of the foreign policy created by Franklin D. Roosevelt towards Latin America", "a": "Good Neighbor Policy"},
    {"q": "What Military force did the US train in nicaragua", "a": "Guarda Nacional"},
    {"q": "What nicaraguan dictator rose to power as a consequence of american intervention", "a": "Anastacio Somoza Garcia"},
    {"q": "Who was the leader of the rebel movement in nicaragua featured in Diego Rivera's 'Portrait of America'", "a": "Augusto Cesar Sandino"},
    {"q": "What was the name of the corollary to the Monroe doctrine that sanctioned foreign interventions for the purpose of maintaining stability and preventing the spread of communism", "a": "Roosevelt Corollary"},
    {"q": "What Brazilian Woman was adopted by hollywood in an attempt to better foreign relations/perceptions in the americas", "a": "Carmen Miranda"},
    {"q": "What mascot, modeled after Carmen Miranda was adopted by the United Fruit Company", "a": "Chiquita Banana"},
    {"q": "What was the movement held among indians that emphasized religious differences and called for partition", "a": "Comunalism"},
    {"q": "What Mexican President Nationalized the Mexican Oil Industry", "a": "Lazaro Cardenas"},
    {"q": "What event, also known as the day of direct action, resulted in mass violence between Muslims and Hindus in India", "a": "Calcutta Killing"},
    {"q": "What Conference represented the beginnings of the non-aligned movement in asia and africa", "a": "Bandung Conference"},
    {"q": "What General lead the viet minh during the vietnamese war against france", "a": "Vo Nguyen Giap"},
    {"q": "Where did the final battle of the France-Vietnam War take place", "a": "Dienbienphu"},
    {"q": "What conference following the end of the France-Vietnam war partitioned Vietnam into North and South", "a": "Geneva Conference"},
    {"q": "What US president coined Domino Theory", "a": "Dwight Eisenhower"},
    {"q": "What organization, Also known as the National Liberation Front developed in south vietnam with the aim of overthrowing US control and unifying the country", "a": "Viet Cong"},
    {"q": "What President Furthered US involvement in the vietnam War", "a": "Lyndon B. Johnson"},
    {"q": "What president ended the Vietnam war under the slogan of Vietnamization", "a": "Richard Nixon"}

    ]

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
