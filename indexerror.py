def index(lista):
    try:
        return lista[5]
    except IndexError:
        print("Index Error Realizamos tareas de control de cierre")
    except Exception:
        print("Exception Realizamos tareas de control de cierre")

#Comprobamos si es el flujo principal
if __name__ == "__main__":

    def main()->None:
        try:
            print(index([1, 2, 3, 4]))
        except:
            print("No lo consiguió")
    main()