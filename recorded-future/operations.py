"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

import xmltodict
from requests import request, exceptions as req_exceptions
from urllib.parse import quote, urlencode
from .constants import *
from connectors.core.connector import ConnectorError, get_logger

logger = get_logger('recorded-future')


def _get_config_params(config):
    base_url = config.get('base_url')
    if not base_url.startswith('https://') and not base_url.startswith('http://'):
        base_url = 'https://' + base_url
    base_url.strip('/')
    api_key = config.get('api_key')
    headers = {
        'X-RFToken': api_key,
        'X-RF-User-Agent': 'cybersponse-1.0.1'
    }
    verify_ssl = config.get('verify_ssl') if config.get('verify_ssl') else False
    return base_url, headers, verify_ssl


def make_rest_call(endpoint, config, method='GET', params=None, data=None):
    try:
        url, headers, verify_ssl = _get_config_params(config)
        response = request(method, url=url + endpoint, headers=headers, params=params, data=data,
                           verify=verify_ssl)
        if response.ok:
            logger.info('Successfully got response for url {}'.format(url))
            if 'json' in str(response.headers):
                return response.json()
            else:
                return response.text
        else:
            logger.error(response.text)
            raise ConnectorError(
                {'status_code': response.status_code, 'message': response.json()['error']['message']})
    except req_exceptions.SSLError:
        logger.error('An SSL error occurred')
        raise ConnectorError('An SSL error occurred')
    except req_exceptions.ConnectionError:
        logger.error('A connection error occurred')
        raise ConnectorError('A connection error occurred')
    except req_exceptions.Timeout:
        logger.error('The request timed out')
        raise ConnectorError('The request timed out')
    except req_exceptions.RequestException:
        logger.error('There was an error while handling the request')
        raise ConnectorError('There was an error while handling the request')
    except Exception as err:
        raise ConnectorError(str(err))


def _get_response(input_text, config, params):
    try:
        fields = params.get('fields') if params.get('fields') else []
        for item in range(len(fields)):
            fields[item] = fields_options.get(fields[item])
        temp_str = ','.join(map(str.strip, fields))
        if temp_str:
            temp_str = 'fields={}'.format(quote(temp_str))
        metadata = params.get('metadata')
        endpoint = '/v2/{0}?{1}&metadata={2}'.format(input_text, temp_str, metadata)
        return make_rest_call(endpoint, config)
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def domain_reputation(config, params):
    domain = params.get('domain')
    return _get_response('domain/{}'.format(domain), config, params)


def ip_reputation(config, params):
    ip = params.get('ip')
    return _get_response('ip/{}'.format(ip), config, params)


def file_reputation(config, params):
    file_hash = params.get('hash')
    return _get_response('hash/{}'.format(file_hash), config, params)


def lookup_vulnerability(config, params):
    cve_id = params.get('cve_id')
    return _get_response('vulnerability/{}'.format(cve_id), config, params)


def lookup_malware(config, params):
    malware_id = params.get('malware_id')
    return _get_response('malware/{}'.format(malware_id), config, params)


def lookup_url(config, params):
    url = params.get('url')
    return _get_response('url/{}'.format(quote(url, safe='')), config, params)


def get_riskrules(config, params):
    try:
        type = type_list.get(params.get('type'), 'ip')
        endpoint = '/v2/{}/riskrules'.format(type)
        return make_rest_call(endpoint, config)
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def _find_risk_list(config, params, input_type):
    try:
        temp = ''
        risk_rule_list = risk_list.get(params.get('risk_rule_list'))
        if risk_rule_list:
            temp = '&list={}'.format(risk_rule_list)
        endpoint = '/v2/{}/risklist?format={}{}'.format(input_type, quote('xml/stix/1.1.1', safe=''), temp)
        res = make_rest_call(endpoint, config)
        return xmltodict.parse(res)
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def ip_risklist(config, params):
    return _find_risk_list(config, params, 'ip')


def file_risklist(config, params):
    return _find_risk_list(config, params, 'hash')


