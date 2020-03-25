#!/usr/bin/env python3
import world, player

class main:
    def __init__ (self):
        self.World = world.world()
        self.Player = player.player(0,0)
        self.World.new_entity(self.Player)
        self.loop()
        
    def loop (self):
        while True:
            self.World.display()
            for entity in self.World.entitys:
                entity.tick()
                

m = main()