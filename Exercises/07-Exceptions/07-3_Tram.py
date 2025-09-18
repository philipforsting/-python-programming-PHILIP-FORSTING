while True:
    try:
        rides_month = int(input("How many times do you take tram in one month? "))
        if not 0 <= rides_month <= 100:
            raise ValueError("Number of times you take tram must be between 0 and 100")
        one_ticket_price = float(input("How much does one ticket cost? (kr) "))
        if not 0 <= one_ticket_price <= 100:
            raise ValueError("One ticket must cost between 0 and 100 kr")
        month_ticket_price = float(input("How much does one month card cost? (kr) "))
        if not 0 <= month_ticket_price <= 2000:
            raise ValueError("Month ticket must cost between 0 and 2000 kr")

        print(f"Cost with one-time tickets {rides_month*one_ticket_price}")
        print(f"Cost with monthly card {month_ticket_price}")
        print(f"It's worth to buy a monthly card") if month_ticket_price < rides_month*one_ticket_price else print(f"It's not worth to buy a monthly card")

        break # breaks out of while loop if nothing went wrong
    except ValueError as err:
        print(err)
    

