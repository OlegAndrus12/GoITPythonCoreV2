# encapsulation: control what is public, protected, or private
#
#   no prefix  — public: part of the interface, use freely
#   _single    — protected: internal detail, "don't touch from outside" (convention only)
#   __double   — private: name-mangled by Python, truly hard to reach from outside


class GPTClient:
    _base_url = "https://api.openai.com/v1"  # protected class attribute

    def __init__(self, api_key, model):
        self.model = model              # public: callers can read and change the model
        self._history = []              # protected: managed internally, not part of API
        self.__api_key = api_key        # private: must never leak outside the class

    def chat(self, message):
        self._history.append({"role": "user", "content": message})
        response = self._call_api(message)
        self._history.append({"role": "assistant", "content": response})
        return response

    def _call_api(self, message):
        # protected: internal helper, not meant to be called directly
        return f"[mock response to: '{message}']"

    def clear_history(self):
        self._history = []

    @property
    def api_key(self):
        return f"****{self.__api_key[-4:]}"   # expose only masked version

    def __repr__(self):
        return f"GPTClient(model={self.model}, key={self.api_key})"


client = GPTClient("sk-supersecret-0042", "gpt-4o")

# public — fine to use anywhere
print(client.model)
client.model = "gpt-4o-mini"

# property — read-only masked access to the private key
print(client.api_key)         # ****0042

# chat — public method
print(client.chat("What is Python?"))
print(client.chat("Give me an example"))
print(client._history)        # accessible but signals "internal"

# __api_key is private — accessing it directly raises AttributeError
# print(client.__api_key)              # AttributeError
print(client._GPTClient__api_key)      # Python's name mangling — avoid in real code

print(client)
