class MySingleton:
    _singleton = None

    def __new__(cls, *args, **kwargs):
        if cls._singleton is None:
            cls._singleton = super(MySingleton, cls).__new__(cls, *args, **kwargs)
        return cls._singleton
