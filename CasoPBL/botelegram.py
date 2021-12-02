import telebot  # Importamos las librería
import random

TOKEN = "2114301277:AAFy7LA2v4Bl7F33wNiEBz0cUUsMvv0jp5I"  # Ponemos nuestro Token generado con el @BotFather
bot = telebot.TeleBot(TOKEN)  # Creamos nuestra instancia "bot" a partir de ese TOKEN.
iniciar = False


# Comando inicio para que el bot salude.
@bot.message_handler(commands=['inicio'])
def inicio(message):
    bot.reply_to(message, "Oído cocina. Tú dirás...")


# Comando Ods para citar un objetivo de desarrollo sostenible aleatorio.
@bot.message_handler(commands=['ods'])
def ods(message):
    numrand = random.randint(1, 17)
    if numrand == 1:
        bot.reply_to(message,
                     "Erradicar la pobreza en todas sus formas sigue siendo uno de los principales desafíos que "
                     "enfrenta la humanidad. Si bien la cantidad de personas que viven en la extrema pobreza "
                     "disminuyó en más de la mitad entre 1990 y 2015, aún demasiadas luchan por satisfacer las "
                     "necesidades más básicas.")
    elif numrand == 2:
        bot.reply_to(message,
                     "Debido al rápido crecimiento económico y al aumento de la productividad agrícola en las últimas "
                     "dos décadas, el número de personas desnutridas disminuyó casi a la mitad. Muchos países en "
                     "desarrollo que sufrían hambrunas están ahora en condiciones de satisfacer las necesidades "
                     "nutricionales de los más vulnerables. Regiones como Asia Central y Oriental y América Latina y "
                     "el Caribe han avanzado enormemente en la erradicación del hambre.")
    elif numrand == 3:
        bot.reply_to(message,
                     "Hemos logrado grandes avances en la lucha contra varias de las principales causas de muerte y "
                     "enfermedad. La esperanza de vida ha aumentado drásticamente, las tasas de mortalidad infantil y "
                     "materna han disminuido, hemos cambiado el curso del VIH y la mortalidad debida a la malaria se "
                     "ha reducido a la mitad.")
    elif numrand == 4:
        bot.reply_to(message,
                     "Desde 2000 se ha registrado un enorme progreso en la meta relativa a la educación primaria "
                     "universal. La tasa total de matrícula alcanzó el 91% en las regiones en desarrollo en 2015 y la "
                     "cantidad de niños que no asisten a la escuela disminuyó casi a la mitad a nivel mundial. "
                     "También ha habido aumentos significativos en las tasas de alfabetización y más niñas que nunca "
                     "antes asisten hoy a la escuela. Sin duda, se trata de logros notables.")
    elif numrand == 5:
        bot.reply_to(message,
                     "Poner fin a todas las formas de discriminación contra las mujeres y niñas no es solo un derecho "
                     "humano básico, sino que además es crucial para el desarrollo sostenible. Se ha demostrado una y "
                     "otra vez que empoderar a las mujeres y niñas tiene un efecto multiplicador y ayuda a promover "
                     "el crecimiento económico y el desarrollo a nivel mundial.")
    elif numrand == 6:
        bot.reply_to(message,
                     "La escasez de agua afecta a más del 40 por ciento de la población mundial, una cifra alarmante "
                     "que probablemente crecerá con el aumento de las temperaturas globales producto del cambio "
                     "climático. Aunque 2.100 millones de personas han conseguido acceso a mejores condiciones de "
                     "agua y saneamiento desde 1990, la decreciente disponibilidad de agua potable de calidad es un "
                     "problema importante que aqueja a todos los continentes.")
    elif numrand == 7:
        bot.reply_to(message,
                     "Expandir la infraestructura y mejorar la tecnología para contar con energía limpia en todos los "
                     "países en desarrollo, es un objetivo crucial que puede estimular el crecimiento y a la vez "
                     "ayudar al medio ambiente.")
    elif numrand == 8:
        bot.reply_to(message,
                     "Fomentar políticas que estimulen el espíritu empresarial y la creación de empleo es crucial "
                     "para este fin, así como también las medidas eficaces para erradicar el trabajo forzoso, "
                     "la esclavitud y el tráfico humano. Con estas metas en consideración, el objetivo es lograr "
                     "empleo pleno y productivo y un trabajo decente para todos los hombres y mujeres para 2030.")
    elif numrand == 9:
        bot.reply_to(message,
                     "La inversión en infraestructura y la innovación son motores fundamentales del crecimiento y el "
                     "desarrollo económico. Con más de la mitad de la población mundial viviendo en ciudades, "
                     "el transporte masivo y la energía renovable son cada vez más importantes, así como también el "
                     "crecimiento de nuevas industrias y de las tecnologías de la información y las comunicaciones.")
    elif numrand == 10:
        bot.reply_to(message,
                     "La desigualad de ingresos es un problema mundial que requiere soluciones globales. Estas "
                     "incluyen mejorar la regulación y el control de los mercados y las instituciones financieras y "
                     "fomentar la asistencia para el desarrollo y la inversión extranjera directa para las regiones "
                     "que más lo necesiten. Otro factor clave para salvar esta distancia es facilitar la migración y "
                     "la movilidad segura de las personas.")
    elif numrand == 11:
        bot.reply_to(message,
                     "Mejorar la seguridad y la sostenibilidad de las ciudades implica garantizar el acceso a "
                     "viviendas seguras y asequibles y el mejoramiento de los asentamientos marginales. También "
                     "incluye realizar inversiones en transporte público, crear áreas públicas verdes y mejorar la "
                     "planificación y gestión urbana de manera que sea participativa e inclusiva.")
    elif numrand == 12:
        bot.reply_to(message,
                     "La gestión eficiente de los recursos naturales compartidos y la forma en que se eliminan los "
                     "desechos tóxicos y los contaminantes son vitales para lograr este objetivo. También es "
                     "importante instar a las industrias, los negocios y los consumidores a reciclar y reducir los "
                     "desechos, como asimismo apoyar a los países en desarrollo a avanzar hacia patrones sostenibles "
                     "de consumo para 2030.")
    elif numrand == 13:
        bot.reply_to(message,
                     "Apoyar a las regiones más vulnerables contriubuirá directamente no solo al Objetivo 13 sino "
                     "tamién a otros Objetivos de Desarrollo Sostenible. Estas acciones deben ir de la mano con los "
                     "esfuerzos destinados a integrar las medidas de reducción del riesgo de desastres en las "
                     "políticas y estrategias nacionales. Con voluntad política y un amplio abanico de medidas "
                     "tecnológicas, aún es posible limitar el aumento de la temperatura media global a dos grados "
                     "Celsius por encima de los niveles pre-industriales, apuntando a 1,5°C. Para lograrlo, "
                     "se requieren acciones colectivas urgentes.")
    elif numrand == 14:
        bot.reply_to(message,
                     "Los Objetivos de Desarrollo Sostenible generan un marco para ordenar y proteger de manera "
                     "sostenible los ecosistemas marinos y costeros de la contaminación terrestre, así como para "
                     "abordar los impactos de la acidificación de los océanos. Mejorar la conservación y el uso "
                     "sostenible de los recursos oceánicos a través del derecho internacional también ayudará a "
                     "mitigar algunos de los retos que enfrentan los océanos.")
    elif numrand == 15:
        bot.reply_to(message,
                     "La vida humana depende de la tierra tanto como del océano para su sustento y subsistencia. La "
                     "flora provee el 80% de la alimentación humana y la agricultura representa un recurso económico "
                     "y un medio de desarrollo importante. A su vez, los bosques cubren el 30% de la superficie "
                     "terrestre, proveen hábitats cruciales a millones de especies y son fuente importante de aire "
                     "limpio y agua. Además, son fundamentales para combatir el cambio climático.")
    elif numrand == 16:
        bot.reply_to(message,
                     "Los Objetivos de Desarrollo Sostenible buscan reducir sustancialmente todas las formas de "
                     "violencia y trabajan con los gobiernos y las comunidades para encontrar soluciones duraderas a "
                     "los conflictos e inseguridad. El fortalecimiento del Estado de derecho y la promoción de los "
                     "derechos humanos es fundamental en este proceso, así como la reducción del flujo de armas "
                     "ilícitas y la consolidación de la participación de los países en desarrollo en las "
                     "instituciones de gobernabilidad mundial.")
    elif numrand == 17:
        bot.reply_to(message,
                     "Los Objetivos de Desarrollo Sostenible solo se pueden lograr con el compromiso decidido a favor "
                     "de alianzas mundiales y cooperación. La Asistencia Oficial para el Desarrollo se mantuvo "
                     "estable pero por debajo del objetivo, a US$147.000 millones en 2017, mientras que las crisis "
                     "humanitarias provocadas por conflictos o desastres naturales continúan demandando más recursos "
                     "y ayuda financiera. Muchos países también requieren de esta asistencia para estimular el "
                     "crecimiento y el intercambio comercial.")


