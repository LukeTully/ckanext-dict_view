import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class Dict_ViewPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IResourceView, inherit=True)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'dict_view')

    def info(self):
        return {
            'name': 'dictionary',
            'title': 'Dictionary Table',
            'iframed': False,
            'preview_enabled': True,
            'full_page_edit': True,
        }

    def can_view(self, data_dict):
        # TODO: Determine if the resource has the appropriate fields available
        return True

    def view_template(self, context, data_dict):
        return 'dictionary_view.html'

    # def form_template(self, context, data_dict):
    #     return 'dictionary_form.html'

    def setup_template_variables(self, context, data_dict):
        result = {}
        current_resource = data_dict['resource'].get('id', None)
        resource = toolkit.get_action('datastore_search')(
            context, {
                'resource_id': current_resource
            }
        )
        result['dictionary'] = resource.get('fields', None)
        return result