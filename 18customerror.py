class Myerror(Exception):
    def __str__(self):
        return "My custom error"

try:
    raise Myerror()
except Exception as e:
    print(e)