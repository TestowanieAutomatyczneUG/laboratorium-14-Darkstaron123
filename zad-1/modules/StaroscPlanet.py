class staroscPlanetKlasa:
	def staroscPlanet(self,sekundy, planeta):
		if (type(sekundy) == str):
			raise Exception("Sekundy nie powinny być lancuchem znakow")
		if (sekundy < 0):
			raise Exception("Podano ujemne sekundy sekundy<0")
		if (type(planeta) != str):
			raise Exception("Nazwa planety nie jest lancuchem znakow type(planeta) !== str")
		if (planeta == "Ziemia"):
			# print(round(sekundy/(1*31557600),2))
			return round(sekundy / (1 * 31557600), 2)
		elif (planeta == "Merkury"):
			# print(round(sekundy/(0.2408467*31557600),2))
			return round(sekundy / (0.2408467 * 31557600), 2)
		elif (planeta == "Wenus"):
			# print(round(sekundy/(0.61519726*31557600),2))
			return round(sekundy / (0.61519726 * 31557600), 2)
		elif (planeta == "Mars"):
			# print(round(sekundy/(1.8808158*31557600),2))
			return round(sekundy / (1.8808158 * 31557600), 2)
		elif (planeta == "Jowisz"):
			# print(round(sekundy/(11.862615*31557600),2))
			return round(sekundy / (11.862615 * 31557600), 2)
		elif (planeta == "Saturn"):
			# print(round(sekundy/(29.447498*31557600),2))
			return round(sekundy / (29.447498 * 31557600), 2)
		elif (planeta == "Uran"):
			# print(round(sekundy/(84.016846*31557600),2))
			return round(sekundy / (84.016846 * 31557600), 2)
		elif (planeta == "Neptun"):
			# print(round(sekundy/(164.79132*31557600),2))
			return round(sekundy / (164.79132 * 31557600), 2)
		else:
			raise Exception("Podano planete ktora nie istnieje.")
print(staroscPlanetKlasa().staroscPlanet(31557600,"Ziemia"))
