#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    i =0
    j = 0
    move_right()
    while not wall_is_on_the_right():

        if i == j:
            fill_cell()
            i = 0
            j+=1
        i +=1
        move_right()
            


if __name__ == '__main__':
    run_tasks()
