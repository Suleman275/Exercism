package techpalace

import (
	"fmt"
	"strings"
)

// WelcomeMessage returns a welcome message for the customer.
func WelcomeMessage(customer string) string {
	return "Welcome to the Tech Palace, " + strings.ToUpper(customer)
}

// AddBorder adds a border to a welcome message.
func AddBorder(welcomeMsg string, numStarsPerLine int) string {
	res := fmt.Sprintln(strings.Repeat("*", numStarsPerLine))
	res += fmt.Sprintln(welcomeMsg)
	res += fmt.Sprint(strings.Repeat("*", numStarsPerLine))

	return res
}

// CleanupMessage cleans up an old marketing message.
func CleanupMessage(oldMsg string) string {
	oldMsg = strings.ReplaceAll(oldMsg, "*", "")
	oldMsg = strings.TrimSpace(oldMsg)

	return oldMsg
}
