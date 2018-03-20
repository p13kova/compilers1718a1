"""
Sample script to test ad-hoc scanning by table drive.
This accepts time in 24hour format (xx:xx, x:xx, x.xx, xx.xx) 
"""

def getchar(words,pos):
	""" returns groupChars at pos of words, or None if out of bounds """

	if pos<0 or pos>=len(words): return None

	

	if words[pos] >= '0' and words[pos] <= '1':
		return 'digit_0'

	elif words[pos] == '2':
		return 'digit_1'

	elif words[pos] >= '0' and words[pos] <= '3':
		return 'digit_2'

	elif words[pos] >= '0' and words[pos] <= '5':
		return 'min_1'

	elif words[pos] >= '0' and words[pos] <= '9':
		return 'min_2'


	elif words[pos] == ':' or words[pos] == '.':
		return 'time_interval'

	else:
		return 'OTHER'



	

def scan(text,transition_table,accept_states):
	""" Scans `text` while transitions exist in 'transition_table'.
	After that, if in a state belonging to `accept_states`,
	returns the corresponding token, else ERROR_TOKEN.
	"""
	
	# initial state
	
	pos = 0
	state = 'q0'
	
	while True:
		
		c = getchar(text,pos)	# get next char
		
		if state in transition_table and c in transition_table[state]:
		
			state = transition_table[state][c]	# set new state
			pos += 1	# advance to next char

			
		else:	# no transition found

			# check if current state is accepting
			if state in accept_states:
				return accept_states[state],pos

			# current state is not accepting
			return 'ERROR_TOKEN',pos
			
	
# the transition table, as a dictionary
td = { 
		'q0' : {'digit_0' : 'q1', 'digit_1' : 'q2', 'digit_2' : 'q3', 'min_1' : 'q3', 'min_2' : 'q3','OTHER':'q8'},
		'q1' : {'time_interval' : 'q5','digit_0': 'q3', 'digit_1' : 'q3', 'digit_2' : 'q3' , 'min_1' : 'q3','min_2' : 'q3','OTHER':'q8'},
		'q2' : {'time_interval' : 'q5', 'digit_0': 'q4', 'digit_1' : 'q4', 'digit_2' : 'q4','OTHER':'q8' },
		'q3' : {'time_interval' : 'q5','OTHER':'q8'},
		'q4' : {'time_interval' : 'q5','OTHER':'q8'},
		'q5' : {'digit_0': 'q6', 'digit_1' : 'q6', 'digit_2' : 'q6', 'min_1' : 'q6','OTHER':'q8'},
		'q6' : {'digit_0': 'q7', 'digit_1' : 'q7', 'digit_2' : 'q7', 'min_1' : 'q7', 'min_2' : 'q7','OTHER':'q8',}
        
     } 


# the dictionary of accepting states and their
# corresponding token
ad = {'q7' : 'TIME_TOKEN',
      'q8' : 'WRONG INPUT'
}




# get a string from input
text = input('give some input>')



# scan text until no more input
while text:	# that is, while len(text)>0
	
	# get next token and position after last char recognized
	token,position = scan(text,td,ad)
	
	if token=='ERROR_TOKEN':
		print('ERROR_TOKEN: unrecognized input at pos',position+1,'of',text)
		break
	
	print(token,text[:position])
	
	# remaining text for next scan

	text = text[position: ]
