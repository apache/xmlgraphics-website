import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('fop', help='fop dir')
parser.add_argument('website', help='website dir')
args = parser.parse_args()

class Item:
    def __init__(self, name, var, parent):
        self.name = name
        self.var = var
        self.parent = parent
        self.element = False
        self.attrtype = 'string'

tags = []

def getItem(parent, l):
    tag = None
    var = None
    if '"' in l:
        tag = findTag(l)
        if '_' in l and '(' in l:
            var = l.split('(')[0]
        elif '_' in l and '=' in l:
            var = l.split('=')[0].strip().split(' ')[-1].strip()
    elif '(' in l and ')' in l and '_' in l:
        var = l.split('(')[1].split(')')[0]
        if '.' in var:
            var = var.split('.')[0]
        if ',' in var:
            var = var.split(',')[0]
        if '_' not in var or ' ' in var:
            return None
    else:
        return None
    parent = parent.replace('.java', '')
    parent = parent.replace('Java2D', 'PCL')
    parent = parent.replace('Option', 'Config')
    for item in tags:
        if parent == item.parent and ((tag and tag == item.name) or (var and var == item.var)):
            return item
    item = Item(tag, var, parent)
    tags.append(item)
    return item

def findTag(l):
    if 'debug' not in l and '*' not in l:
        exclude = ['true', 'false']
        for tag in l.split('"'):
            if tag.upper() != tag and '.' not in tag and ' ' not in tag and '(' not in tag and tag not in exclude and '[' not in tag:
                return tag

def scan(afilter):
    for root, _, files in os.walk(args.fop):
        for name in files:
            if name.endswith('.java') and afilter in name:
                fn = os.path.join(root, name)
                f = open(fn)
                parser = name in ['FopConfParser.java', 'DefaultFontConfig.java']
                rendererConfigOption = False
                for l in f:
                    l = l.strip()
                    if 'implements RendererConfigOption' in l:
                        rendererConfigOption = True
                    if rendererConfigOption or parser:
                        item = getItem(name, l)
                        if item:
                            if 'getChild' in l:
                                item.element = True
                            if 'Boolean' in l:
                                item.attrtype = 'true/false'
                            if 'Integer' in l:
                                item.attrtype = 'integer'
                            if 'Float' in l:
                                item.attrtype = 'float'
                            if 'Option' in name:
                                if 'true' in l:
                                    item.attrtype = 'default: true'
                                if 'false' in l:
                                    item.attrtype = 'default: false'       
                f.close()

#scan('RendererOption')
scan('')

"""
def check(fn):
    f = open(fn)
    for l in f:
        for tag in list(tags):
            if ('<' + tag + ' ') in l or ('"' + tag + '"') in l or (' ' + tag + ' ') in l or ('<' + tag + '>') in l or (' ' + tag + '=') in l or ('<' + tag + '/') in l :
                tags.remove(tag)
    f.close()
            
for root, _, files in os.walk(args.website + '/content/fop/trunk'):
    for name in files:
        if name.endswith('.mdtext'):
            fn = os.path.join(root, name)
            #check(fn)
#check(home + '/xmlgraphics-website/content/fop/fop-pdf-images.mdtext')
"""

f = open(args.website + '/content/fop/trunk/fopxconf.mdtext', 'w')

f.write('Title: Apache(tm) FOP: Config Options\n\n')
f.write('#Apache&trade; FOP: Config Options\n\n')

links = {
'FopConfParser':'configuration.html',
'DefaultFontConfig': 'fonts.html#bulk',
'PDFEncryptionConfig': 'pdfencryption.html#embedded',
'PDFRendererConfig': 'pdfa.html#fop-xconf',
'AFPRendererConfig': 'output.html#afp-configuration',
'PSRendererConfig': 'output.html#ps-configuration',
'TxtRendererConfig': 'output.html#txt',
'PCLRendererConfig': 'output.html#pcl-configuration',
'BitmapRendererConfig': 'output.html#bitmap-configuration',
'TIFFRendererConfig': 'output.html#bitmap-configuration',
'IFRendererConfig': ''
}

def printtags(tag, hasParent):
    if tag.name:
        if tag.element:
            if tag.attrtype != 'string':
                f.write('- &lt;' + tag.name + '&gt;' + tag.attrtype + '&lt;/' + tag.name + '&gt;\n')
            else:
                f.write('- &lt;' + tag.name + '/&gt;\n')
        else:
            if hasParent:
                f.write('    ')
            f.write('- ' + tag.name + '=' + tag.attrtype + '\n')
    
seen = []
    
def printGroup(parent, hasParent):
    if parent not in seen:
        f.write('### [' + parent + '](' + links[parent] + ')\n\n')
        for tag in tags:
            if tag.parent == parent:
                printtags(tag, hasParent)
        f.write('\n')
        seen.append(parent)

printGroup('FopConfParser', True)
printGroup('DefaultFontConfig', True)
for tag in tags:
    printGroup(tag.parent, False)
    
f.close()    
    