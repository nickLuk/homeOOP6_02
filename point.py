class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def show_point(self):
        print("Coordinates point:\n - point X = ", self.x, "\n - point X = ", self.y)

    def change_point(self):
        print("Coordinates point: ", self.x, self.y)

exit = False
while not exit:
        print("+++++++++++++++ShowCoordinates+++++++++++++++++++++++++++++")
        try:
            choise = int(input(" 1. entering coordinates\n 2. show info point\n 3. change coordinates\n 0. exit\n"))
            if choise == 1:
                x = int(input("Enter coordinates x ===> "))
                y = int(input("Enter coordinates y ===> "))
                coordinates_point = Point(x, y)
                coordinates_point.show_point()
            elif choise == 2:
                
                coordinates_point.change_point()
            elif choise == 3:
                x = int(input("Enter new coordinates x ===> "))
                y = int(input("Enter new coordinates y ===> "))
                coordinates_point = Point(x, y)
                coordinates_point.change_point()

                
            elif choise == 0:
                exit = True
            else:
                    print("read manual")   
        except Exception as error:
            print("ERROR ===> ", error) 



