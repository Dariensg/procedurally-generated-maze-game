import pygame

import constants

def main():
    screen = pygame.display.set_mode([1000, 1000], pygame.FULLSCREEN)
    font = pygame.font.Font(None, 100)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(375, 400, 250, 100)

    text = ''
    done = False

    clock.tick(10)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return text
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        screen.fill(constants.BLACK)
        # Render the current text.
        txt_surface = font.render(text, True, constants.WHITE)
        question_surface = font.render("What is your name?", True, constants.WHITE)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width

        input_box.x = 500-(input_box[2]/2)
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        screen.blit(question_surface, [500 - (question_surface.get_rect()[2]/2), 200])
        # Blit the input_box rect.
        pygame.draw.rect(screen, constants.WHITE, input_box, 2)

        pygame.display.flip()
        clock.tick(30)
