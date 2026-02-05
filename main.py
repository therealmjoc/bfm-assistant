print("""
   ___    ___           _           _     _              _   
  / __\  / __\/\/\     /_\  ___ ___(_)___| |_ __ _ _ __ | |_ 
 /__\// / _\ /    \   //_\\\/ __/ __| / __| __/ _` | '_ \| __|
/ \/  \/ /  / /\/\ \ /  _  \__ \__ \ \__ \ || (_| | | | | |_ 
\_____/\/   \/    \/ \_/ \_/___/___/_|___/\__\__,_|_| |_|\__|
                                                             
2025 MJOC
-------------------------------------
Pre-alpha version. CONCEPT ONLY.
-------------------------------------
""")

# timetable structure
monday = ['','','','','','','','','','','','']
tuesday = ['','','','','','','','','','','','']
wednesday = ['','','','','','','','','','','','']
thursday = ['','','','','','','','','','']
friday = ['','','','','','','','','','']

timetable = [monday,tuesday,wednesday,thursday,friday]

# show slots are defined as a tuple [int day, int timeslot],
# where the day is a day 0-4 and timeslot is a time 0-11

'''
Arguments
name: the name of the show
slots: a list slots of the show, stored as a list of tuples

Inserts a show into the timetable in order of the timeslots given. If their first preference is not available, it will fall
back on their second etc.
'''
def insertShow(name, slots):
    for slot in slots:
        if timetable[slot[0]][slot[1]] == '':
            timetable[slot[0]][slot[1]] = name

insertShow("In the loop",[[0,0]])
print(timetable)