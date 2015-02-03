
class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print self.sounds[i % len(self.sounds)],
        print ""

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print "Be with you in a moment"
        print "Twoning, sproing, splang"

class Drummer(Musician):
	def __init__(self):
		super(Drummer, self).__init__(['d1','d2','d3','d4'])
		super(Drummer, self).solo(4)

class Band():       

	def hire_or_fire(self):
		first_input=raw_input("plz type in whether u want to hire(H) or fire(F) a musician:") 
		if (first_input == 'H' ): 
			hire_input=raw_input("plz write the names of the musicians that you want to hire:")
			musicisns.append(hire_input)
			print 'your new band members will be %s' %musicisns
		elif (first_input == 'F' ): 
			fire_input=raw_input("plz select the name that you want to fire from the list %s :" %musicisns)
			musicisns.remove(fire_input)
			print 'your new band members will be %s' %musicisns

	#def play(self):
	#	super(Band, self).__init__()
		#super(Band, self).__init__()


a= Band()
print a.hire_or_fire()

