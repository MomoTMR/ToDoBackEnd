from typing import List
import os
import json
class EntryManager:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.entries: List[Entry] = []

    def save(self):
        for item in self.entries:
            item.save(self.data_path)

    def load(self):
        for filename in os.listdir(self.data_path):
            file_path = os.path.join(self.data_path, filename)
            if file_path.endswith('.json') == True:
                self.entries.append(Entry.load(file_path))

    def add_entry(self, title: str):
        self.entries.append(Entry(title))
def print_with_indent(value, indent=0):
    indetion = '\t' * indent
    print(indetion + str(value))


class Entry:
    def __init__(self, title, entries=None, parent=None):
        if entries is None:
            entries = []
        self.title = title
        self.entries = entries
        self.parent = parent

    def __str__(self):
        return self.title

    def add_entry(self, Entry):
        self.entries.append(Entry)
        Entry.parent = self

    def print_entries(self, indent=0):
        print_with_indent(self, indent)
        for entry in self.entries:
            entry.print_entries(indent + 1)

    def json(self):
        res = {
            'title': self.title,
            'entries': [entry.json() for entry in self.entries]
        }
        return res

    def save(self, path):
        filename = os.path.join(path, f'{self.title}.json')
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.json(), f)

    @classmethod
    def load(cls, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = json.load(f)
            return cls.from_json(content)

    @classmethod
    def from_json(cls, value: dict):
        new_e = cls(value['title'])
        for item in value.get('entries', []):
            new_e.add_entry(cls.from_json(item))
        return new_e


grocery_list = {
    "title": "Продукты",
    "entries": [
        {
            "title": "Молочные",
            "entries": [
                {
                    "title": "Йогурт",
                    "entries": []
                },
                {
                    "title": "Сыр",
                    "entries": []
                }
            ]
        }
    ]
}


# category = Entry('Гости')
# usr1 = Entry('Гость1')
# usr2 = Entry('Гость2')
# category.add_entry(usr1)
# category.add_entry(usr2)
# usr1.add_entry(Entry('Ержан'))
# usr1.add_entry(Entry('m'))
# usr2.add_entry(Entry('Асылбек'))
# usr2.add_entry(Entry('m'))

# res = category.json()
# print(grocery_list)
# print(json.dumps(grocery_list,ensure_ascii=False, indent = 4))
# res1 = Entry.from_json(grocery_list)
# res1.print_entries()
# print(res1.json())
