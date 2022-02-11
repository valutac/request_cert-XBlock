""" RequestCertXBlock main Python class"""
import logging

from xblock.core import XBlock
from xblock.fields import Boolean, DateTime, Float, Integer, List, Scope, String, Dict
from xblock.fragment import Fragment
from xblockutils.resources import ResourceLoader
from xblockutils.studio_editable import StudioEditableXBlockMixin

from .utils import resource_string

_ = lambda text: text
logger = logging.getLogger(__name__)


class RequestCertXBlock(StudioEditableXBlockMixin, XBlock):
    """
    Fields RequestCertXBlock
    """

    display_name = String(
        display_name="Display Name",
        default="Request Certificate",
        scope=Scope.settings,
    )

    header_content = String(
        display_name=_("Header"),
        scope=Scope.settings,
        default="Selamat! Kamu telah menyelesaikan kursus",
    )

    images = String(
        display_name=_("Images"),
        scope=Scope.settings,
        default="https://developmentx.s3.amazonaws.com/files/complete.gif",
    )

    button_desc = String(
        display_name=_("Button Description"),
        scope=Scope.settings,
        default="Klik tombol di bawah ini untuk melakukan permohonan sertifikat!",
    )

    button_text = String(
        display_name=_("Button Text"),
        scope=Scope.settings,
        default="Permohonan Sertifikat",
    )

    editable_fields = ('display_name', 'header_content', 'images', 'button_desc', 'button_text',)


    """
    Main functions
    """
    def student_view(self, context=None):
        context.update({
            'display_name': self.display_name,
            'header_content': self.header_content,
            'images': self.images,
            'button_desc': self.button_desc,
            'button_text': self.button_text,
        })
        loader = ResourceLoader(__name__)
        fragment = Fragment()
        fragment.add_content(loader.render_mako_template('static/html/student_view.html', context))
        return fragment
