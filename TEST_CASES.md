# Pizza Palace – Test Cases & Results
**Project:** Python Pizza Delivery Application  
**Tester Role:** Test Lead  
**Total Test Cases:** 8  

---

## Test Case 1 – Valid Delivery Order (Basic)
| Field | Details |
|---|---|
| **Test ID** | TC-001 |
| **Description** | Place a single delivery order with one pizza, no drinks, no promo code |
| **Inputs** | Name: John Doe / Address: 100 Main St / Phone: 555-0001 / Order: Delivery / Size: Small / Crust: Thin / Topping: Pepperoni / No more pizzas / No drinks / No promo code |
| **Expected Output** | Subtotal: $10.49, Delivery Fee: $3.99, Tax: $1.16, **Total: $15.64** |
| **Actual Output** | Total: $15.64 ✅ |
| **Result** | **PASS** |

---

## Test Case 2 – Valid Pickup Order (No Delivery Fee)
| Field | Details |
|---|---|
| **Test ID** | TC-002 |
| **Description** | Place a pickup order — no delivery fee should be applied |
| **Inputs** | Name: Jane Smith / Address: N/A / Phone: 555-0002 / Order: Pickup / Size: Medium / Crust: Regular / No toppings / No drinks / No promo |
| **Expected Output** | Delivery Fee: $0.00, Tax on $11.99, **Total: $12.95** |
| **Actual Output** | Total: $12.95 ✅ |
| **Result** | **PASS** |

---

## Test Case 3 – Valid Promo Code (PIZZA10)
| Field | Details |
|---|---|
| **Test ID** | TC-003 |
| **Description** | Apply valid promo code PIZZA10 and verify 10% discount is applied |
| **Inputs** | Name: Alex Lee / Size: Large / Crust: Thick / Toppings: Sausage, Bacon / No drinks / Promo: PIZZA10 |
| **Expected Output** | Subtotal before discount: $19.99 / Discount: $2.00 / Delivery Fee: $3.99 / Tax: $1.76 / **Total: $23.74** |
| **Actual Output** | Total: $23.74 ✅ |
| **Result** | **PASS** |

---

## Test Case 4 – Invalid Promo Code
| Field | Details |
|---|---|
| **Test ID** | TC-004 |
| **Description** | Enter an invalid promo code — no discount should be applied |
| **Inputs** | Valid pizza order / Promo code: FREEPIZZA |
| **Expected Output** | Message: "Invalid promo code." / No discount applied |
| **Actual Output** | "Invalid promo code." printed / Full price charged ✅ |
| **Result** | **PASS** |

---

## Test Case 5 – Multiple Pizzas in One Order
| Field | Details |
|---|---|
| **Test ID** | TC-005 |
| **Description** | Order two pizzas and verify both are itemized on the receipt |
| **Inputs** | Pizza 1: Small, Thin, Pepperoni / Pizza 2: XL, Stuffed Crust, Extra Cheese + Mushrooms / Add another pizza: Y (after pizza 1) |
| **Expected Output** | Receipt shows Pizza #1 and Pizza #2 with separate subtotals |
| **Actual Output** | Both pizzas displayed correctly on receipt ✅ |
| **Result** | **PASS** |

---

## Test Case 6 – Add Drinks to Order
| Field | Details |
|---|---|
| **Test ID** | TC-006 |
| **Description** | Add two drinks and verify prices are included in the total |
| **Inputs** | Pizza: Medium / Regular / No toppings / Add drinks: Y / Coke + Lemonade |
| **Expected Output** | Drinks listed: Coke $1.99, Lemonade $2.49 / Included in subtotal |
| **Actual Output** | Both drinks itemized, total updated correctly ✅ |
| **Result** | **PASS** |

---

## Test Case 7 – Invalid Menu Input (Letters Instead of Numbers)
| Field | Details |
|---|---|
| **Test ID** | TC-007 |
| **Description** | Enter a letter when a number is expected — program should re-prompt |
| **Inputs** | At size prompt, enter: "abc" then "2" |
| **Expected Output** | Message: "Invalid input. Please enter a number." / Re-prompts for input |
| **Actual Output** | Error message shown, re-prompted successfully ✅ |
| **Result** | **PASS** |

---

## Test Case 8 – Out-of-Range Menu Input
| Field | Details |
|---|---|
| **Test ID** | TC-008 |
| **Description** | Enter a number outside valid range — program should re-prompt |
| **Inputs** | At size prompt, enter: "9" then "3" |
| **Expected Output** | Message: "Please enter a number between 1 and 4." / Re-prompts |
| **Actual Output** | Error message shown, re-prompted, Large pizza selected ✅ |
| **Result** | **PASS** |

---

## Summary

| Total Tests | Passed | Failed | Pass Rate |
|---|---|---|---|
| 8 | **8** | 0 | **100%** |

All test cases passed. The application correctly handles valid inputs, invalid inputs, promo codes, multiple pizzas, drink additions, delivery vs. pickup pricing, and tax calculations.
