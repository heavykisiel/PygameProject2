
class Item:
    item_counter = 0

    def __init__(self, item_id_counter=item_counter):
        self.item_id = item_id_counter + 1
        self.item_type = self.item_type_selector(1)
        print(self.item_type)
        self.stats = self.stats_maker(self.item_type)

    def stats_maker(self, item_type):
        if item_type == 0:
            dicto = {
                "slot": None,
                "armor": None,
                "kg": None
            }
            return dicto

    def item_type_selector(self, number):
        item_types = {
            "wearable": 0,
            "weldable": 1,
            "consumable": 2,

        }
        if number < 0:
            raise Exception("item_type_selector: argument number shouldn't be less than 0")
        if number > item_types.__len__():
            raise Exception("item_type_selector: argument number shouldn't be more than {0} (item_types.__len__())"
                            .format(item_types.__len__()))

        return item_types[number]


def itemlist():
    worlds_items = list()
    list.append(Item)