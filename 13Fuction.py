def exam_arg(*args):
    print(args)
    print(args[1])
    print(type(args))

exam_arg('test','출력',123)
#가변인자

def exam_args(**kwargs):
    print(kwargs)
    print(type(kwargs))

exam_args(key='test',word='출력',args=123)
#가변키워드인자

#docstring

def exam_docstring(*args):
    """

    :param args:
    :return:
    """