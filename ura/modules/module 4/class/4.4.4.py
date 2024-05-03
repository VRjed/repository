def greet(s):
	return s.capitalize()  
def whisper(s):
	return s.lower()
def shout(s):
	return s.upper()
def volume(v='Greet'):
    d = {'greet':greet,'shout':shout,'whisper':whisper}
   
    return d.get(v.lower())