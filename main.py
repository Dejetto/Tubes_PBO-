import pygame , os

#class ini merupakan kelas dari seluruh tampilan dan inisialisasi game
class Game(): 
    def  __init__ (self):
        pygame.init()
        self.width , self.height = 900 , 500 #lebar jendela window
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("1v1 Bang-Bang") #judul window
        self.run , self.running = True, True #varibel untuk mengecek kejadian 

    #fungsi ini untuk melakukan perulangan terhadap game
    def loop (self):
        while self.run:
            self.get_event()

    #fungsi untuk mendapatkan event terhadap kejadian pada game. Mis QUIT, PLAY, START, dll
    def get_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                pygame.quit()

    #fungsi ini untuk membuat objek hero yang akan dipilih
    def load_player():
        pass

    #fungsi ini untuk membuat objek menu
    def load_menu():
        pass

    #fungsi ini untuk mengatur FPS dari game
    def get_FPS():
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    #Fungsi ini untuk membuat background dari game
    def background():
        text_surface = self.font.render(text, True, color)
            #text_surface.set_colorkey((0,0,0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)




if __name__ == "__main__":
    BB1v1 = Game()
     
    while BB1v1.running:
        BB1v1.loop()


