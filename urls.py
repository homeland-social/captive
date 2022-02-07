from api.views.wifi import NetworkResource, scan  # noqa: E402
app.add_url_rule('/api/wifi/scan/', view_func=scan, methods=['POST'])
NetworkResource.add_url_rules(app, rule_prefix='/api/wifi/networks/')

