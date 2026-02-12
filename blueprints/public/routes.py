from flask import render_template
from . import public_bp
import sqlite3
from flask import (
    render_template, request, redirect, url_for, session,
    flash, current_app, Response, jsonify, abort
)


@public_bp.route('/')
def index():
    """Landing page"""
    return render_template('public/index.html')

@public_bp.route('/about')
def about():
    """About Us page"""
    return render_template('public/about.html')

@public_bp.route('/terms-of-service')
def terms():
    """Legal: TOS"""
    return render_template('public/terms.html')

@public_bp.route('/privacy-policy')
def privacy():
    """Legal: Privacy"""
    return render_template('public/privacy.html')