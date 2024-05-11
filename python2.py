import turtle
def dessiner_carre(couleur):
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()
def dessiner_triangle(couleur):
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)
        turtle.end_fill()
def dessiner_motif():
 for _ in range(6):
        dessiner_carre("blue")
        turtle.right(60)
        turtle.speed(2)
dessiner_motif()
dessiner_triangle("red")
turtle.done()
