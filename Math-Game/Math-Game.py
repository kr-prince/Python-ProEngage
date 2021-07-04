import time
from tkinter.ttk import Progressbar, Treeview, Style
from utils import generate_expression, evaluate_expression, check_hall_of_fame, initdB, add_to_hall_of_fame, get_hof_scores
from tkinter import Button, Tk, Frame, Entry, LabelFrame, Label, StringVar, PhotoImage, Menu, messagebox, Toplevel


TIME_LIMIT = 20

# initialize dB
initdB()

def start_game():
	''' This function starts the actual game play '''
	chances, score, solved = 3, 0, 0
	while chances > 0:
		# Update the chances left 
		chanceLabel['text'] = "Chances: "+str(chances)

		# get an expression
		expr = ' _ '.join(map(str, generate_expression()[0]))
		# change the last _ to =
		i = expr.rfind('_')
		expr = expr[:i]+'='+expr[i+1:]
		expression.set(expr)
		
		start_time = time.time()
		while True:
			# Check if the expression is complete
			expr = expression.get()
			if not '_' in expr:
				check = evaluate_expression(expr)
				if check is True:
					# The expression is correct
					chances += 1
					solved += 1
					# Update the score
					score += (TIME_LIMIT - int(time.time()-start_time))
					scoreLabel['text'] = "Score: "+str(score)
				break
			# Update timer
			try:
				time_left = TIME_LIMIT - int(time.time()-start_time)
				timerBar['value'] = time_left
				# The timer becomes red if only 25% of the TIME LIMIT is left
				timerBar['style']='green.Horizontal.TProgressbar' if time_left > (0.25*TIME_LIMIT) else 'red.Horizontal.TProgressbar'
				root.update()
			except Exception as ex:
				# Exception means application has been closed abruptly
				chances = 0
				break


			if time.time() - start_time >= TIME_LIMIT:
				# if the TIME_LIMIT is over we break the loop
				break
		chances -= 1

	# Clear the display
	try:
		chanceLabel['text'] = "Chances: "
		scoreLabel['text'] = "Score: "
		timerBar['value'] = 0
		expression.set("")
		root.update()
	except:
		# Exception means application has been terminated abruptly or some widget was destroyed
		return

	# Display the final Score
	messagebox.showinfo("Final Score", "You final Score is : %d" %score)
	strike_rate = 0 if solved == 0 else round(score/solved, 2)
	if score > 0 and check_hall_of_fame(score, strike_rate):
		# If the player made it to Hall of Fame, take the name and add player
		player_name = get_player_name()
		add_to_hall_of_fame(player_name, score, strike_rate)



def get_player_name():
	''' This function gets the player name to add in hall of fame '''
	pname_window = Toplevel()
	pname_window.title("Welcome")
	pname_window.resizable(False, False)
	pname_window.focus_force()
	pname_window.geometry("500x200+%d+%d" % ((root.winfo_screenwidth() / 3),
	                                     (root.winfo_screenheight() / 3)))
	# Welcome banner
	label = Label(pname_window, text='Congrats..! You made it to the Hall of Fame')
	label.config(font='Arial 15')
	label.pack(pady=15)

	# Entry for name inputs
	pname = StringVar()
	label = Label(pname_window, text='Type your Name:')
	label.config(font='Times 10 bold')
	label.pack(pady=(10,5))
	entry = Entry(pname_window, textvariable=pname)
	entry.config(font='Times 10', width=30) 
	entry.pack()

	def exit_window():
		pname_window.destroy()
		pname_window.quit()

	# Submit button
	submit = Button(pname_window, text='Submit', command=exit_window)
	submit.config(bg='darkblue', fg='white')
	submit.pack(pady=10)
	pname_window.mainloop()
	# Return the name 
	return pname.get().title()


def display_hall_of_fame():
	''' This function displays the scores in hall of fame '''
	hof_window = Toplevel()
	hof_window.title("Hall Of Fame")
	hof_window.resizable(False, True)
	hof_window.focus_force()
	hofIcon = PhotoImage(file='./icons/trophy.png')
	hofIcon = hofIcon.subsample(2, 2)
	hof_window.iconphoto(True, hofIcon)
	hof_window.geometry("+%d+%d" % ((root.winfo_screenwidth() / 5),(root.winfo_screenheight() / 3)))

	# Fetch all records
	scores = get_hof_scores()
	# Tree View for display
	score_view = Treeview(hof_window, columns=(0, 1, 2, 3, 4), show="headings")
	score_view.pack()
	# Add Heading
	score_view.heading(0, text="Rank#")
	score_view.column(0, width=70, minwidth=70, stretch='NO', anchor='center')
	score_view.heading(1, text="Name")
	score_view.column(1, width=250, minwidth=250, stretch='NO', anchor='center')
	score_view.heading(2, text="Score")
	score_view.column(2, width=150, minwidth=150, stretch='NO', anchor='center')
	score_view.heading(3, text="Strike Rate")
	score_view.column(3, width=150, minwidth=150, stretch='NO', anchor='center')
	score_view.heading(4, text="Date")
	score_view.column(4, width=200, minwidth=200, stretch='NO', anchor='center')
	# Add scores in View
	for i,sc in enumerate(scores):
		score_view.insert(parent='', index=i+i, values=(i+1,sc[0],sc[1],sc[2],sc[3]))

	hof_window.mainloop()
	return


