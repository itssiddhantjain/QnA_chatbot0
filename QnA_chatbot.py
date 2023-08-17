import re

class OrderBot:
    def process_input(self, user_input):
        if "cancel" in user_input:
            if "shipped" in user_input:
                return "To cancel orders that are already shipped:\n" \
                       "1. Go to Your Orders\n" \
                       "2. Select the Request cancellation option and proceed further\n" \
                       "3. The item(s) will be returned to us for a refund (if the payment is already made)\n" \
                       "In case you're still contacted for delivery, please refuse to accept it."
            else:
                return "To cancel orders that are not shipped yet:\n" \
                       "1. Go to Your Orders\n" \
                       "2. Select the item you want to cancel and click Cancel items\n" \
                       "3. Provide reasons for cancellation (optional) and proceed"
        else:
            return "I'm sorry, I can't understand your request."

def main():
    bot = OrderBot()
    print("Welcome to the OrderBot!")

    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print("OrderBot: Goodbye!")
            break

        response = bot.process_input(user_input)
        print("OrderBot:", response)

if __name__ == "__main__":
    main()