def vulnerability_risklist(config, params):
    return _find_risk_list(config, params, 'vulnerability')


def domain_risklist(config, params):
    return _find_risk_list(config, params, 'domain')


def url_risklist(config, params):
    return _find_risk_list(config, params, 'url')


def _search_request(config, params, url_text, params_dict):
    try:
        for item in params_dict:
            params_dict[item] = params.get(item)
        if url_text == 'alert':
            params_dict['status'] = status_dict.get(params_dict['status'])
        else:
            temp_list = []
            for item in params_dict['fields']:
                temp_list.append(fields_options.get(item))
            params_dict['fields'] = ','.join(map(str.strip, temp_list))
            params_dict['riskRule'] = risk_list.get(params_dict['riskRule'])
        params_dict['orderby'] = order_by_dict.get(params_dict['orderby'])
        params_dict['direction'] = direction_list.get(params_dict['direction'])
        params_dict = {k: v for k, v in params_dict.items() if v is not None and v != ''}
        endpoint = '/v2/{}/search?{}'.format(url_text, urlencode(params_dict))
        return make_rest_call(endpoint, config)
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def search_file(config, params):
    try:
        params_dict = {'fields': [], 'metadata': False, 'limit': 0, 'from': 0, 'riskScore': '',
                       'algorithm': '', 'firstSeen': '', 'lastSeen': '', 'list': '', 'riskRule': '',
                       'orderby': '', 'direction': ''}
        return _search_request(config, params, 'hash', params_dict)
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def search_vulnerability(config, params):
    try:
        params_dict = {'freetext': '', 'fields': [], 'metadata': False, 'limit': 0, 'from': 0,
                       'riskScore': '', 'cvssScore': '', 'firstSeen': '', 'lastSeen': '', 'list': '',
                       'riskRule': '', 'orderby': '', 'direction': ''}
        return _search_request(config, params, 'vulnerability', params_dict)
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def search_url(config, params):
    try:
        params_dict = {'fields': [], 'metadata': False, 'limit': 0, 'from': 0, 'riskScore': '',
                       'firstSeen': '', 'lastSeen': '', 'list': '', 'riskRule': '', 'orderby': '',
                       'direction': ''}
        return _search_request(config, params, 'url', params_dict)
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def search_domain(config, params):
    try:
        params_dict = {'fields': [], 'metadata': False, 'limit': 0, 'from': 0, 'riskScore': '',
                       'firstSeen': '', 'lastSeen': '', 'list': '', 'riskRule': '', 'parent': '',
                       'orderby': '', 'direction': ''}
        return _search_request(config, params, 'domain', params_dict)
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def search_ip(config, params):
    try:
        params_dict = {'fields': [], 'metadata': False, 'limit': 0, 'from': 0, 'range': '',
                       'riskScore': '', 'firstSeen': '', 'lastSeen': '', 'list': '',
                       'riskRule': '', 'orderby': '', 'direction': ''}
        return _search_request(config, params, 'ip', params_dict)
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def search_malware(config, params):
    try:
        params_dict = {'freetext': '', 'fields': [], 'metadata': False, 'limit': 0, 'from': 0,
                       'firstSeen': '', 'lastSeen': '', 'list': '', 'orderby': '', 'direction': '',
                       'riskRule': ''}
        return _search_request(config, params, 'malware', params_dict)
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def search_alerts(config, params):
    try:
        params_dict = {'triggered': '', 'assignee': '', 'status': '', 'alertRule': '',
                       'freetext': '', 'limit': 0, 'from': 0, 'orderby': '', 'direction': ''}
        return _search_request(config, params, 'alert', params_dict)
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def search_alert_rules(config, params):
    try:
        params = {k: v for k, v in params.items() if v is not None and v != ''}
        endpoint = '/v2/alert/rule?{}'.format(params)
        return make_rest_call(endpoint, config)
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def build_payload(params):
    data = {}
    for k, v in params.items():
        if v:
            if isinstance(v, list):
                data[k] = [str(x) for x in v]
            elif k in PARA_LIST:
                data[k] = [x.strip() for x in str(v).split(",")]
            else:
                data[k] = v
    logger.debug('data ------->{}'.format(data))
    return data


