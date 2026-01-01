from odoo import http
from odoo.http import request
from odoo.addons.website_blog.controllers.main import WebsiteBlog
from odoo.addons.website.controllers.main import QueryURL


class MultimediaBlogController(WebsiteBlog):

    @http.route([
        '/blog/type/<string:content_type>',
    ], type='http', auth="public", website=True)
    def blog_multimedia_filter(self, content_type, page=1, **opt):
        valid_types = ['article', 'music', 'video', 'magazine', 'collection']
        if content_type not in valid_types:
            return request.redirect('/blog')

        Blog = request.env['blog.blog']
        blogs = Blog.search(request.website.website_domain(), order="create_date asc, id asc")

        values = self._prepare_blog_values(blogs=blogs, page=page, **opt)

        values['blog_url'] = QueryURL('/blog', ['blog', 'tag'],
                                      date_begin=opt.get('date_begin'),
                                      date_end=opt.get('date_end'),
                                      search=values.get('search'))

        domain = [('content_type', '=', content_type)]
        posts = request.env['blog.post'].search(domain, order="post_date desc")

        values['posts'] = posts

        return request.render("website_blog.blog_post_short", values)