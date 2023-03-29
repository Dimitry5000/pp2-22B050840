import pygame
pygame.init()
def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
def play_previous_song():
    global _songs
    _songs = _songs[-1] + _songs[:-1]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
screen = pygame.display.set_mode((500,500))
running = True
_songs = "somesong, somesong2, somesong3"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            pygame.mixer.music.play(-1)
        if pressed[pygame.K_DOWN]:
            pygame.mixer.music.pause()
        if pressed[pygame.K_LEFT]:
            pygame.mixer.music.stop()
        if pressed[pygame.K_RIGHT]:
            play_next_song()
        if pressed[pygame.K_0]:
            play_previous_song()
    pygame.display.flip()