import pygame


class EventHandler():
    """Different events are important in different situations"""

    def normal(event_queue, control_args):
        for event in event_queue:
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                control_args.append("p1_shoot")

    def alternating(event_queue):
        for event in event_queue:
            if event.type == pygame.QUIT:
                quit()
