from modules.StaroscPlanet import staroscPlanetKlasa

def before_scenario(context, scenario):
	context.klasa = staroscPlanetKlasa()

def after_scenario(context, scenario):
	context.klasa = None

