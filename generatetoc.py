import os

for root, _, files in os.walk('content/fop/dev'):
    for name in files:
        if name.endswith('.mdtext'):
            path = os.path.join(root, name)
            f = open(path)
            title = None
            for l in f:
                title = l.split(': ')[-1].strip()
                break
            f.close()
          
            name = name.replace('.mdtext', '')
            url = root.replace('content/', '/') + '/' + name
            print '<li><a href="%s.html">%s</a></li>' % (url, title)