"""
You're building a ticket infor system for a railway app.
Based on seat type,show its features:

Task:
    1) Input: `Sleeper`, `AC`, `General`, `Luxury`
    2) Match using `match-case`
    3) Unknown --> show : `Invalid seat type`
"""
seat_type = input("Enter seat type (Sleeper/AC/General/Luxury): ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper: Non-AC, Berths available")
    case "ac":
        print("AC: Air-conditioned, Comfortable seating")
    case "general":
        print("General: Cheapest option, No reservations")
    case "luxury":
        print("Luxury: Premium AC, Extra amenities")
    case _:
        print("Invalid seat type")