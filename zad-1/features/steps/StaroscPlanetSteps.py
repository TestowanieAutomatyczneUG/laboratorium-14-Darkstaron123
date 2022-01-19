from behave import *
from modules.StaroscPlanet import staroscPlanetKlasa
use_step_matcher("re")

@given("there is a staroscPlanetKlasa")
def step_impl(context):
    context.klasa = staroscPlanetKlasa()

@when("there are: (?P<seconds>.+) seconds given?")
def step_impl(context, seconds):
    if(type(seconds)==int and seconds>0):
        return True
    else:
        return False
@when("there are: (?P<seconds>.+) false seconds given?")
def step_impl(context, seconds):
    if(type(seconds)!=int or seconds<=0):
        return False
    else:
        return True

@then("seconds from 1 year on earth are converted to years on (?P<planet>.+)?")
def step_impl(context, planet):
    context.klasa = staroscPlanetKlasa()
    context.klasa.staroscPlanet(31557600, planet)
