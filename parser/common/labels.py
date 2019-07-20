class Label(object):

    @staticmethod
    def from_int(value):
        assert(isinstance(value, int))
        for l in Label._get_supported_labels():
            if l.to_int() == value:
                return l
        raise Exception("Label by value '{}' doesn't supported".format(value))

    @staticmethod
    def _get_supported_labels():
        supported_labels = [
            PositiveLabel(),
            NegativeLabel()
        ]
        return supported_labels

    def to_int(self):
        raise NotImplementedError()


class PositiveLabel(Label):

    def to_int(self):
        return int(1)


class NegativeLabel(Label):

    def to_int(self):
        return int(-1)

