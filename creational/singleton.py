class Singleton:
    # Here will be the instance stored
    __instance = None

    @staticmethod
    def get_instance():
        """Static access method"""
        if not Singleton.__instance:
            return Singleton()
        return Singleton.__instance

    def __init__(self):
        """Virtually private constructor"""
        if Singleton.__instance:
            raise Exception("This class is a Singleton")
        else:
            Singleton.__instance = self


if __name__ == '__main__':
    s = Singleton()
    print(s)

    s1 = Singleton.get_instance()
    print(s1)

    # s = Singleton() # will be failed, raise an exception

    s2 = Singleton.get_instance()
    print(s2)