# What am I

xmler is a python package for converting python dictionaries into valid XML. Most XML conversion utilities out there don't seem to provide any namespace support, which was my main reason for creating this package. Inspiration was drawn from the current most popular dictionary to  XML conversion utility [dicttoxml](https://github.com/quandyfactory/dicttoxml).

# Details

xmler has a very specific api that it abides by and, for now, doesn't have very good error handling. Getting namespace support with python dictionaries is not easy so there may be some quirks.

To be used with this package your dictionary must be formatted in the following way:

```python
import dict2xml from xmler

myDict = {
	"RootTag": {						# The root tag. Will not necessarily be root. (see #customRoot)
		"@ns": "soapenv",			# The namespace for the RootTag. The RootTag will appear as <soapenv:RootTag ...>
		"@attrs": {						# @attrs takes a dictionary. each key-value pair will become an attribute
			{ "xmlns:soapenv": "http://schemas.xmlsoap.org/soap/envelope/" }
		},
		"childTag": {
			"@attrs": {
				"someAttribute": "colors are nice"
			},
			"grandchild": "This is a text tag"
		}
	}
}

print(dict2xml(myDict, pretty=True, customRoot=None))
```

Which will return the following XML:

```xml
<soapenv:RootTag xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
	<childTag someAttribute="colors are nice">
		<grandchild>This is a text tag</grandchild>
	</childTag>
</soapenv:RootTag>
```

As you can see if a key is given a string rather than a dictionary it becomes a text tag.

# API

### Options

#### @ns

The namespace option. Adds the supplied namespace to the element.

**Example:**

Python input:
```python
myDict = {
	"RootTag": {
		"@ns": "soapenv"
	}
}
```

Pretty XML Output:
```xml
<soapenv:RootTag />
```

#### @attrs

The attributes option takes a dictionary of attributes. The key for each becomes the attribute itself, while the value becomes the attribute's value.

**Example:**

Python input:
```python
myDict = {
	"RootTag": {
		"@ns": "soapenv",
		"@attrs": {
			"xmlns:soapenv": "http://schemas.xmlsoap.org/soap/envelope/"
		}
	}
}
```

Pretty XML Output:
```xml
<soapenv:RootTag xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" />
```

#### @name

Changes the name of the tag.

*Example:*

Python input:
```python
myDict = {
	"RootTag": {
		"@ns": "soapenv",
		"@attrs": {
			"xmlns:soapenv": "http://schemas.xmlsoap.org/soap/envelope/"
		},
		"@name": "SomethingElse"
	}
}
```

Pretty XML Output:
```xml
<soapenv:SomethingElse xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" />
```

#### @value

Allows you to give the tag a string value rather than having nested tags.

**Example:**

Python input:
```python
myDict = {
	"RootTag": {
		"@ns": "soapenv",
		"@attrs": {
			"xmlns:soapenv": "http://schemas.xmlsoap.org/soap/envelope/"
		},
		"@value": "Namespace test",
		"@name": "SomethingElse"
	}
}
```

Pretty XML Output:
```xml
<soapenv:SomethingElse xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">Namespace test</soapenv:SomethingElse>
```

### Tags

Tags are defined by using a key value for the dictionary that does not start with a `@`. For now no syntax checking is being done on tag names, so use this wisely.

The value of the dictionary key can be either a dictionary or a string. If a dictionary is used you can define a namespace, attributes, name, and value for the tag. If a string is supplied you can only have a basic tag with text content.

**Example:**

```python
# The following two tags are exactly the same,
# but defined in a different way

myDict = {
	"SomeTag": {
		"@value": "Some value"
	},
	"SomeTag": "Some value"
}
```

# Installation

xmler is [published to PyPi](https://pypi.python.org/pypi/xmler), so installing it is as easy as:

```shell
pip install xmler
```

OR

```shell
easy_install xmler
```

You can also download the installer as a tar archive and install it using python with:

```shell
python setup.py install
```

# Author

+ Author: Chris Watson
+ Email: chris@marginzero.co
+ Repository: http://github.com/iDev0urer/xmler

# Version

+ Version: 0.1.0
+ Release date: 2016-08-09

# Revision History

## Version 0.1.0
+ Release date: 2016-08-09
+ Changes:
	- Initial commit

# Copywrite and License

Copywrite 2016 by Christopher Watson

Released under the GNU General Public Licence, Version 2:
http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
