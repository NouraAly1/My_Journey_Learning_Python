# Weather-Based Clothing Recommendation
# This program suggests what to wear based on the weather condition

# Get weather input from user and convert to lowercase, strip whitespace
weather = input("how is the weather?").lower().strip()

# Provide clothing recommendations based on weather
if weather == "sunny":
    print("Wear glasses")
elif weather == "cold":
    print("Wear a jacket")
elif weather == "rainy":
    print("Take an umbrella")
else:
    print("Sorry, I don't understand:", weather)