# Military History Aid - Project

## Goals
- Build a system for tracking the movement, makeup, and historical details of military units in a dynamic way, to enhance the study of military history
- Utilize database of units, locations, and operations/campaigns to show
	+ Unit movements and details at a given moment in or over a span of time (i.e. movements, organization, etc.)
	+ Location details at a given moment in or over a span of time (i.e. occupying unit(s), terrain details, etc.)
- UI should include a Map area, Historical Date/Time controls panel, Search box panel, Unit Hierarchy tree panel, Information panel

## Features
### Map
- __Smart Dynamic Zoom__
	+ When fully zoomed out, reveals the "highest-level" units in the hierarchy, assuming that they are geographically close enough to do so (not separated by other units)
	+ As user zooms in, unit display choices are re-evaluated, to show "lower-level" units independently
- __Control Areas__
	+ Use heavier/lighter color transparencies to visually discern unit concentraion (number of individuals) in a given area; higher ratio of individuals to area yields lower transparency and vise versa
- __Unit Movements__
	+ Given 2+ different start and end dates/times (instead of just a single point in time), show the units location and concentration at each date/time and their movement paths in between

### Date/Time Controls
- __Add/Remove Date/Time Point__
	+ Users may add additional Date/Time Points, showing Unit movements between each point
- __Time Incrementation Slider__
	+ A slider that incrementally temporarily changes the current Historical Date/Time to one between two selected points; allows for the the analysis of unit movements in more detail

### Search Box
- Allows for searching by, unit, location, or operation/campaign details

### Unit Tree
- __Dynamic Hierarchy__
	+ Displays the currently selected unit in relation to its placement within the unit hierarchy; changing with the currently selected Date/Time Point

### Information Panel
- __Detail Display__
	+ Displays notable unit, location, and operation/campaign information based on the currently selected point in or span of time and the viewable area of the map

### Operations/Campaigns
- __Pause Points__
	+ Date/Time Points within a particular operation/campaign that are noted as crucial and/or significant for analytical purposes
