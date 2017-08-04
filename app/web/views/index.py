# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from flask import Blueprint, render_template


bp = Blueprint('home', __name__)


@bp.route('/')
def index():
    return render_template('index.html')
