


class Note:
    id_counter = 1
    def __init__(self, text, time):
        self.id = f'{Note.id_counter} {time}'
        self.text = text
        self.tags = []
        

    def add_tag(self, tags):
        for tag in tags:
            if tag not in self.tags:
                self.tags.append(tag)

    def remove_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)

    def show_note(self):
        return f"ID: {self.id}, Text: {self.text}, Tags: {', '.join(self.tags)}"
    

    def __repr__(self) -> str:
        return f"        ID: {self.id}\n{self.text}\n\nTags: {', '.join(self.tags)}"
