from elem import Elem, Text


class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('html', attr, content, 'double')


class Head(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('head', attr, content, 'double')


class Body(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('body', attr, content, 'double')


class Title(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('title', attr, content, 'double')


class Meta(Elem):
    def __init__(self, attr={}):
        super().__init__('meta', attr, None, 'simple')


class Img(Elem):
    def __init__(self, attr={}):
        super().__init__('img', attr, None, 'simple')


class Table(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('table', attr, content, 'double')


class Th(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('th', attr, content, 'double')


class Tr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('tr', attr, content, 'double')


class Td(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('td', attr, content, 'double')


class Ul(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('ul', attr, content, 'double')


class Ol(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('ol', attr, content, 'double')


class Li(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('li', attr, content, 'double')


class H1(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('h1', attr, content, 'double')


class H2(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('h2', attr, content, 'double')


class P(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('p', attr, content, 'double')


class Div(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('div', attr, content, 'double')


class Span(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('span', attr, content, 'double')


class Hr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('hr', attr, content, 'simple')


class Br(Elem):
    def __init__(self):
        super().__init__('br', {}, None, 'simple')


if __name__ == "__main__":
    elem_title = Title(Text("Hello ground!"))
    elem_meta = Meta({"charset": "utf-8"})
    elem_head = Head([elem_meta, elem_title], {"lang": "fr"})
    elem_h2 = H2(Text("BURNET Lucille"))
    elem_h1 = H1(Text("CV pour la Piscine Django"))
    elem_br = Br()
    elem_p = P([Text("parce qu'il faut bien la tester aussi"), elem_br])
    elem_img = Img({"src": "http://i.imgur.com/pfp3T.jpg"})
    elem_div = Div([elem_p, elem_img])
    elem_li = Li(Text("Algorithmique, Techniques d'optimisation et IA"))
    elem_ul = Ul(elem_li)
    elem_ol = Ol(elem_li)
    elem_span = Span([elem_ol, elem_ul])
    elem_th = Th(Text("Langues"), {"colspan": "2"})
    elem_tr0 = Tr(elem_th)
    elem_thead = Elem(tag='thead', content=elem_tr0)
    elem_td0 = Td()
    elem_td1 = Td(Text("niveau"))
    elem_tr1 = Tr([elem_td0, elem_td1])
    elem_tbody = Elem(tag='tbody', content=elem_tr1)
    elem_table = Table([elem_thead, elem_tbody])
    elem_hr = Hr()
    elem_body = Body([elem_h2, elem_h1, elem_div, elem_span, elem_table, elem_hr])
    elem_html = Elem(tag='html', content=[elem_head, elem_body], attr={'lang': 'fr'})
    print(elem_html)