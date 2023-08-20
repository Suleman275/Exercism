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

	return val
}

// FirstTurn returns the decision for the first turn, given two cards of the
// player and one card of the dealer.
func FirstTurn(card1, card2, dealerCard string) string {
	var res string

	cardsTotalVal := ParseCard(card1) + ParseCard(card2)

	switch {
	case card1 == "ace" && card2 == "ace":
		res = "P"
	case (cardsTotalVal == 21) && (ParseCard(dealerCard) < 10):
		res = "W"
	case (cardsTotalVal == 21) && (ParseCard(dealerCard) >= 10):
		res = "S"
	case cardsTotalVal > 16 && cardsTotalVal < 21:
		res = "S"
	case cardsTotalVal > 11 && cardsTotalVal < 17 && ParseCard(dealerCard) >= 7:
		res = "H"
	case cardsTotalVal > 11 && cardsTotalVal < 17:
		res = "S"
	case cardsTotalVal <= 11:
		res = "H"
	}

	return res
}
