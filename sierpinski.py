from graphics import *
import math

def main():
    win = GraphWin("Sierpinski", 900, 600)
    win.setBackground("white")

    altura = (((70)*math.sqrt(3))/2)

    A = Point(100,450)
    B = Point(600,500)
    C = Point(410, altura)
    A2 = B
    B2 = Point(750,370)
    C2 = C


    def getSubTriangulos(pointA, pointB, pointC):
        triangulos_procesar = []
        
        CA = operacionCoord(pointC, pointA)
        BC = operacionCoord(pointB, pointC)
        AB = operacionCoord(pointA, pointB)

        sub_triangle_1 = Polygon(pointA, CA, AB)
        sub_triangle_2 = Polygon(pointB, AB, BC)
        sub_triangle_3 = Polygon(pointC, CA, BC)

        triangulos_procesar.append(sub_triangle_3)
        triangulos_procesar.append(sub_triangle_1)
        triangulos_procesar.append(sub_triangle_2)

        return triangulos_procesar

    def operacionCoord(point1, point2):
        x = (point1.getX() / 2 + point2.getX() / 2)
        y = (point1.getY() / 2 + point2.getY() / 2)
        return Point(x,y)

    def procesar_triangulos(a_procesar):
        for triangle in a_procesar:
            triangle.setFill("black")
            triangle.draw(win)

    def check():
        resp = input("Iteracion Triangulo Sierpinski: ")
        sierpinski(esfuerzo(resp), A, B, C) 
        sierpinski(esfuerzo(resp), A2, B2, C2)
        input("Done.")
              
    def esfuerzo(resp):
        suma = 0
        
        for n in range(int(resp)):
            suma += (3 ** n)

        print("Esfuerzo:", suma)
        print("Su antena contiene {} triangulos.".format(3 ** int(resp)))
        return suma

    def sierpinski(obj, coord_A, coord_B, coord_C):
        triangulo_aux = Polygon(coord_A, coord_B, coord_C)
        aux_triangulos = [triangulo_aux]
        objetivo = obj

        for x in range (objetivo):
            vert_data = aux_triangulos.pop(0).getPoints()
            generados = getSubTriangulos(vert_data[0], vert_data[1], vert_data[2])
            for triangulo in generados:
                aux_triangulos.append(triangulo)
        procesar_triangulos(aux_triangulos)

    def debug():
        while True:
            print(win.getMouse())

    check()
    # debug()
main()

