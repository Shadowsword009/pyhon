n, m, a, b = map(int, input().split())
a1 = n * a
full_tickets = n // m
remaining_rides = n % m
multi_ride_cost = full_tickets * b + min(remaining_rides * a, b)
print(min(a1, multi_ride_cost))