# Comando cita para mostrar una cita del aula virtual aleatoriamente.
@bot.message_handler(commands=['cita'])
def ods(message):
    numrand = random.randint(1, 14)
    if numrand == 1:
        bot.reply_to(message, "Al no ser los únicos, decidimos ser los mejores. (Gorka Lomeña)")
    elif numrand == 2:
        bot.reply_to(message,
                     "Con demasiada frecuencia damos a los estudiantes respuestas para recordar en lugar de problemas "
                     "para resolver (Roger Lewin)")
    elif numrand == 3:
        bot.reply_to(message,
                     "Si la depuración es el proceso de eliminar errores, entonces la programación debe ser el "
                     "proceso de introducirlos. (Edsger Dijkstra)")
    elif numrand == 4:
        bot.reply_to(message,
                     "Pensar es el trabajo más difícil que existe. Quizá esa sea la razón por la que haya tan pocas "
                     "personas que lo practiquen. (Henry Ford)")
    elif numrand == 5:
        bot.reply_to(message,
                     "No es que sea muy inteligente. Es simplemente que estoy más tiempo con los problemas. (Albert "
                     "Einstein)")
    elif numrand == 6:
        bot.reply_to(message,
                     "Programar no es un talento; es una habilidad. En tu mano está desarrollarla. (Codecademy)")
    elif numrand == 7:
        bot.reply_to(message, "No digas: “Es imposible”. Di: “No lo he hecho todavía”. (Proverbio japonés)")
    elif numrand == 8:
        bot.reply_to(message,
                     "Al ordenador le importa tres leches tu problema, así que el esfuerzo por que éste realice un "
                     "proceso por el cual se resuelve dicho problema lo tienes que hacer TÚ. Y el esfuerzo consiste "
                     "en dárselo mascado para que lo lleve a cabo una y otra vez. (Alex Tolón)")
    elif numrand == 9:
        bot.reply_to(message, "Las raíces del estudio son amargas. Los frutos, dulces. (Cicerón)")
    elif numrand == 10:
        bot.reply_to(message,
                     "Los malos programadores se preocupan del código. Los buenos se preocupan de las estructuras de "
                     "datos y de sus relaciones. (Linus Torvalds)")
    elif numrand == 11:
        bot.reply_to(message, "La práctica te perfecciona. Descubre cuánta práctica necesitas tú. (Alex Tolón)")
    elif numrand == 12:
        bot.reply_to(message, "Un problema se transforma en desafío cuando le pones fecha de solución. (Anónimo)")
    elif numrand == 13:
        bot.reply_to(message, "El futuro no es lo que va a pasar sino lo que vamos a hacer. (Anónimo)")
    elif numrand == 14:
        bot.reply_to(message,
                     "La experiencia demuestra que el éxito de un curso de programación depende críticamente de la "
                     "elección de los ejemplos que se utilice. (Niklaus Wirth)")


# Comando final para que el bot se despida.
@bot.message_handler(commands=['final'])
def final(message):
    bot.reply_to(message, "¡Que pases un buen día!")


bot.polling()
