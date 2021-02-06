###### convertDAQ Module:
###### Module for post processing arduino data
###### Post processing prevents unnecessary use of 
###### arduino RAM

## voltage05:
## Input: analogRead value (1-1023)
## Output: voltage (0-5 V)
def voltage05(x):
	return float(x)*(5.0/1023.0)

## serialFilter:
## Converts strings to floats and filters out null output
## Input: Serial Data
## Output: Float Data
def serialFilter(str):
	try:
		out = float(str)
		return out
	except ValueError:
		return "Null"