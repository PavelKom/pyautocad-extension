

class Collection(object):
    def __init__(self, obj):
        self.me = obj

    def Add(self, item, key=None, before=None, after=None):
        kw = dict()
        kw["Item"] = item
        if key is not None:
            kw["Key"] = key
        if before is not None:
            kw["Before"] = before
        if after is not None:
            kw["after"] = after
        return self._add(kw)

    def _add(self, kwargs):
        self.me.Add(**kwargs)
        """
        match key, before, after:
            case None, None, None:
                self.me.Add(obj)
            case str(), None, None:
                self.me.Add(obj, key)
            case None, int(), None:
                """