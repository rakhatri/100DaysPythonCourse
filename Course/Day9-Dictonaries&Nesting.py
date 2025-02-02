# # capitals = {
# #     "France": "Paris",
# #     "Germany": "Berlin",
# # }
# #
# # travel_log = {
# #     "India": ["Jabalpur", "Trivandrum", "Pune", "Delhi"],
# #     "Canada": ["Toronto", "Mississauga", "Brampton"]
# # }
# #
# # print(travel_log["India"][1])
# #
# # nested_list = ["A", "B", ["C", "D"]]
# # print(nested_list[2][1])
#
# travel_log = {
#   "France": {
#     "cities_visited": ["Paris", "Lille", "Dijon"],
#     "total_visits": 12
#    },
#   "Germany": {
#     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#     "total_visits": 5
#    },
# }
#
# print(travel_log["Germany"]["cities_visited"][2])

from Bidding_art import logo

print(logo)
print("Welcome to the secret auction program.")
bids = {}
is_bidding_open = True

while is_bidding_open:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid
    more_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    print("\n" * 20)
    if more_bids == "no":
        is_bidding_open = False
max_bidder = ""
max_bid = 0
for bid in bids:
    if bids[bid] > max_bid:
        max_bidder = bid
        max_bid = bids[bid]
print(f"The winner is {max_bidder} with the bid of ${max_bid}.")


