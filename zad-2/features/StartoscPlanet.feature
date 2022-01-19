Feature: StaroscPlanetValidator
	Check, if function converts time on different planets in reference to earth time correctly

	Scenario Outline: Earth Year to <<planeta>>
		Given there is a staroscPlanetKlasa
		When there are: <seconds given> seconds given
		Then seconds from 1 year on earth are converted to years on <planeta>

		Examples:
			| seconds given     | planeta          |
			| 67                | Mars             |
			| 92023             | Wenus            |
			| 3653              | Uran             |
			| 55                | Jowisz           |
			| 33                | Merkury          |
			| 88                | Neptun           |