from odoo import models, fields

class BlogPost(models.Model):
    _inherit = 'blog.post'

    content_type = fields.Selection([
        ('article', 'Article'),
        ('music', 'Music'),
        ('video', 'Video'),
        ('magazine', 'Magazine'),
        ('collection', 'Collection')
    ], string='Content Type', default='article', required=True)

    music_url = fields.Char('Music URL(Embed)')
    music_artist = fields.Char('Artist Name')
    video_url = fields.Char('Video URL(Embed)')
    magazine_url = fields.Char('Magazine Link')
    collection_ids = fields.Many2many(
        'blog.post',
        'blog_post_collection_rel',
        'parent_id', 'child_id',
        string='Related Posts'
    )