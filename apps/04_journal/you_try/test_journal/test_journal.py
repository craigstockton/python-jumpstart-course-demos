import os

from journal import Journal

file_path = './default.jrn'


def test_journal_save():
    if os.path.exists(file_path):
        os.remove(file_path)
    expected = True
    Journal().save()
    actual = os.path.exists(file_path)
    assert expected == actual


def test_journal_list():
    if os.path.exists(file_path):
        os.remove(file_path)
    entry_1 = 'This is my first entry journal entry'
    entry_2 = 'Now we have excellent history features.'
    entry_3 = 'What a sunny Saturday. Time for some exercise!'
    entries = [entry_1, entry_2, entry_3]
    listing = '1. {}\n2. {}\n3. {}\n'.format(entry_3, entry_2, entry_1)
    expected = 'Your 3 journal entries\n\n{}'.format(listing)
    actual = Journal(entries).list()
    assert expected == actual


def test_journal_add_new_content():
    if os.path.exists(file_path):
        os.remove(file_path)
    entry_1 = 'This is my first entry journal entry'
    expected = 'Your 1 journal entry\n\n1. {}\n'.format(entry_1)
    journal = Journal()
    journal.add(entry_1)
    actual = journal.list()
    assert expected == actual


def test_journal_save_content():
    if os.path.exists(file_path):
        os.remove(file_path)
    entry_1 = 'This is my first entry journal entry'
    expected = '{}\n'.format(entry_1)
    journal = Journal()
    journal.add(entry_1)
    journal.save()
    actual = open(file_path, 'r').read()
    assert expected == actual


def test_journal_add_content():
    if os.path.exists(file_path):
        os.remove(file_path)
    entry_1 = 'This is my first entry journal entry'
    entry_2 = 'Now we have excellent history features.'
    expected = "{}\n{}\n".format(entry_1, entry_2)
    journal = Journal()
    journal.add(entry_1)
    journal.save()
    journal = Journal()
    journal.add(entry_2)
    journal.save()
    actual = open(file_path, 'r').read()
    assert expected == actual


def test_journal_list_empty():
    if os.path.exists(file_path):
        os.remove(file_path)
    expected = 'Your 0 journal entries\n\n'
    actual = Journal().list()
    assert expected == actual
