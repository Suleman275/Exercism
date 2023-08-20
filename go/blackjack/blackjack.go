package blackjack

// ParseCard returns the integer value of a card following blackjack ruleset.
func ParseCard(card string) int {
	var val int

	switch card {
		case "ace":
			val = 11
		case "two":
			val = 2
		case "three":
			val = 3
		case "four":
			val = 4
		case "five":
			val = 5
		case "six":
			val = 6
		case "seven":
			val = 7
		case "eight":
			val = 8
		case "nine":
			val = 9
		case "ten", "jack", "queen", "king":
			val = 10
		default:
			val = 0
	}

	return val;
}

// FirstTurn returns the decision for the first turn, given two cards of the
// player and one card of the dealer.
func FirstTurn(card1, card2, dealerCard string) string {
	panic("Please implement the FirstTurn function")
}
