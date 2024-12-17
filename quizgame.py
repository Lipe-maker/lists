import pgzrun

TITLE = 'Quiz Master'
WIDTH  = 870
HEIGHT = 650

marquee_box = Rect(0,0,880,80)
question_box = Rect(0,0,650,150)
timer_box = Rect(0,0,150,150)
answer_box1 = Rect(0,0,300,150)
answer_box2 = Rect(0,0,300,150)
answer_box3 = Rect(0,0,300,150)
answer_box4 = Rect(0,0,300,150)
skip_box = Rect(0,0,1500,330)


score = 0
time_left = 10
question_file_name = 'questions.txt'
marquee_message = ''
is_game_over = False

answer_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]
questions = []
question_count = 0
question_index = 0

marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
timer_box.move_ip(700,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
skip_box.move_ip(700,270)

def draw()
    global marquee_message
    screen.clear()
    screen.fill(color='black')
    screen.draw.filled_rect(marquee_box, 'black')
    screen.draw.filled_rect(question_box,'navy blue')
    screen.draw.filled_rect(timer_box, 'navy blue')
    screen.draw.filled_rect(skip_box, 'bright green')

for answer_box in answer_boxes:
    screen.draw.filled.rect(answer_box, 'dark orange')

    marquee_message = 'Welcome to the Quiz Master . . .'
    marquee_message = marquee_message + f'q  {question_index} of {question_count}'

    screen.draw.textbox(marquee_message, marquee_box, color='white')
    screen.draw.textbox(
        str(time_left), timer_box, 
        color='white', shadow=(0.5, 0.5),
        scolor='dim grey'
    )
screen.draw.textbox(
    'Skip',skip_box,
    colors='black', angle=-90
    )
screen.draw.textbox(
        question[0].strip(), question_box, 
        color='white', shadow=(0.5, 0.5),
        scolor='dim grey'
    )
index = 1
for answer_box in answer_boxes:
    screen.draw.textbox(question[index].strip(), answer_box, color='black')
    index = index + 1

def update():
    move_marquee()



def move_marquee():
    marquee_box.x = marquee_box.x - 2
    if marquee_box.right < 0:
        marquee_box.left = WIDTH


def read_question_file():
    global question_count, questions
    q_file=open(question_file_name, 'r')
    for question in q_file:
        question.append(question)
        question_count = 
#quiz = open('quiz.txt','r')
#print( quiz.read())
#for wad in quiz:
    #print(wad)

whats the current populationnof the world,10B,15B,5B,8B,4
What is the capital of Australia?,London,Canberra,Melbourne,Tokyo,2
What is 5 x 7?,35,57,8,14,1
What is the fifth month of the year?,April,May,June,July,2
What is the largest planet in our solar system,Saturn,Neptune,Jupiter,Venus,3
Where is the stonehenge?,India,England,Scottland,Canada,2
What grows quicker?,Hair,Toenail,Skin,Eyebrows,1
Which is the tallest mountain in the world?,Mount Kilimanjaro,Mount Denali,Mount Fuji,Mount Everest,4
Which planet is known as the red planet?,Venus,Mars,Earth,Jupitar,2
Which part of the body continue to grow for your entire life?,Brain,Teeth,Nose,Eyes,3
Which first electrical item did Thomas Edision invent?,Rice cooker,Lightbulb,Hair Dryer,Fan,2
