import random
def intDiv(a:int, b:int)->int:
    try:
        return a // b
    except TypeError:
        print("Realizamos tareas de control de cierre")
    except ZeroDivisionError:
        print("ZeroDivisionError Realizamos tareas de control de cierre")
    except Exception:
        print("Exception Realizamos tareas de control de cierre")

#Comprobamos si es el flujo principal
if __name__ == "__main__":

    def main()->None:
        for i in range(30):
            a = random.randint(0, 9)
            b = random.randint(0, 9)
            print("a:", a, "b:", b, "a // b:", intDiv(a, b))
            
        intDiv(2, "3")
        try:
            intDiv()
        except:
            print("No lo consiguió")

    main()