def get_alert(config, params):
    try:
        alert_id = params.get('alert_ID')
        endpoint = '/v2/alert/{}'.format(alert_id)
        return make_rest_call(endpoint, config)
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError(str(err))


def get_maps_list(config, params):
    endpoint = '/threat/maps'
    return make_rest_call(endpoint, config)


def get_threat_map(config, params):
    endpoint = '/threat/map/actors'
    params = build_payload(params)
    return make_rest_call(endpoint, config, data=params, method='POST')


def get_threat_map_by_org_id(config, params):
    endpoint = f'/threat/map/{params.pop("orgId")}/actors'
    params = build_payload(params)
    return make_rest_call(endpoint, config, data=params, method='POST')


def get_malware_threat_map(config, params):
    endpoint = '/threat/map/malware'
    params = build_payload(params)
    return make_rest_call(endpoint, config, data=params, method='POST')


def get_malware_threat_map_by_org_id(config, params):
    endpoint = f'/threat/map/{params.pop("orgId")}/malware'
    params = build_payload(params)
    return make_rest_call(endpoint, config, data=params, method='POST')


def get_threat_actors_list(config, params):
    endpoint = '/threat/actor/search'
    params = build_payload(params)
    return make_rest_call(endpoint, config, data=params, method='POST')


def get_threat_actors_categories(config, params):
    endpoint = '/threat/actor/categories'
    return make_rest_call(endpoint, config)


def get_malware_categories(config, params):
    endpoint = '/threat/malware/categories'
    return make_rest_call(endpoint, config)


def get_third_party_risk_alert_by_alert_id(config, params):
    endpoint = f'/playbook-alert/third_party_risk/{params.pop("playbook_alert_id")}'
    params = build_payload(params)
    return make_rest_call(endpoint, config, data=params, method='POST')


def get_bulk_third_party_risk_alerts(config, params):
    endpoint = f'/playbook-alert/third_party_risk'
    params = build_payload(params)
    return make_rest_call(endpoint, config, data=params, method='POST')


def get_identity_novel_exposures_alert_by_alert_id(config, params):
    endpoint = f'/playbook-alert/identity_novel_exposures/{params.pop("playbook_alert_id")}'
    params = build_payload(params)
    return make_rest_call(endpoint, config, data=params, method='POST')


def get_bulk_identity_novel_exposures_alerts(config, params):
    endpoint = f'/playbook-alert/identity_novel_exposures'
    params = build_payload(params)
    return make_rest_call(endpoint, config, data=params, method='POST')


def create_user_list(config, params):
    endpoint = f'/list/create'
    params = build_payload(params)
    return make_rest_call(endpoint, config, data=params, method='POST')


def get_user_lists(config, params):
    endpoint = f'/list/search'
    params = build_payload(params)
    return make_rest_call(endpoint, config, data=params, method='POST')


def get_user_list_by_list_id(config, params):
    endpoint = f'/list/{params.pop("listId")}/info'
    return make_rest_call(endpoint, config)


def get_user_list_status_by_list_id(config, params):
    endpoint = f'/list/{params.pop("listId")}/status'
    return make_rest_call(endpoint, config)


def get_entities_by_list_id(config, params):
    endpoint = f'/list/{params.pop("listId")}/entities'
    return make_rest_call(endpoint, config)


def add_entity_to_user_list(config, params):
    endpoint = f'/list/{params.pop("listId")}/entity/add'
    data = {
        "entity": {
            "id": params.get('id')
        }
    }
    if params.get('context'):
        data['context'] = params.get('context')
    return make_rest_call(endpoint, config, data=data, method='POST')


def remove_entity_from_user_list(config, params):
    endpoint = f'/list/{params.pop("listId")}/entity/remove'
    data = {
        "entity": {
            "id": params.get('id')
        }
    }
    return make_rest_call(endpoint, config, data=data, method='POST')


