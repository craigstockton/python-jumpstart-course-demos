import os


class Journal:
    file_path = os.path.abspath(os.path.join('./default.jrn'))

    def __init__(self, entries=''):
        """
        A journal stored as a file.

        :param entries: List of entries to be appended to the end of the current journal.
        """
        print('... loading journal from {} ...'.format(self.file_path))
        self.content = []
        if os.path.exists(self.file_path):
            with open(self.file_path) as journal_file:
                for entry in journal_file.readlines():
                    self.content.append(entry.rstrip())
        if entries:
            for entry in entries:
                self.content.append(entry)
        entry_count = len(self.content)
        print('... loaded {} entr{}'.format(entry_count, 'y' if entry_count == 1 else 'ies'))

    def save(self):
        """
        Write the entries to journal file 'default.jrn'.

        :return: None
        """
        print('... saving to {} ...'.format(self.file_path))
        with open(self.file_path, 'w') as journal_file:
            for entry in self.content:
                journal_file.write('{}\n'.format(entry))
        print('... save complete ...', )
        journal_file.close()

    def list(self):
        """
        Display the journal entries.

        :return: All entries, numbered, in reverse order (LIFO).
        """
        entries_ordered = reversed(self.content)
        entry_count = len(self.content)
        return_string = 'Your {} journal entr{}\n\n'.format(entry_count, 'y' if entry_count == 1 else 'ies')
        for index, entry in enumerate(entries_ordered):
            entry_numbered = '{}. {}'.format(index + 1, entry)
            return_string += '{}\n'.format(entry_numbered)
        return return_string

    def add(self, entry):
        """
        Add a new entry to the journal

        :param entry: Any value
        :return: None
        """
        self.content.append(entry)
