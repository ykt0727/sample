from file import File
class FileTxt(File):
    def set_txt(self, val):
        with open(self.path, 'w', encoding='utf-8') as f:
            f.write(str(val))
    
    def get_txt(self):
        with open(self.path, 'r', encoding='utf-8') as f:   
            return f.read()