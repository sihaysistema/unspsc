# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "unspsc"
app_title = "UNSPSC"
app_publisher = "Si Hay Sistema"
app_description = "UNSPSC son las iniciales de United Nations Standard Products and Services Code. Es un sistema de cifrado que clasifica productos y servicios para fines comerciales a escala mundial."
app_icon = "octicon octicon-git-branch"
app_color = "#0e63aa"
app_email = "m.monroyc22@gmail.com"
app_license = "MIT"

# fixtures = ["Item Group"]
fixtures = [
     {
         "doctype": "Item Group",
         "filters": [
             ["item_group_name", "not in", ("All Item Groups")]
             ]
     }]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/unspsc/css/unspsc.css"
# app_include_js = "/assets/unspsc/js/unspsc.js"

# include js, css files in header of web template
# web_include_css = "/assets/unspsc/css/unspsc.css"
# web_include_js = "/assets/unspsc/js/unspsc.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "unspsc.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "unspsc.install.before_install"
# after_install = "unspsc.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "unspsc.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"unspsc.tasks.all"
# 	],
# 	"daily": [
# 		"unspsc.tasks.daily"
# 	],
# 	"hourly": [
# 		"unspsc.tasks.hourly"
# 	],
# 	"weekly": [
# 		"unspsc.tasks.weekly"
# 	]
# 	"monthly": [
# 		"unspsc.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "unspsc.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "unspsc.event.get_events"
# }

