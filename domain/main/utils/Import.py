class Import:

    def __init__(self, package: str, method: str = None, as_name: str = None):
        self.package: str = package
        self.method: str = method
        self.as_name: str = as_name

    def export(self) -> str:

        if self.method is None and self.as_name is None:
            return f'import {self.package}'

        if self.method is None and not (self.as_name is None):
            return f'import {self.package} as {self.as_name}'

        if self.method is not None and self.as_name is None:
            return f'from {self.package} import {self.method}'

        raise Exception(
            f'Cannot parse import : "Import(package={self.package}, method={self.method}, as_name={self.as_name})"')
