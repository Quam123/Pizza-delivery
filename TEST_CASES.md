# Pizza Palace – Test Cases & Results
**Project:** Python Pizza Delivery Application
**Role:** Test Lead
**Tests Run:** 8

---

## TC-001 – Basic Delivery Order

| Field | Details |
|---|---|
| **Test ID** | TC-001 |
| **What I was testing** | A straightforward delivery order with one pizza, no drinks, no promo |
| **What I entered** | Name: John Doe / Address: 100 Main St / Phone: 555-0001 / Delivery / Small / Thin Crust / Pepperoni / Done with pizzas / No drinks / No promo |
| **What I expected** | Subtotal $10.49, delivery fee $3.99, tax $1.16, total $15.64 |
| **What I got** | Total: $15.64 ✅ |
| **Result** | PASS |

---

## TC-002 – Pickup Order (No Delivery Fee)

| Field | Details |
|---|---|
| **Test ID** | TC-002 |
| **What I was testing** | Making sure pickup orders don't get charged the delivery fee |
| **What I entered** | Name: Jane Smith / Pickup / Medium / Regular Crust / No toppings / No drinks / No promo |
| **What I expected** | $0.00 delivery fee, tax on $11.99, total $12.95 |
| **What I got** | Total: $12.95 ✅ |
| **Result** | PASS |

---

## TC-003 – Promo Code PIZZA10 Works

| Field | Details |
|---|---|
| **Test ID** | TC-003 |
| **What I was testing** | Entering the valid code PIZZA10 and seeing if the 10% discount shows up |
| **What I entered** | Name: Alex Lee / Large / Thick Crust / Sausage + Bacon / No drinks / Promo: PIZZA10 |
| **What I expected** | Pre-discount subtotal $19.99, discount -$2.00, delivery $3.99, tax $1.76, total $23.74 |
| **What I got** | Total: $23.74 ✅ |
| **Result** | PASS |

---

## TC-004 – Bad Promo Code Gets Rejected

| Field | Details |
|---|---|
| **Test ID** | TC-004 |
| **What I was testing** | Typing a fake promo code to make sure the app doesn't give a discount |
| **What I entered** | Normal pizza order / Promo code: FREEPIZZA |
| **What I expected** | App says "Hmm, that code didn't match anything." and charges full price |
| **What I got** | Error message shown, no discount applied ✅ |
| **Result** | PASS |

---

## TC-005 – Two Pizzas in One Order

| Field | Details |
|---|---|
| **Test ID** | TC-005 |
| **What I was testing** | Ordering two separate pizzas and checking they both show on the receipt |
| **What I entered** | Pizza 1: Small, Thin, Pepperoni / Said "Y" to add another / Pizza 2: XL, Stuffed Crust, Extra Cheese + Mushrooms |
| **What I expected** | Receipt shows Pizza #1 and Pizza #2 with their own subtotals |
| **What I got** | Both pizzas printed correctly on the receipt ✅ |
| **Result** | PASS |

---

## TC-006 – Adding Drinks

| Field | Details |
|---|---|
| **Test ID** | TC-006 |
| **What I was testing** | Adding two drinks and making sure they show up in the total |
| **What I entered** | Medium pizza / Regular crust / No toppings / Yes to drinks / Coke + Lemonade |
| **What I expected** | Coke $1.99 and Lemonade $2.49 both listed, totals correct |
| **What I got** | Both drinks on the receipt, math checked out ✅ |
| **Result** | PASS |

---

## TC-007 – Typing Letters at a Number Prompt

| Field | Details |
|---|---|
| **Test ID** | TC-007 |
| **What I was testing** | What happens if someone types letters when the app wants a number |
| **What I entered** | Typed "abc" at the size prompt, then "2" |
| **What I expected** | App says "That didn't work -- please type a number." and asks again |
| **What I got** | Error message came up, re-prompted, accepted "2" fine ✅ |
| **Result** | PASS |

---

## TC-008 – Number Out of Range

| Field | Details |
|---|---|
| **Test ID** | TC-008 |
| **What I was testing** | Entering a number that's too high for the menu options |
| **What I entered** | Typed "9" at the size prompt (only 4 options), then "3" |
| **What I expected** | App says "Pick a number from 1 to 4." and asks again |
| **What I got** | Range error shown, re-prompted, Large pizza selected on "3" ✅ |
| **Result** | PASS |

---

## Summary

| Total Tests | Passed | Failed | Pass Rate |
|---|---|---|---|
| 8 | **8** | 0 | **100%** |

Everything passed. The app handled good inputs, bad inputs, promo codes, multiple pizzas, drinks, delivery vs. pickup pricing, and the tax math without any issues.
