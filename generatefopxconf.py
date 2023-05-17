import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('fop', help='fop dir')
parser.add_argument('website', help='website dir')
args = parser.parse_args()

class Item:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent.replace('.java', '')
        self.element = False
        self.attrtype = 'string'

tags = []

def getItem(parent, l):
    tag = None
    if '"' in l:
        tag = l.split('"')[1]
        if ' ' in tag or len(tag) < 2 or tag.lower() != tag or tag == 'true':
            return None
    elif '(' in l:
        tag = l.split('(')[1].split(')')[0]
        if '_' not in tag or ' ' in tag or '.' in tag:
            return None
        tag = tag.lower().replace('_', '-')
    else:
        return None
    for item in tags:
        if tag == item.name:
            return item
    item = Item(tag, parent)
    tags.append(item)
    return item

for root, _, files in os.walk(args.fop):
    for name in files:
        if name.endswith('.java'):
            fn = os.path.join(root, name)
            f = open(fn)
            if name == 'Java2DRendererOption.java':
                name = 'PCLRendererOption.java'
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

f = open(args.website + '/content/fop/trunk/fopxconf.mdtext', 'w')

f.write('Title: Apache(tm) FOP: Config Options\n\n')
f.write('#Apache&trade; FOP: Config Options\n\n')

links = {
'FopConfParser':'configuration.html',
'DefaultFontConfig': 'fonts.html#bulk',
'PDFEncryptionOption': 'pdfencryption.html#embedded',
'PDFRendererOption': 'pdfa.html#fop-xconf',
'AFPRendererOption': 'output.html#afp-configuration',
'PSRendererOption': 'output.html#ps-configuration',
'TxtRendererConfig': 'output.html#txt',
'PCLRendererOption': 'output.html#pcl-configuration',
'BitmapRendererOption': 'output.html#bitmap-configuration',
'TIFFRendererConfig': 'output.html#bitmap-configuration',
}

def printtags(tag, hasParent):
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
    