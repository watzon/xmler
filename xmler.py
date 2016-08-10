#!/usr/bin/env python
# coding: utf-8

"""
Converts a Python dictionary to a valid XML string
"""

from __future__ import unicode_literals

__version__ = '0.1.0'
version = __version__

from xml.dom.minidom import parseString
import logging

LOG = logging.getLogger("xmler")

class XmlTag(object):

    def __init__(self, name="key", children=None, namespace=None,
                attributes=None, self_close=True):
        self.name = name
        self.children = children if children else []
        self.namespace = namespace
        self.attributes = attributes if attributes else {}
        self.self_close = self_close

    def to_string(self):

        attrs = ""
        children = ""
        name = "%s:%s" % (self.namespace, self.name) if self.namespace else self.name
        has_children = len(self.children) > 0

        # Build the temp string based on whether or not the element has children
        if self.self_close and not has_children:
            temp = "<{0}{1}/>"
        elif has_children:
            temp = "<{0}{1}>{2}</{0}>"
        else:
            temp = "<{0}{1}></{0}>"

        # Iterate over the attributes and build a new string of attribute keys
        # to values like so: key="value"
        print(attrs)
        for key, attr in self.attributes.items():
            attr_string = "%s=\"%s\" " % (key, attr)
            attrs = "%s %s" % (attrs, attr_string)

        # Loop through the children. If the child is a string we need to just
        # add it, but if it's an instance of XmlTag we need to call the format
        # function and add that
        for child in self.children:
            if (type(child) is str):
                children = "%s%s" % (children, child)
            elif(type(child) is XmlTag):
                children = "%s%s" % (children, child.to_string())

        if has_children:
            return temp.format(name, attrs, children)
        else:
            return temp.format(name, attrs)

    def pretty_print(self):
        "Pretty prints the output"
        return parseString(self.to_string()).toprettyxml()

    def addprop(self, name, method):
        cls = type(self)
        if not cls.hasattr('__perinstance'):
            cls = type(cls.__name__, (cls,), {})
            cls.__perinstance = True
        setattr(cls, name, property(method))

def deep_to_dict(obj, namespace=None):
    for key, value in obj.items():
        is_option = key[0] == "@"
        if not is_option:
            if type(value) is not dict:
                d = {}


def dict2xml(dic, encoding="UTF-8", customRoot="root", pretty=False):
    """Converts a python dictionary into a valid XML string

    Args:
        - encoding specifies the encoding to be included in the encoding
          segment. If set to False no encoding segment will be displayed.
        - customRoot defines the tag to wrap the returned output. Can be
          a string, dictionary, or False if no custom root is to be used.

    Returns:
        A XML formatted string representing the dictionary.

    Examples:
        ```
        dic = {
            "Envelope": {
                "@ns": "soapenv",
                "@attrs": {
                    "xmlns:soapenv": "http://schemas.xmlsoap.org/soap/envelope/",
                    "xmlns:urn": "urn:partner.soap.sforce.com"
                },
                "Header": {
                    "@ns": "soapenv",
                    "SessionHeader": {
                        "@ns": "urn",
                        "sessionId": {
                            "@ns": "urn",
                            "@value": "00D36000000b28L!ARsAQMtHo4XD71VYRxoz"
                        }
                    }
                },
                "Body": {
                    "@ns": "soapenv",
                    "query": {
                        "@ns": "urn",
                        "queryString": {
                            "@ns": "urn",
                            "@value": "SELECT Id, Name FROM Account LIMIT 2"
                        }
                    }
                }
            }
        }

        xml = xml2dict(dict, customRoot=False)
        print(xml)
        ```

        output:
        ```
        <?xml version="1.0" encoding="UTF-8"?>
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
          xmlns:urn="urn:partner.soap.sforce.com">
          <soapenv:Header>
             <urn:SessionHeader>
                <urn:sessionId>{0}</urn:sessionId>
             </urn:SessionHeader>
          </soapenv:Header>
        </soapenv:Envelope>
        ```
    """

    root = None
    if customRoot:
        if type(customRoot) is str:
            root = XmlTag(name=customRoot)
        elif type(customRoot) is dict:
            root = parseDict(customRoot)

    encoding_string = "<?xml version=\"1.0\" encoding=\"{0}\"?>".format(encoding) if encoding else ""
    xml_string = encoding_string + parseDict(dic, root=root, pretty=pretty)

    return xml_string

def xml2dict():
    pass

def parseDict(dic, root=None, pretty=False):

    for key, value in dic.items():

        child = XmlTag()
        is_option = key[0] == "@"

        if is_option:
            option = key[1:]
            if option == "ns":
                root.namespace = value
            elif option == "name":
                root.name = value
            elif option == "attrs":
                root.attributes = value
            elif option == "value":
                if type(value) is dict:
                    v = parseDict(value)
                    root.children.append(v)
                else:
                    root.children.append(value)
            else:
                print("Property %s does not exist on type XmlTag" % option)

        elif type(value) is dict:
            child.name = key
            child2 = parseDict(value, root=child)

            if root:
                root.children.append(child2)
            else:
                root = child

        else:
            child.name = key
            child.children.append(value)

            if root:
                root.children.append(child)
            else:
                root = child

    return root.pretty_print() if pretty else root.to_string()
