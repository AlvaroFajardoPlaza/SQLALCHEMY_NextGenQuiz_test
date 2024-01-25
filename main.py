#### ESTE ES EL ARCHIVO PRINCIPAL DE NUESTRO PROYECTO ####
import sys
import db


from models import Category
from scrapper_bot_01.bot_01 import scrappeCategories, scrappeQuestionsAndAnswers, categorizingQuestions, randomTriviaTest, categorizedTriviaTest


#### FUNCION DE PRUEBA --> CATEGORIAS
def createCategories():
    cat1 = Category("geography")
    cat2 = Category("history")
    cat3 = Category("science")

    category_list = [cat1, cat2, cat3]
    # Mandamos los datos a la BBDD
    db.session.add_all(category_list)
    db.session.commit()
    db.session.close()
    print("-------------- AGREGADAS CATEGORÍAS DE PRUEBA --------------")



if __name__ == "__main__":

    #### RESET DB
    # db.Base.metadata.drop_all(bind=db.sa_engine,)

    # La línea de código que debería de crear nuestras tablas en la BBDD, si no existen:
    # db.Base.metadata.create_all(db.sa_engine)

    """
    DESCOMENTA ESTAS TRES FUNCIONES PARA GENERAR LAS TABLAS DE CATEGORÍAS Y PREGUNTAS

    COMO YA HEMOS GENERADO LAS TABLAS Y LOS REGISTROS, 
    NO NECESITAMOS BORRAR Y VOLVER A CREAR DE 0 LAS TABLAS.
    
    TAMBIÉN HEMOS CATEGORIZADO LAS PREGUNTAS
    
    scrappeCategories()
    scrappeQuestionsAndAnswers()
    categorizingQuestions()
    """


    ##### RANDOM TRIVIA TEST #####
    #randomTriviaTest()

    # Le pasamos un array con las categorías de las preguntas que queramos
    print("PRUEBA DE TEST CATEGORIZADO 1 ----------")
    categorizedTriviaTest(8, 5, 2)

    print("PRUEBA DE TEST CATEGORIZADO 2 ----------")
    categorizedTriviaTest(1, 6)

    print("PRUEBA DE TEST CATEGORIZADO 3 ----------")
    categorizedTriviaTest(3, 4, 9, 12, 10)


   



