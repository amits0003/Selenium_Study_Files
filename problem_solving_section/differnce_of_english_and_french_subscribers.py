
n_english = int(input())
english_subscribers = input().split(" ")
n_french = int(input())
french_subscribers = input().split(" ")

differnce_arr = set(english_subscribers).difference(french_subscribers)

print(len(differnce_arr))

symmetric_differnce_arr = set(english_subscribers).symmetric_difference(french_subscribers)

print(len(symmetric_differnce_arr))
