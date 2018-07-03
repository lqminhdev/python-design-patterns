class VietnameseGetter(object):
    def __init__(self):
        self.trans = dict(dog='Cho', cat='Meo')

    def get(self, msg_id):
        return self.trans.get(msg_id, str(msg_id))


class EnglishGetter(object):
    def get(self, msg_id):
        return str(msg_id)


def get_localizer(language='English'):
    """The Factory Method"""
    languages = dict(English=EnglishGetter, Vietnamese=VietnameseGetter)
    return languages[language]()


if __name__ == '__main__':
    # Create some localizers
    e, v = get_localizer(language='English'), get_localizer(language='Vietnamese')
    # Localize some text
    for msg_id in "dog parrot cat bear".split():
        print(e.get(msg_id), v.get(msg_id))