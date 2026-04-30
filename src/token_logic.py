class TokenCalculator:
    def __init__(self, cost_per_token=0.01):
        self.cost_per_token = cost_per_token

    def calculate_tokens(self, input_text):
        tokens = len(input_text.split())
        return tokens

    def spend_credits(self, user, tokens_used):
        x = tokens_used * self.cost_per_token
        if user.credits >= cost:
            user.credits -= cost
            return True
        else:
            return False
