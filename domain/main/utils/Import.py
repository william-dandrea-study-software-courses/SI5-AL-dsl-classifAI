class Import:

    def __init__(self, package: str, method: str = None, as_name: str = None):
        self.__package: str = package
        self.__method: str = method
        self.__as_name: str = as_name

    def export(self) -> str:

        if self.__method is None and self.__as_name is None:
            return f'import {self.__package}\n'

        if self.__method is None and not (self.__as_name is None):
            return f'import {self.__package} as {self.__as_name}\n'

        if self.__method is not None and self.__as_name is None:
            return f'from {self.__package} import {self.__method}\n'

        raise Exception(
            f'Cannot parse import : "Import(package={self.__package}, method={self.__method}, as_name={self.__as_name})"')
