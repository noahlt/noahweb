#!/usr/bin/env python

from markdown.preprocessors import Preprocessor
import markdown
import os
import os.path as path
import markdown
import shutil
import re
from wand.image import Image
from jinja2 import FileSystemLoader, Environment, select_autoescape

PROJECT_DIR = path.normpath(
    path.join(path.dirname(path.realpath(__file__)), '..'))
CONTENT_DIR = path.join(PROJECT_DIR, 'content')
TEMPLATE_DIR = path.join(PROJECT_DIR, 'templates')
OUTPUT_DIR = path.join(PROJECT_DIR, 'output')
ASSETS_REL = 'assets'

print(f'reading content from {CONTENT_DIR}')

# Delete old stuff

for filename in os.listdir(OUTPUT_DIR):
    filepath = path.join(OUTPUT_DIR, filename)
    if path.isdir(filepath) and not path.islink(filepath):
        shutil.rmtree(filepath)
    elif path.exists(filepath):
        os.remove(filepath)

#
# Set up Markdown
#

# unfortunately, this global is how we tell the ImagePreprocessor what the
# current working directory is.
CWD_HACK = ''


class ImagePreprocessor(Preprocessor):
    '''Transform custom image tags into images of the cropped versions,
    linking to full-size images.'''

    regex = re.compile(r'^IMG:\s?([^\s]*)(.*)$')

    def run(self, lines):
        new_lines = []
        for line in lines:
            m = ImagePreprocessor.regex.match(line)
            if m:
                imgpath = m[1]
                rest_of_line = m[2]
                with Image(filename=path.join(CWD_HACK, imgpath)) as img:
                    base, ext = path.splitext(imgpath)
                    if img.width > 1200:  # 2x 600px wide
                        new_lines.append(
                            f'[<img src="{base}.600{ext}" srcset="{base}.1200{ext} 2x">]({imgpath}){rest_of_line}')
                    else:
                        new_lines.append(
                            f'[<img src="{base}.600{ext}" srcset="{imgpath} 2x">]({imgpath}){rest_of_line}')
                    # todo: theoretical case for img.width < 600
            else:
                new_lines.append(line)
        return new_lines


class ImagePreprocessorExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        md.preprocessors.add('cropped_images', ImagePreprocessor(md), '_begin')


md = markdown.Markdown(extensions=['meta', ImagePreprocessorExtension()])

#
# Set up Jinja2
#

templates = Environment(loader=FileSystemLoader([TEMPLATE_DIR]))

#
# Main code begins
#

blog_posts = []

for dirname, subdirnames, filenames in os.walk(CONTENT_DIR):
    for filename in filenames:
        relpath = path.relpath(dirname, start=CONTENT_DIR)
        infilepath = path.join(dirname, filename)
        base, ext = path.splitext(filename)
        if filename == '.DS_Store':  # ideally, skip all files in .gitignore
            pass
        elif ext == '.html':
            print(f'🌎 {path.join(relpath, filename)} (raw html)')
            copyfilepath = path.join(OUTPUT_DIR, relpath, filename)
            htmldir = path.join(OUTPUT_DIR, relpath)
            if not os.path.exists(htmldir):
                os.makedirs(htmldir)
            print(f' - copying {copyfilepath}')
            shutil.copyfile(infilepath, copyfilepath)
        elif ext == '.md':
            print(f'📃 {path.join(relpath, filename)} (markdown)')
            md.reset()
            template_context = {}
            with open(infilepath, 'r') as mdfile:
                print(f' - converting markdown')
                CWD_HACK = path.relpath(dirname)
                template_context['body'] = md.convert(mdfile.read())
            # The following line tells pylint to disregard the fact that the
            # Markdown class doesn't have a .Meta attribute defined.
            # (It's added by the 'meta' extension.)
            # pylint: disable=no-member
            if md.Meta:
                # This is silly, but we go through each metadata item and
                # if it's a single-element list we flatten it.
                for key, val in md.Meta.items():
                    if not hasattr(val, 'strip') and len(val) == 1:
                        md.Meta[key] = val[0]
                if 'date' in md.Meta:
                    blog_data = md.Meta.copy()
                    blog_data['url'] = path.join('/', relpath, base+'.html')
                    blog_posts.append(blog_data)
                template_context.update(md.Meta)
            blog_template = templates.get_template('blogpost.html')
            html = blog_template.render(template_context)
            htmldir = path.join(OUTPUT_DIR, relpath)
            if not os.path.exists(htmldir):
                os.makedirs(htmldir)
            htmlpath = path.join(htmldir, base+'.html')
            with open(htmlpath, 'w') as htmlfile:
                print(f' - writing {htmlpath}')
                htmlfile.write(html)
        elif ext in ['.png', '.jpg', '.jpeg']:
            print(f'🖼  {path.join(relpath, filename)} (image)')
            copyfilepath = path.join(OUTPUT_DIR, relpath, filename)
            print(f' - copying original image to {copyfilepath}')
            shutil.copyfile(infilepath, copyfilepath)

            # We must recreate both imgfile and img because reading and
            # resizing mutate the file/img object state. Lame.
            for cropwidth in [600, 1200]:  # 1200 is for 2x retina
                with Image(filename=infilepath) as img:
                    if img.width <= cropwidth:
                        print(
                            f' ~ {filename} is {img.width}px wide and need not be cropped to {cropwidth}px')
                        continue
                    img.transform(resize=str(cropwidth))
                    cropped_img_path = path.join(
                        OUTPUT_DIR, relpath, f'{base}.{cropwidth}{ext}')
                    print(f' - saving cropped version {cropped_img_path}')
                    img.save(filename=cropped_img_path)
        else:
            print(
                f'❌ unknown extension for {path.join(relpath, filename)}: "{ext}"')

print('🏠 generating home page')
index_html = templates.get_template('index.html').render(blog_posts=blog_posts)
with open(path.join(OUTPUT_DIR, 'index.html'), 'w') as index_file:
    index_file.write(index_html)

print('🛢  copying assets')
assets_out = path.join(OUTPUT_DIR, ASSETS_REL)
shutil.copytree(path.join(PROJECT_DIR, ASSETS_REL), assets_out)
