class Note:
    id_counter = 1
    def __init__(self, text, time):
        self.id = f'{Note.id_counter} {time}'
        self.text = text
        self.tags = set()
        Note.id_counter += 1
        

    def add_tag(self, tags):
        for tag in tags:
            if tag not in self.tags:
                self.tags.add(tag)

    def remove_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)

    def show_note(self):
        return '~' * 50 + f"\n        ID: {self.id}\n\n{self.text}\n\nTags: {' '.join(self.tags)}\n\n" + '~' * 50
    

    def __repr__(self) -> str:
        return '~' * 50 + f"\n        ID: {self.id}\n\n{self.text}\n\nTags: {' '.join(self.tags)}\n\n" + '~' * 50
