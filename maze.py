import os
from colorama import Fore
import random
import turtle
import heapq
import random
import math

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("maze")
wn.setup(700,700)
wn.register_shape('F:/oop/AI_project/maze_project/acqbGGGcM.gif')
class Pen(turtle.Turtle):
    def __init__(self) :
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
class Path (turtle.Turtle):
    def __init__(self) :
        turtle.Turtle.__init__(self)
        self.shape("classic")
        self.color("red")
        self.penup()
        self.speed(0)
class Goal(turtle.Turtle):
    def __init__(self) :
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("green")
        self.penup()
        self.speed(0)


class Player(turtle.Turtle):
    def __init__(self) :
        turtle.Turtle.__init__(self)
        self.shape("F:/oop/AI_project/maze_project/acqbGGGcM.gif")
        self.color("blue")
        self.penup()
        self.speed(0)

    def go_up(self):
        move_x=player.xcor()
        move_y=player.ycor()+24
        if (move_x,move_y) not in whall:
            self.goto(move_x,move_y)

    def go_down(self):
        move_x=player.xcor()
        move_y=player.ycor()-24
        if (move_x,move_y) not in whall:
            self.goto(move_x,move_y)
    def go_left(self):
        move_x=player.xcor()-24
        move_y=player.ycor()
        if (move_x,move_y) not in whall:
            self.goto(move_x,move_y)
    def go_right(self):
        move_x=player.xcor()+24
        move_y=player.ycor()
        if (move_x,move_y) not in whall:
            self.goto(move_x,move_y)
    def win(self,other):
        a=self.xcor()- other.xcor()
        b=self.ycor()- other.ycor()
        d=math.sqrt((a**2)+(b**2))
        if d<5:
            return True
        else:
            return False
goal=Goal()
path=Path()
pen=Pen()
player=Player()
ppath=[]
whall=[]


def turtule_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character=level[y][x]
            screen_x=-288+(x*24)
            screen_y=288-(y*24)
            if character=="w":
                pen.goto(screen_x,screen_y)
                pen.stamp()
                whall.append((screen_x,screen_y))
            # if character=="z":
            #     path.goto(screen_x,screen_y)
            #     path.stamp()
            if character=="g":
                goal.goto(screen_x,screen_y)
                goal.stamp()

            if character=="c":
                player.goto(screen_x,screen_y)



wall = 'w'
cell = 'c'
unvisited = 'u'
maze = []
def maze_genrator(maze_size):

    for i in range(0, maze_size):
        line = []
        for j in range(0, maze_size):
            line.append(unvisited)
        maze.append(line)


    starting_point = random.randint(1,maze_size)
    if (starting_point == 0):
        starting_point += 1
    if (starting_point == maze_size-1):
        starting_point -= 1

    
    maze[starting_point][starting_point] = cell
    walls = []
    walls.append([starting_point - 1, starting_point])
    walls.append([starting_point, starting_point - 1])
    walls.append([starting_point, starting_point + 1])
    walls.append([starting_point + 1, starting_point])

    
    maze[starting_point-1][starting_point] = 'w'
    maze[starting_point][starting_point - 1] = 'w'
    maze[starting_point][starting_point + 1] = 'w'
    maze[starting_point + 1][starting_point] = 'w'

    while (walls):
       
        rand_wall = walls[int(random.random()*len(walls))-1]

        
        if (not(rand_wall[1] == 0)):
            if (maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
                s_cells = tedad_hamsaye(rand_wall)

                if (s_cells < 2):
                    
                    maze[rand_wall[0]][rand_wall[1]] = 'c'

                   
                    if (rand_wall[0] != 0):
                        if (not(maze[rand_wall[0]-1][rand_wall[1]] == 'c')):
                            maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])


                   
                    if (rand_wall[0] != maze_size-1):
                        if (not(maze[rand_wall[0]+1][rand_wall[1]] == 'c')):
                            maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])

                    
                    if (rand_wall[1] != 0):	
                        if (not(maze[rand_wall[0]][rand_wall[1]-1] == 'c')):
                            maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])
                
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        
        if (not(rand_wall[0] == 0)):
            if (maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]] == 'c'):

                s_cells = tedad_hamsaye(rand_wall)
                if (s_cells < 2):
                    maze[rand_wall[0]][rand_wall[1]] = 'c'

                   
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                            maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])

            
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                            maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])

                
                    if (rand_wall[1] != maze_size-1):
                        if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                            maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])

             
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

       
        if (not(rand_wall[0] == maze_size-1)):
            if (maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == 'c'):

                s_cells = tedad_hamsaye(rand_wall)
                if (s_cells < 2):
                    
                    maze[rand_wall[0]][rand_wall[1]] = 'c'

                   
                    if (rand_wall[0] != maze_size-1):
                        if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                            maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                            maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])
                    if (rand_wall[1] != maze_size-1):
                        if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                            maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])

            
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)


                continue

        
        if (not(rand_wall[1] == maze_size-1)):
            if (maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == 'c'):

                s_cells = tedad_hamsaye(rand_wall)
                if (s_cells < 2):
                   
                    maze[rand_wall[0]][rand_wall[1]] = 'c'

                    
                    if (rand_wall[1] != maze_size-1):
                        if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                            maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])
                    if (rand_wall[0] != maze_size-1):
                        if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                            maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])
                    if (rand_wall[0] != 0):	
                        if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                            maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])

                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        
        for wall in walls:
            if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                walls.remove(wall)
        


    
    for i in range(0, maze_size):
        for j in range(0, maze_size):
            if (maze[i][j] == 'u'):
                maze[i][j] = 'w'

   
    for i in range(0, maze_size):
        if (maze[1][i] == 'c'):
            maze[0][i] = 'c'
            break

    for i in range(maze_size-1, 0, -1):
        if (maze[maze_size-2][i] == 'c'):
            maze[maze_size-1][i] = 'c'
            break

    
    return maze
