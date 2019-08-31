#!/usr/bin/python
"""Create a class Song that has methods: __init__(self, lyrics) where lyrics is a list containing the lines of the input song, and sing_me_a_song that prints all the lines of the song."""

class Song:
	def __init__(self, lyrics):
		self.lyrics = lyrics
	def sing_me_a_song(self):
		[print (lines) for lines in self.lyrics]

fix_you = Song(["Lights will guide you home",
				"And ignite your bones ",
				"And I will try to fix you"])

fix_you.sing_me_a_song()