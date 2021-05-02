from jinja2 import Template

class TemplateLetterNotRenderedException(Exception): pass

class TemplateLetter():
    
    def __init__(self, template):
        self.template = Template(template)
        self.rendered_template = str()
        
    def render(self, **kwargs):
        self.rendered_template = self.template.render(**kwargs)

    def __str__(self):
        if not self.rendered_template:
            raise TemplateLetterNotRenderedException
        return self.rendered_template