def tedad_hamsaye(rand_wall):
	tedad_hamsaye_hamsaye = 0
	if (maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
		tedad_hamsaye_hamsaye += 1
	if (maze[rand_wall[0]+1][rand_wall[1]] == 'c'):
		tedad_hamsaye_hamsaye += 1
	if (maze[rand_wall[0]][rand_wall[1]-1] == 'c'):
		tedad_hamsaye_hamsaye +=1
	if (maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
		tedad_hamsaye_hamsaye += 1

	return tedad_hamsaye_hamsaye

def dijkstra(maze):
    start = None
    end = None
    heap = []
    visited = set()
    distances = {}
    parents = {}

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "c":
                if start == None:
                    start = (i, j)
                else:
                    end = (i, j)
            distances[(i, j)] = float('inf')
            parents[(i, j)] = None

    distances[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        current_distance, current_cell = heapq.heappop(heap)
        if current_cell in visited:
            continue
        visited.add(current_cell)
        if current_cell == end:
            break
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= current_cell[0] + dx < len(maze) and 0 <= current_cell[1] + dy < len(maze[0]) and maze[current_cell[0] + dx][current_cell[1] + dy] != "w":
                new_distance = current_distance + 1
                if new_distance < distances[(current_cell[0] + dx, current_cell[1] + dy)]:
                    distances[(current_cell[0] + dx, current_cell[1] + dy)] = new_distance
                    heapq.heappush(heap, (new_distance, (current_cell[0] + dx, current_cell[1] + dy)))
                    parents[(current_cell[0] + dx, current_cell[1] + dy)] = current_cell

    current_cell = end
    while current_cell != start:
        current_cell = parents[current_cell]
        maze[current_cell[0]][current_cell[1]] = "z"

    return maze


def main():
    os.system("cls")
    print(f"""
    |{Fore.BLUE}############################################{Fore.WHITE}|
    |                                            |
    |          {Fore.GREEN}Maze genarator and solver{Fore.WHITE}         |
    |                                            |
    |     P:[play]                  A:[about]    |
    |                   E[exit]                  |
    |{Fore.BLUE}############################################{Fore.WHITE}|
    """)
    flag=input(":")
    if flag =="p":
        os.system("cls")
        print(f"""
        |{Fore.BLUE}#########################################{Fore.WHITE}|
        |                                         |
        |    size maze ra vared konid:            | 
        |                                         | 
        |{Fore.BLUE}#########################################{Fore.WHITE}|
        """)
        si=int(input(":"))
        os.system("cls")
        s=maze_genrator(si)
        maze_with_shortest_path = dijkstra(s)

        goal_andis=maze_with_shortest_path[0].index("z")
        maze_with_shortest_path[0][goal_andis]="g"

        levels=[""]
        level_1=[]
        string=""
        for i in maze_with_shortest_path:
            for j in i:
                string+=j
            level_1.append(string)
            string=""
        levels.append(level_1)



        turtule_maze(levels[1])

        turtle.listen()
        turtle.onkey(player.go_up,"Up")
        turtle.onkey(player.go_down,"Down")
        turtle.onkey(player.go_right,"Right")
        turtle.onkey(player.go_left,"Left")
        wn.tracer(0)

        while True:
            if player.win(goal):
                print(f"""
                |{Fore.BLUE}#############################{Fore.WHITE}|
                |                             |
                |       {Fore.GREEN}<YOU WIN!!!!>{Fore.WHITE}         |
                |                             |
                |{Fore.BLUE}#############################{Fore.WHITE}|
                """)
                wn.bye()
                
                r=input(""" Do you want to play one more time?
                            y:[main]     e:[exit]           """)
                if r=="y":
                    main()
                else:
                    exit()

            wn.update()

        




    if flag =="a":
        print("""
        |###################################|
        |   Arian Akhshabi                  |
        |   STID:990201110009               |
        |###################################|
        """)
    if flag=="e":
        exit()
  

main()

