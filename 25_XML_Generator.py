def XML_generator(tag, body='', **attributes):
    attrs = ''.join([f' {key}="{value}"' for key, value in attributes.items()])
    xml = f'<{tag}{attrs}>{body}</{tag}>'
    return print(xml)

XML_generator('foo', 'bar', a=1, b=2, c=3)