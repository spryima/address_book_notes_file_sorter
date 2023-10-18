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

    def edit_note(self, ui):
        ui.show_message('Here you can retype your note')
        self.text = ui.user_input('>')
        ui.show_message(self.tags)
        ui.show_green_message('Wanna change some tags? Type it (comma separated)  [Enter to skip]:')
        tags = set(ui.user_input('>').split())
        if tags:
            self.tags = tags


    def __repr__(self) -> str:
        return '~' * 50 + f"\n        ID: {self.id}\n\n{self.text}\n\nTags: {' '.join(self.tags)}\n\n" + '~' * 50
