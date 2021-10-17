'''
def html_creator(tag):
    def text_wrapper(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))
    return text_wrapper


h1_html_creator = html_creator('h1')
h1_html_creator('H1 태크는 타이틀')
'''


def index_creator(tag):
    def text_wrapper(list_data):
        for i in list_data:
            print('{0} {1}'.format(tag, i))
    return text_wrapper


list_data = ['야호', '무야호']
ex_index_creator = index_creator('-')
ex_index_creator(list_data)
