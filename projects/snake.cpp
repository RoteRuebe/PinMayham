#include <stdio.h>
#include <unistd.h>
#include <ncurses.h>
#include <stdlib.h>
#include <cstdlib>

class LinkedElement {
    public:
        int x;
        int y;
        LinkedElement* p;

        LinkedElement(int x, int y, LinkedElement* p) {
            this->x = x;
            this -> y = y;
            this->p = p;
        }

    LinkedElement* nextElement() {
        return this->p;
    }
};

LinkedElement* initList(int length, int values[]) {
    LinkedElement* p = 0x00;
    for (int i = length*2-1; i>= 0; i -= 2) {
        p = new LinkedElement(values[i-1],values[i],p);
    }
    return p;
}

LinkedElement* getLast(LinkedElement* l) {
    int lflag = 0;
    while (!lflag) {
        if (l->p == 0x00) {
            lflag = 1;
        }
        else {
            l = l->nextElement();
        }
    }
    return l;
}

void game_over() {
    exit(0);
}

int main () {
    stdscr = initscr();
    cbreak();
    nodelay(stdscr, TRUE);
    noecho();
    curs_set(0);
    const int map_length = 20;
    WINDOW* game_window = newwin(map_length+2,map_length+2,0,0);

    int snake_length = 3;
    int direction = 0;
    int values[] = {3,3,4,3,5,3};
    const int max_amount_fruits = 3;
    LinkedElement* snake_tail = initList(snake_length,values);
    LinkedElement* snake_head = getLast(snake_tail);
    int fruits[max_amount_fruits*2];
    int amount_fruits = 0;
    
    int frame = 0;
    while (1){   
        //change direction (dont allow 180 turns)
        switch (getch()) {
            case ('d'):
                if (direction != 2) {direction = 0;}
                break;
            case('s'):
                if (direction != 3) {direction = 1;}
                break;
            case('a'):
                if (direction != 0) {direction = 2;}
                break;
            case('w'):
                if (direction != 1) {direction = 3;}
                break;
        } 
            if (frame == 1000) {
                frame = 0;
                
                //display
                LinkedElement* s = snake_tail;
                wclear(game_window);
                for (int i = 0; i < snake_length; i ++) {
                    wmove(game_window,s->y+1,s->x+1);
                    waddch(game_window,' ' | A_REVERSE);

                    s = s->nextElement();
                }
                for (int i = 0; i < amount_fruits; i += 2) {
                    wmove(game_window,fruits[i]+1,fruits[i+1]+1);
                    waddch(game_window,'B' | A_REVERSE);

                    s = s->nextElement();
                }
                box(game_window,'|','-');
                touchwin(game_window);
                wrefresh(game_window);

                //move snake       
                LinkedElement* old_snake_head = snake_head;
                LinkedElement* old_snake_tail = snake_tail;
                snake_tail = old_snake_tail->nextElement();
                snake_head = old_snake_tail;
                old_snake_head -> p = snake_head;
                snake_head -> p = 0x00;
                snake_head -> x = old_snake_head -> x;
                snake_head -> y = old_snake_head -> y;

                switch(direction) {
                    case (0):
                        snake_head->x ++;
                        break;
                    case(1):
                        snake_head->y ++;
                        break;
                    case(2):
                        snake_head->x --;
                        break;
                    case(3):
                        snake_head->y --;
                        break;
                }

                //detect collisions
                if (snake_head->x > map_length | snake_head->x < 0 | snake_head->y > map_length | snake_head -> y < 0) {
                    game_over();
                }
                s = snake_tail;
                for (int i = 0; i < snake_length-1; i++) {
                    if (snake_head -> x == s -> x && snake_head -> y == s -> y){
                        game_over();
                    }
                    s = s->nextElement();
                }

                //spawn fruits
                if (amount_fruits < max_amount_fruits) {
                    if (rand() % 10 >= 7) {
                        fruits[amount_fruits*2+1] = rand() % map_length;
                        fruits[amount_fruits*2+1] = rand() % map_length;
                        amount_fruits ++;
                    }
                }
            }
            
        usleep(100);
        frame ++;
    }
}

