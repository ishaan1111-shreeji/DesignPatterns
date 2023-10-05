# It is used to describe the formation of a single instance of class
# while offering a single global access point to the object.
class GovtSingleton:
    __instance__ = None

    def __init__(self):
        # This is a Constructor

        if GovtSingleton.__instance__ is None:
            GovtSingleton.__instance__ = self
        else:
            raise Exception("We can not creat another class")

    @staticmethod
    def get_instance():
        # We define the static method to fetch instance
        if not GovtSingleton.__instance__:
            GovtSingleton()
        return GovtSingleton.__instance__


data = GovtSingleton()
print(data)
same_data = GovtSingleton.get_instance()
print(same_data)
another_data = GovtSingleton.get_instance()
print(another_data)
# we can access instance at by .get_instance in static method but we cannot create
# new object of it.
# new_data=GovtSingleton()
# print(new_data)
another_data_1 = GovtSingleton.get_instance()
print(another_data_1)
#In the project, where we need a firm control over the global variables, we must use the Singleton Method.
# Singleton patterns solves the most occurring problems such as logging, caching, thread pools, and configuration setting and often used in conjunction with the Factory design pattern.
