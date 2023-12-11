#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        return super().__str__().replace(
            '<', '&lt;').replace(
            '>', '&gt;').replace(
            '"', '&quot;').replace(
            '\n', '\n<br />\n'
        )


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    class ValidationError(Exception):
        def __init__(self, *args: object) -> None:
            super().__init__(*args)

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        if type(content) == str and content == '':
            raise Elem.ValidationError()
        self.tag = tag
        self.attr = attr
        # if content == None:
        #     self.content = []
        # elif isinstance(content, list):
        #     self.content = content
        # else:
        #     self.content = [content]
        self.content = ""
        if isinstance(content, str) and content:  # check is type(Text)
            self.content += "\n  " + content + '\n'
        elif isinstance(content, Elem):
            self.content += "\n  "
            self.content += str(content).replace('\n', "\n  ")
            self.content += "\n"
        elif isinstance(content, list):
            for l in content:
                if isinstance(l, str) and l:  # check is type(Text)
                    if self.content == "":
                        self.content += "\n  "
                    self.content += l + "\n  "
                elif isinstance(l, Elem):
                    if self.content == "":
                        self.content += "\n  "
                    self.content += str(l).replace('\n', "\n  ")
                    self.content += "\n  "
        if self.content != "":
            self.content = self.content.rstrip() + "\n"
        self.tag_type = tag_type

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        if self.tag_type == 'double':
            # result = f"<{self.tag}{self.attr}>{self.__make_content()}</{self.tag}>"
            result = f"<{self.tag}{self.__make_attr()}>{self.content}</{self.tag}>"
        elif self.tag_type == 'simple':
            result = f"<{self.tag}{self.__make_attr()} />"
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """
        if len(self.content) == 0:
            return ''
        result = ''
        for elem in self.content:
            # print(f"elem = [{elem}]")
            if isinstance(elem, str) and elem:
                print("Here")
                result += "\n  " + elem + '\n'
            elif isinstance(elem, Elem):
                result += "\n  " + str(elem).replace('\n', "\n  ") + '\n'
            result = result.rstrip() + '\n'
            # print(f"result = [{result}]")
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


if __name__ == '__main__':
    elem_title = Elem(tag="title", content="Hello ground!")
    elem_head = Elem(tag="head", content = elem_title)
    elem_h1 = Elem(tag="h1", content="Oh no, not again!")
    elem_img = Elem(tag="img", attr={"src": "http://i.imgur.com/pfp3T.jpg"}, tag_type='simple')
    elem_body = Elem(tag="body", content=[elem_h1, elem_img])
    elem_html = Elem(tag="html", content=[elem_head, elem_body])
    print(elem_html)
