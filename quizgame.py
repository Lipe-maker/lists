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
question_file_name = ''


#quiz = open('quiz.txt','r')
#print( quiz.read())
#for wad in quiz:
    #print(wad)
