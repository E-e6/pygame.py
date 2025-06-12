import pygame
import sys

# Init
pygame.init()
pygame.mixer.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vista from a Grotto")

# Load images
foreground = pygame.image.load("grotto_foreground.png").convert_alpha()
background = pygame.image.load("vista_background.jpg").convert()
background = pygame.transform.scale(background, (WIDTH * 2, HEIGHT))

# Load sound
try:
    pygame.mixer.music.load("ambient_cave.wav")
    pygame.mixer.music.play(-1)  # loop forever
except:
    print("⚠️ Sound file missing or unsupported.")

# Main loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get mouse x-position and calculate scroll offset
    mouse_x = pygame.mouse.get_pos()[0]
    scroll_bg = int((mouse_x / WIDTH) * (WIDTH // 2))  # parallax: 50% scroll
    scroll_fg = int((mouse_x / WIDTH) * (WIDTH // 4))  # foreground: less scroll

    # Draw background (parallax)
    screen.blit(background, (-scroll_bg, 0))

    # Draw foreground (cave arch)
    screen.blit(foreground, (-scroll_fg, 0))

    pygame.display.flip()
    clock.tick(60)