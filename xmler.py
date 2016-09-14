#!/usr/bin/env python
# coding: utf-8

"""
Converts a Python dictionary to a valid XML string
"""

from __future__ import unicode_literals

__version__ = '0.2.0'
version = __version__

from xml.dom import minidom
from xml.etree.ElementTree import Element, tostring

import logging

def dict2xml(dict, encoding="utf-8", pretty=False):
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

    import ipdb;
    ipdb.set_trace()

    xml_string = tostring(parse(dict, pretty=pretty), encoding=encoding)

    if pretty:
        xml_pretty_string = minidom.parseString(xml_string)
        return xml_pretty_string.toprettyxml().decode(encoding)
    else:
        return xml_string.decode(encoding)


def parse(dict, parent={}, pretty=False):

    for key, value in dict.items():

        if '@ns' in value:
            parent['namespace'] = value['@ns']
            value.pop('@ns')

        if '@attrs' in value:
            parent['attributes'] = value['@attrs']
            value.pop('@attrs')

        if '@name' in value:
            parent['name'] = value['@name']
            value.pop('@name')
        else:
            parent['name'] = key

        if '@value' in value:
            parent['value'] = value = value['@value']
        else:
            parent['value'] = value

    if 'namespace' in parent:
        parent['name'] = "%s:%s" % (parent['namespace'], parent['name'])

    if 'attributes' in parent:
        element = Element(parent['name'], parent['attributes'])
    else:
        element = Element(parent['name'])

    if isinstance(parent['value'], str):
        element.text = parent['value']
    else:
        for child_key, child_value in value.items():
            element.append(parse({child_key: child_value}, parent={}))

    return element
