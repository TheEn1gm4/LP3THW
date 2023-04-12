type_of_people= 10
x = f"Hay {type_of_people} tipos de persona"

binary= "binario"
do_not="no"
y=f"esos que saben {binary} y esos que {do_not}. "

print(x)
print(y)

print(f"Yo digo {x}")
print(f"Yo tambien digo '{y}'. ")

hilarious=False
joke_evaluation="no es ese chiste bien gracioso!? {}"
print(joke_evaluation.format(hilarious))

w= "Este es el lado izquierdo de... "
e= "una cadena con un lado derecho"
print(w+e)