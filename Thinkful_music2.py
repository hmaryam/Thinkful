#Drummers should be able to solo, count to four, and spontaneously combust. Then add a Band class. Bands should be able to hire and fire musicians, and have the musicians play their solos after the drummer has counted time.
import random       

class Musician(object):
	#sounds = [] is an attribute 
    def __init__(self, sounds, name):
        self.sounds = sounds
        self.name = name
    # length is an parameter
    def solo(self, length):
    	music= []
        for i in range(length):
            music.append(self.sounds[i % len(self.sounds)])
        return music

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"], 'bassist')

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Guitarist, self).__init__(["Boink", "Bow", "Boom"], 'guitarist')

    def tune(self):
        print "Be with you in a moment"
        print "Twoning, sproing, splang"

class Drummer(Musician):
	def __init__(self):
		super(Drummer, self).__init__(['d1','d2','d3'], 'drummer')
	
class Band():
#Relationship betwenn (class Band) and (class Guitarist) and (class Bassist) and (Class Drummer) 	
	def __init__(self):
			self.Bassist = None
			self.Guitarist = None
			self.Drummer = None
			
	def hire(self, **players):
		self.Bassist= players.get('bass')
		self.Guitarist= players.get('git')
		self.Drummer= players.get('drum')
		print players.get('bass').name, players.get('git').name, players.get('drum').name

	def fire(self, **players):
		if self.Bassist != None and players.get('bass')!= None:
			self.Bassist = None
			print '%s is fired' % players.get('bass').name
		if self.Guitarist != None and players.get('git') != None:
			self.Guitarist = None
			print '%s is fired' % players.get('git').name
		if self.Drummer != None and players.get('drum') != None:
			self.Drummer = None
			print '%s is fired' % players.get('drum').name

	def members(self):
		memberlist=[]
		if self.Bassist != None:
			memberlist.append(self.Bassist.name)
		if self.Guitarist != None:
			memberlist.append(self.Guitarist.name)
		if self.Drummer != None:
			memberlist.append(self.Drummer.name)
		print ' The band members after hiring and firing, are: %s' % memberlist

		
	def play(self):
		playlist= []
		randomlist=[]
		if self.Drummer != None:
			print d.solo(4)
		if self.Bassist != None:
			playlist.append(g.solo(random.randint(1, 5)))
		if self.Guitarist != None:
			playlist.append(b.solo(random.randint(1, 5)))

		if len(playlist) > 0:
			randomlist.append(playlist[random.randint(0, len(playlist)-1)])

		if len(playlist) > 1:

			temp = playlist[random.randint(0, len(playlist)-1)]
			while temp == randomlist[0] :
				temp = playlist[random.randint(0, len(playlist)-1)]
			randomlist.append(temp)

		for i in randomlist:
			print i

			

b = Bassist()
g = Guitarist()
d = Drummer() 

p = {'bass':b, 'git': g, 'drum': d}
f={'git':g, 'bass':b}

band = Band()

band.hire(**p)
band.fire(**f)
band.members()
band.play()