def exit_application():
	root.destroy()
	root.quit()



root = Tk()
root.title("Math Game")
root.resizable(False, False)
root.focus_force()
rootIcon = PhotoImage(file = './icons/logo.png')
rootIcon = rootIcon.subsample(4, 4)
root.iconphoto(False, rootIcon)
root.geometry("600x350+%d+%d" % ((root.winfo_screenwidth() / 4),(root.winfo_screenheight() / 4)))


# Creating Menubar
menubar = Menu(root)
menubar.config(bg='white', fg='blue')
# Menu options and commands
game = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Game', menu = game)
game.add_command(label ='Start Game', command = start_game)
game.add_command(label ='Hall of Fame', command = display_hall_of_fame)
game.add_separator()
game.add_command(label ='Exit', command = exit_application)
# display Menu
root.config(menu = menubar, bg='white')


gameArea = Frame(root, width=5)
gameArea.config(bg='white')
gameArea.pack(side='top', fill='x', padx=5, pady=10)

# This is the area for progress bar
# First we define the style of the progressbar
s = Style()
s.theme_use('clam')
s.configure('green.Horizontal.TProgressbar', troughcolor='white', bordercolor='black', 
						background='green', lightcolor='green', darkcolor='green')
s.configure('red.Horizontal.TProgressbar', troughcolor='white', bordercolor='black', 
						background='red', lightcolor='red', darkcolor='red')
timerBar = Progressbar(gameArea, orient='horizontal', mode='determinate')
timerBar.config(maximum=TIME_LIMIT, style='green.Horizontal.TProgressbar')
timerBar.pack(side='top', fill='x', padx=5)

# This is the area to display the math expression
mathFrame = LabelFrame(gameArea, padx=50, pady=10, text='Solve')
mathFrame.config(bg='white')
mathFrame.pack(pady=10, fill='x')

expression = StringVar()
expressionLabel = Label(mathFrame, textvariable=expression, bg='light blue')
expressionLabel.config(font='Arial 15', relief='flat', padx=5)
expressionLabel.pack(fill='x')


# This is the area to display the score and chances
statusFrame = Frame(gameArea)
statusFrame.config(bg='white')
statusFrame.pack(fill='x', pady=10)
chanceLabel = Label(statusFrame, text="Chances: ", fg='red')
chanceLabel.config(font='Arial 10 bold', relief='flat', padx=10, bg='white')
chanceLabel.pack(side='left', padx=10, pady=5, )
scoreLabel = Label(statusFrame, text="Score: ", fg='darkgreen')
scoreLabel.config(font='Arial 10 bold', relief='flat', padx=10, bg='white')
scoreLabel.pack(side='right', padx=(0,10), pady=5)



def addOperator(op):
	''' This is the command function for control buttons '''
	expr = expression.get()
	if len(expr.strip()) > 0:
		i = expr.find('_')
		expr = expr[:i]+op+expr[i+1:]
		expression.set(expr)


# This is the area to display the mathematical operation buttons
controlFrame = Frame(gameArea)
controlFrame.config(bg='white')
controlFrame.pack(pady=10)
plusIcon = PhotoImage(file = './icons/plus.png')
plusIcon = plusIcon.subsample(2, 3)
plusButton = Button(controlFrame, command=lambda : addOperator('+'))
plusButton.config(image=plusIcon, bg='light blue', highlightbackground='steel blue')
plusButton.grid(row=0,column=0, ipadx=10, padx=10, pady=10)

minusIcon = PhotoImage(file = './icons/minus.png')
minusIcon = minusIcon.subsample(2, 3)
minusButton = Button(controlFrame, text="-", command=lambda : addOperator('-'))
minusButton.config(image=minusIcon, bg='light blue', highlightbackground='steel blue')
minusButton.grid(row=0,column=1, ipadx=10, padx=10, pady=10)

multiIcon = PhotoImage(file = './icons/multi.png')
multiIcon = multiIcon.subsample(2, 3)
multiButton = Button(controlFrame, text="x", command=lambda : addOperator('*'))
multiButton.config(image=multiIcon, bg='light blue', highlightbackground='steel blue')
multiButton.grid(row=1,column=0, ipadx=10, padx=10, pady=10)

divIcon = PhotoImage(file = './icons/divide.png')
divIcon = divIcon.subsample(2, 3)
divButton = Button(controlFrame, text="/", command=lambda : addOperator('/'))
divButton.config(image=divIcon, bg='light blue', highlightbackground='steel blue')
divButton.grid(row=1,column=1, ipadx=10, padx=10, pady=10)

# Infinite loop
root.mainloop()