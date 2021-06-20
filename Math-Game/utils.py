import sqlite3
from datetime import datetime
from random import choice, sample

DB_PATH = './score.db'

def generate_expression():
	''' This function generates a valid question for the game '''
	digits = [9,8,7,6,5,4,3,2,1,0]
	ops = ['+','-','*','/']
	while True:
		# run the loop till we get a valid expression
		# sample 4 digits and 3 operators 
		dstack, ostack = sample(digits, 4), sample(ops, 3)
		
		result = dstack[0]
		# validating the expression
		for i in range(3):
			if ostack[i] == '/':
				if dstack[i+1] == 0 or (result % dstack[i+1] != 0):
					# if the last operator was division and the number after that is 0
					# OR if the result so far is not divisible with the number then we have to change it
					dstack[i+1] = choice([d for d in digits[:-1] if result % d == 0])
			
			result = eval(str(result)+ostack[i]+str(dstack[i+1]))
		if result < 0:
			# if we get a negative result we run the process again
			continue
		dstack.append(int(result))
		break
	return dstack, ostack


def evaluate_expression(expr):
	''' This function evaluates the expression we get from user '''
	# Remove extra space
	expr = expr.replace(' ','')
	# split the expression to lhs and rhs
	lhs, rhs = expr.split('=')
	
	# Evaluate the expression
	res = int(lhs[0])
	for i in range(1, len(lhs), 2):
	    try:
	        res = eval(str(res)+lhs[i]+lhs[i+1])
	    except:
	        return False

	return (res == int(rhs))


def initdB():
	''' This function initialises the database for saving scores '''
	with sqlite3.connect(DB_PATH) as conn:
		conn.execute('''
			CREATE TABLE IF NOT EXISTS Score (
				ID INTEGER PRIMARY KEY AUTOINCREMENT, 
				Name TEXT NOT NULL,
				Score BIGINT NOT NULL,
				Strike_Rate FLOAT NOT NULL,
				Date_Time TEXT NOT NULL );
			''')



def check_hall_of_fame(score, strike_rate):
	''' This function checks if the player has scored better than any existing player in the hall of fame '''
	with sqlite3.connect(DB_PATH) as conn:
		# Get all the records in Score table
		records = conn.execute("SELECT Score, Strike_Rate from Score;").fetchall()
		if len(records) < 10:
			# If count is less than 10, we simply add the new score in table
			return True
		else:
			# If the hall of fame is full we check if this score is better than anybody
			for sc, sr in records:
				if score > sc or (score == sc and strike_rate > sr):
					# Add the player if any player in the hall of fame has lower score  
					# OR has the same score but lower strike rate 
					return True
		return False


def add_to_hall_of_fame(pName, score, strike_rate):
	''' This function add a player to the hall of fame '''
	with sqlite3.connect(DB_PATH) as conn:
		# First we add the new record in the table
		conn.execute("INSERT INTO Score(Name,Score,Strike_Rate,Date_Time) VALUES (?,?,?,?)", 
				(pName, score, strike_rate, datetime.now().strftime('%d-%m-%Y %I:%M %p')))
		conn.commit()
		score_count = conn.execute("SELECT COUNT(*) from Score;").fetchone()[0]
		if score_count > 10:
			# Since we store the top 10 scores only, so we have to delete the extra scores
			delete_stmt = '''
				DELETE FROM Score WHERE ID NOT IN (
					SELECT ID FROM Score 
					ORDER BY Score DESC, Strike_Rate DESC 
					LIMIT 10
				);
			'''
			conn.execute(delete_stmt)
			conn.commit()


def get_hof_scores():
	''' This function returns all the scores in hall of fame '''
	records = None
	with sqlite3.connect(DB_PATH) as conn:
		records = conn.execute('''SELECT Name,Score,Strike_Rate,Date_Time 
				FROM Score ORDER BY Score DESC, Strike_Rate DESC;''').fetchall()
	return records

if __name__ == '__main__':
	# for i in range(10):
	# 	print(generate_expression())
	# initdB()
	# check_hall_of_fame(1,1)
	print(get_hof_scores())
