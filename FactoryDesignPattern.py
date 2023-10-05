# The factory method offers us the best way to create an object.
#  In this method, objects are created without revealing the logic to the client.
#  To create a new type of object, the client uses the same common interface.
# class French_language:
#     def __init__(self):
#         self.translate = {"goodmorning": "bonjour", "goodnight": "bonnenuit"}
#
#     def localize(self, msg):
#         return self.translate.get(msg)
#
#
# class German_language:
#     def __init__(self):
#         self.translate = {"goodmorning": "GutenMorgen", "goodnight": "GuteNacht"}
#
#     def localize(self, msg):
#         return self.translate.get(msg)
#
#
# if __name__ == "__main__":
#     f = French_language()
#     g = German_language()
#     message = ["goodnight", "goodmorning"]
#     for msg in message:
#         print(msg, " in french :", f.localize(msg))
#         print(msg, " in german :", g.localize(msg))
#

# in above code different objects are created of different language depending upon user
# requirement, we can use Factory method for this solution instead of creating different
# objects we define a method name Factory and call it depending upon user input.

class French_language:
    def __init__(self):
        self.translate = {"goodmorning": "bonjour", "goodnight": "bonnenuit"}

    def localize(self, msg):
        return self.translate.get(msg)


class German_language:
    def __init__(self):
        self.translate = {"goodmorning": "GutenMorgen", "goodnight": "GuteNacht"}

    def localize(self, msg):
        return self.translate.get(msg)


class English_language:
    def localize(self, msg):
        return msg

# applying factory design
def Factory(language="english"):
    localizer = {
        "french": French_language(),
        "german": German_language(),
        "english": English_language()
    }
    return localizer[language]


if __name__ == '__main__':
    a = German_language()
    print(a.localize('goodmorning'))
    f = French_language()
    print(f.localize('goodmorning'))
    print("*"*50)
    fr = Factory("french")
    gr = Factory("german")
    en=Factory("english")
    message = ["goodnight", "goodmorning"]
    for m in message:
        print(fr.localize(m))
        print(gr.localize(m))
        print(en.localize(m))
#--> Benifits of using Factory Method:
        # factory methods are very useful in adding new types of
        # product without distributing the existing client code.
        # It avoids the tight coupling between the products and the creator classes and objects.
# -->Where to use??
#      ->Replacing complex logical code
    # ->Combining similar features under a common interface

