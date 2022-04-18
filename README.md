# Awesome Wallet

A simple online budget-logger for those who find managing their (monthly) budget hard.

## 1. How to Run
1. Run app.py ```python3 app.py```
2. Copy and paste the local host (local host for demo purposes) to your web browser.
3. Login with the demo accounts ```ID: admin1, PW: 123``` or ```ID: user1, PW: 321``` (see Section 2)

## 2. Motivation
Some people, maybe kids, people with disabilities or the elders, may find it hard to manage or understand their spending habbits. The website povides budget managing and visualisation features for the user. One account is divided into the admin page and the user page, so that their parents or cares can acceess the admin page to update the monthly budget. The inputted data is then visualised on the user page so that it is easier to see their monthly expenses.

## 3. Key Features
- Login page that takes you to the admin or the user page depending on the account.
- The admin can set the total monthly budget (balance)
- Admin can then log out the expenditures of the user under the relevant categories
- The user can spend as much as 20% of the total balance on each category (e.g food)
- The user can check their balance for each category (food, transport, etc.) on the user page.
- The user page displays progress bars (showing how much of the 20% of the total balance is still available to spend on that catrogry) for visualisation.
- For example, if the total balance is set to 200, the user can spend a maximum of 20% of 200 = 40 on each category. Let us say that after certain amount of days the user spend 30 on food, then the user page will show a 75% filled bar for the food category (30/40 = 0.75). 

## 4. Possible Future Improvements
- A feature where the user can suggest updates to their budget, which can be approved by the admin.
- Smarter progress bars, e.g., negative balance, changing colour, animations.
- A better and secure login system.
