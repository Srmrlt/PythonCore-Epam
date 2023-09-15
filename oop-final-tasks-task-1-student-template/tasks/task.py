class Sun:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls.inst = super().__new__(cls, *args, **kwargs)
        return cls._instance

    @staticmethod
    def inst():
        pass
