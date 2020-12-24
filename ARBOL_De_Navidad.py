
''' Codificación De Árbol Navideño Con tkinter.Canvas '''


import tkinter as tk
import random     



class Arbol :
    
    def __init__(self) :
        
        self.indices = [ ]
        self.objs_nieve = [ ]
        self.contador = 0
        
        self.root = tk.Tk()
        
        self.root.configure(bg = "orange")
        
        self.canvas = tk.Canvas(self.root, width = 600, height = 600, bg = "black", bd =10, relief = "sunken")
        
      
        
        #crea la estrella del arbol
        self.puntos = 300, 50, 280, 80, 240, 80, 280, 100, 300, 130, 320, 100, 360, 80, 320, 80, 300, 50   
    
    
        self.star = self.canvas.create_polygon(self.puntos, fill = "yellow", tag = "Estrella")
        
        
        
        ''' creamos los triángulos que formarán el arbol navideño mediante un bucle for '''
        coordenadas = x1, y1, x2, y2, x3, y3 = 180, 150, 420, 150, 300, 110

        for i in range(7) :
            
            # se guarda una tupla de las coordenadas de los lados izquierdos y derechos de cada triangulo creado que servía después para agregar los adornos al arbol .
            self.indices.extend([(x1, y1, x2, y2)] ) 
        
            self.canvas.create_polygon(coordenadas, fill = "green") 
       
            x1 = x1 - 30
            y1 = y1 + 50
            x2 = 600-x1
            y2 = y1
            x3 = 300 
            y3 = y3 + 35
        
            coordenadas = x1, y1, x2, y2, x3, y3
            
        
                        
        self.add_adornos() 
        
        self.canvas.create_text((300, 300 ), text = "   FELIZ\nNAVIDAD", fill = "red", font = "Verdana 10 bold")        


        self.canvas.create_rectangle((250, 450, 350, 600), fill = "brown")

        self.canvas.create_arc( (0, 500, 640, 750),start = 0, extent = 180,  fill = "brown" ) 
        
        
        
        
        self.crear_nieve() 
        
        self.canvas.after(300, self.deslizar_nieve)  

        
                                
        
        self.canvas.pack(side = tk.TOP, pady = 50)
        
        self.root.mainloop()
            
        
    
    ''' método dónde se utiliza la lista self.indices que contiene las coordenadas de las esquinas izquierdas y derechas de cada polígono triangular que forma el árbol para crear adornos aleatorios pueden ser ovalos o rectángulos . '''        
    def add_adornos(self) :
      
      
        for i in self.indices :
            n = random.choice([0,1])
            LEFT_x1 = i[0] + 10
            LEFT_y1 = i[1]
            LEFT_x2 = LEFT_x1 + 20
            LEFT_y2 = LEFT_y1 + 20
            lado_LEFT = LEFT_x1, LEFT_y1, LEFT_x2, LEFT_y2
            
            RIGHT_x1 = i[2] - 10
            RIGHT_y1 = i[3]
            RIGHT_x2 = RIGHT_x1 + 20
            RIGHT_y2 = RIGHT_y1 + 20
            lado_RIGHT = RIGHT_x1, RIGHT_y1, RIGHT_x2, RIGHT_y2
            
            color = lambda x : random.choice(x)
            colores = ["blue", "orange", "yellow", "skyblue"]
            
            if n :               
                
                self.canvas.create_oval(lado_LEFT, fill = color(colores))
                self.canvas.create_oval(lado_RIGHT, fill = color(colores))
                
            
            else :
                
                self.canvas.create_rectangle(lado_LEFT, fill = color(colores))
                self.canvas.create_rectangle(lado_RIGHT, fill = color(colores))

                         
              
              
                
    ''' Metodo que creara 200 ovalos que representara la nieve ''' 
    def crear_nieve(self) :
            
         if self.contador <= 200 :
            
            self.contador += 1
            x1, y1 = random.randint(0,600), random.randint(0, 600)
            
            coordenadas = x1, y1, x1+ 6, y1+6 
        
            objeto = self.canvas.create_oval(coordenadas, fill = "white", tag = "nieve")
            
            self.objs_nieve.append(objeto)
            
            
               
         self.canvas.after(20, self.crear_nieve)              
            
            
    
    
    ''' Método que creara la animación de mover la nieve o ovalos creados en el Canvas ''' 
    def deslizar_nieve(self) :
        
         while True :
             
             for i in self.objs_nieve :
                 coord = self.canvas.coords(i)
                 x = y = 1
                 if coord[0] >= 600 :
                       x = -600
                 if coord[1] >= 600 :
                       y = -600
                       
                 self.canvas.move(i, x, y)
             self.canvas.update() 


''' ----------------------------- '''    
        

if __name__ == "__main__" :
      # ejecuta el programa 
      Arbol()   
      
     
