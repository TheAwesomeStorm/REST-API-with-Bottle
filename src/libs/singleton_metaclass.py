class SingletonMetaclass(type):

    """

    Define a estrutura de uma classe **Singleton**, qualquer classe que utilize esta como **metaclasse** irá restringir
    suas instâncias a somente um objeto

    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """

        Sobreescreve o método **__call__** de :class:`Type`

        Este método invoca *self* como uma função

        """

        if cls not in cls._instances:

            cls._instances[cls] = super(SingletonMetaclass, cls).__call__(*args, **kwargs)

        return cls._instances[cls]
