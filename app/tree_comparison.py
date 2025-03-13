import timeit
from BTrees.OOBTree import OOBTree


class TreeContainer:
    def __init__(self):
        self.tree = OOBTree()

    def add_item_to_tree(self, key, item):
        self.tree[key] = item

    def range_query_tree(self, min_prise, max_prise):
        return [item for _, item in self.tree.items(min_prise, max_prise) if min_prise <= item['price'] <= max_prise]

class DictContainer:
    def __init__(self):
        self.items = {}

    def add_item_to_dict(self, key, item):
        self.items[key] = item

    def range_query_dict(self, min_prise, max_prise):
        return [item for item in self.items.values() if min_prise <= item['price'] <= max_prise]


dict_container = DictContainer()
tree_container = TreeContainer()


def load_data(add_item):
    import csv

    with open("data/generated_items_data.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        count = 0
        for row in reader:
            add_item(int(row["ID"]), {
                "name": row["Name"],
                "category": row["Category"],
                "price": float(row["Price"]),
            })
            count = count + 1
        print(f"Data loaded: {count} items")


load_data(dict_container.add_item_to_dict)
load_data(tree_container.add_item_to_tree)

execution_time = timeit.timeit(lambda: dict_container.range_query_dict(150, 275), number=100)
print(
    f"Total range_query time for Dict: {execution_time:.5f} seconds."
)

execution_time = timeit.timeit(lambda: tree_container.range_query_tree(150, 275), number=100)
print(
    f"Total range_query time for OOBTree: {execution_time:.5f} seconds."
)
