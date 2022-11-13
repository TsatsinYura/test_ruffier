class Mapmanager():
    """ Управление картой """
    def __init__(self):
        self.model = 'block' # модель кубика лежит в файле block.egg
        # # используются следующие текстуры: 
        self.texture = 'block.png'          
        self.color =(0.5, 0.3, 0.0, 1) #rgba
        # создаём основной узел карты:
        self.startNew() 
        # self.addBlock((0,10, 0))
sdfasffsdaf
    def startNew(self):
        """создаёт основу для новой карты""" 
        self.land = render.attachNewNode("Land") # узел, к которому привязаны все блоки карты
    
    def addBlock(self, position):
        # создаём строительные блоки 

        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture)) 
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)

    def clear(self):
        """обнуляет карту"""
        self.land.removeNode()
        self.startNew()

    def loadLand(self, filename):
        """создаёт карту земли из текстового файла, возвращает её размеры"""
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    for z0 in range(int(z)+1):
                        block = self.addBlock((x, y, z0))
                    x += 1
                y += 1

