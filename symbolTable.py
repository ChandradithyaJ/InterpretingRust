from collections import OrderedDict

class Symbol(object):
    def __init__(self, name, type=None):
        self.name = name
        self.type = type

class BuiltinTypeSymbol(Symbol):
    def __init__(self, name):
        super(BuiltinTypeSymbol, self).__init__(name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<{class_name}(name='{name}')>".format(
            class_name=self.__class__.__name__,
            name=self.name,
        )

class VarSymbol(Symbol):
    def __init__(self, name, type):
        super(VarSymbol, self).__init__(name, type)

    def __str__(self):
        return "<{class_name}(name='{name}', type='{type}')>".format(
            class_name=self.__class__.__name__,
            name=self.name,
            type=self.type,
        )

    __repr__ = __str__

class SymbolTable(object):
    def __init__(self):
        self._symbols = OrderedDict()


    def __str__(self):
        s = 'Symbols: {symbols}'.format(
            symbols=[value for value in self._symbols.value()]
        )
        return s

    __repr__ = __str__

    def __init_builtins(self):
        self.insert(BuiltinTypeSymbol('let'))

    def insert(self, symbol):
        # inserting a symbol name
        self._symbols[symbol.name] = symbol

    def define(self, symbol):
        print('Define %s' % symbol)
        self._symbols[symbol.name] = symbol

    def lookup(self, name):
        print('Lookup: %s' % name)
        symbol = self._symbols.get(name)
        # 'symbol' is either an instance of the Symbol class or 'None'
        return symbol

