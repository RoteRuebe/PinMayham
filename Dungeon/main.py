#!/usr/bin/env python3
import world, entity, curses

def main(screen):
    curses.curs_set(False)
    World = world.world(screen)
    Player = entity.player(0,0,World)

    while True:
        World.display()
        World.tick()


curses.wrapper(main)
