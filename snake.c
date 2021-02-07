#include <stdio.h>
#include <unistd.h>
#include <curses.h>

struct LinkedElement {
    int x;
    int *p;
};

LinkedElement nextElement (LinkedElement* el) {
    return el+1;
}

int main () {

}


/*
    int map_length = 10;
    int snake[map_length*map_length];
    int snake_length = 1;
    int direction = 0;
    snake[0] = 0;
    snake[1] = 0;
    snake[2] = 0;
    snake[3] = 1;

    while (1){
        switch(direction) {
            case (0):
                snake[snake_length*2-1] ++;
                break;
            case(1):
                snake[snake_length*2] --;
                break;
            case(2):
                snake[snake_length*2-1] --;
                break;
            case(3):
                snake[snake_length*2] ++;
                break;
        }
        for (int y = 0; y < map_length; y++) {
            for (int x = 0; x < map_length; x++) {
                for (int i = 0; i <= snake_length; i++) {
                    if (x == snake[i] && y == snake[i+1]) {
                        printf("S");
                    }
                    else {
                        printf("X");
                    }
                }
            }
            printf("\n");
        }
    sleep(1);
    printf("\n\n\n");
    }
*/

