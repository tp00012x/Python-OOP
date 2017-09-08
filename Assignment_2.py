import abc, csv

class WriteFile(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, file):
        self.file = file

    @abc.abstractclassmethod
    def write(self, message):
        return

class LogFile(WriteFile):

    def write(self, message):
        with open(self.file, "a") as txt_file:
            txt_file.write(message + "\n")


class DelimFile(WriteFile):

    def __init__(self, file, deli):
        super().__init__(file)
        self.deli = deli

    def write(self, message):
        with open(self.file, "a") as csv_file:
            writer = csv.writer(csv_file, delimiter=self.deli)
            writer.writerow(message)


log = LogFile('log.txt')
c = DelimFile('text.csv', ',')

log.write('this is a log message')
log.write('this is another log message')

c.write(['a', 'b', 'c', 'd'])
c.write(['1', '2', '3', '4'])
