# campus
build a campus Resources Management System

List the problems out
1. func that stores resource inventory, issue item(give), accepts return, search inventory and produces accurate reports.

data needed:
1. resource inventory; should have unique ID number, name(string), category(string), total unit(int), and availabe unit(int), Add and list, reject duplicates IDs(err).

2. Borrowing; check fellow and resource ID(auth), quantity only possitive numbers and not less than stock, log(write) a successful borrow record, regect attemp must not mutate(change) state

3. Returns; Only return quantity(int) a fellow only has as loan; update both borrowing record and invetory.

4. search/filter; case sensitive name search; filter by category.

5. Reports; show total units(int), available units(int), units(int) currently borrowed, resources with fewer than 3 available unit and resources with most units currently borrowed. if tied(same unit number of currently borrowed item), identify all tied leaders

6. structure/robustness; meaningfull functions, menu that loops until exit, input validation and helpful errors. 