def add_ioc_to_recorded_future_intelligence_cloud(config, params):
    endpoint = '/collective-insights/detections'
    data = {}
    if params.get('options'):
        data['options'] = params.pop('options')
    if params.get('organization_ids'):
        data['organization_ids'] = [x.strip() for x in str(params.pop('organization_ids')).split(",")]
    data['data'] = build_payload(params)
    return make_rest_call(endpoint, config, data=data, method='POST')


def test_connection(config):
    try:
        url, headers, verify_ssl = _get_config_params(config)
        endpoint = '{}/v2/soar/triage/contexts'.format(url)
        response = request(method='GET', url=endpoint, headers=headers, verify=verify_ssl)
        if response.ok:
            logger.info('check health executed successfully')
            return True
        elif response.status_code == 401:
            raise ConnectorError('Invalid endpoint or credentials')
        elif response.status_code == 403:
            raise ConnectorError('Unauthorized')
        else:
            logger.error(response.json())
    except req_exceptions.SSLError:
        logger.error('An SSL error occurred')
        raise ConnectorError('An SSL error occurred')
    except req_exceptions.ConnectionError:
        logger.error('A connection error occurred')
        raise ConnectorError('A connection error occurred')
    except req_exceptions.Timeout:
        logger.error('The request timed out')
        raise ConnectorError('The request timed out')
    except req_exceptions.RequestException:
        logger.error('There was an error while handling the request')
        raise ConnectorError('There was an error while handling the request')
    except Exception as e:
        raise ConnectorError(str(e))
    raise ConnectorError(response.json()['error']['message'])


operations = {
    'domain_reputation': domain_reputation,
    'domain_risklist': domain_risklist,
    'search_domain': search_domain,
    'ip_reputation': ip_reputation,
    'search_ip': search_ip,
    'ip_risklist': ip_risklist,
    'file_reputation': file_reputation,
    'file_risklist': file_risklist,
    'search_file': search_file,
    'lookup_vulnerability': lookup_vulnerability,
    'search_vulnerability': search_vulnerability,
    'vulnerability_risklist': vulnerability_risklist,
    'lookup_url': lookup_url,
    'search_url': search_url,
    'url_risklist': url_risklist,
    'lookup_malware': lookup_malware,
    'search_malware': search_malware,
    'search_alert_rule': search_alert_rules,
    'get_alert': get_alert,
    'search_alerts': search_alerts,
    'get_riskrules': get_riskrules,
    'get_maps_list': get_maps_list,
    'get_threat_map': get_threat_map,
    'get_threat_map_by_org_id': get_threat_map_by_org_id,
    'get_malware_threat_map': get_malware_threat_map,
    'get_malware_threat_map_by_org_id': get_malware_threat_map_by_org_id,
    'get_threat_actors_list': get_threat_actors_list,
    'get_threat_actors_categories': get_threat_actors_categories,
    'get_malware_categories': get_malware_categories,
    'get_third_party_risk_alert_by_alert_id': get_third_party_risk_alert_by_alert_id,
    'get_bulk_third_party_risk_alerts': get_bulk_third_party_risk_alerts,
    'get_identity_novel_exposures_alert_by_alert_id': get_identity_novel_exposures_alert_by_alert_id,
    'get_bulk_identity_novel_exposures_alerts': get_bulk_identity_novel_exposures_alerts,
    'create_user_list': create_user_list,
    'get_user_lists': get_user_lists,
    'get_user_list_by_list_id': get_user_list_by_list_id,
    'get_user_list_status_by_list_id': get_user_list_status_by_list_id,
    'get_entities_by_list_id': get_entities_by_list_id,
    'add_entity_to_user_list': add_entity_to_user_list,
    'remove_entity_from_user_list': remove_entity_from_user_list,
    'add_ioc_to_recorded_future_intelligence_cloud': add_ioc_to_recorded_future_intelligence_cloud
}
