//Package weather provides a method to forecast the weather.
package weather

//CurrentCondition is a string that represents your current condition.
var CurrentCondition string
//CurrentLocation is a string that represents your current location.
var CurrentLocation string

//Forecast returns a forecast given a city and a condition. 
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
