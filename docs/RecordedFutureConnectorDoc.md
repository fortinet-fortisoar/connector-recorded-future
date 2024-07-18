## About the connector
Recorded Future is a threat intelligence product that automatically collects and analyzes threat intelligence from technical, open, and dark web sources to provide invaluable context for faster human analysis and real-time integration with your existing security systems.
<p>This document provides information about the Recorded Future Connector, which facilitates automated interactions, with a Recorded Future server using FortiSOAR&trade; playbooks. Add the Recorded Future Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Recorded Future.</p>

### Version information

Connector Version: 2.0.0

Authored By: Fortinet

Certified: No
## Release Notes for version 2.0.0
Following enhancements have been made to the Recorded Future Connector in version 2.0.0:
<ul>
<li><p>Added following new actions and corresponding playbooks:</p>

<ul>
<li>Get Maps List</li>
<li>Get Threat Map</li>
<li>Get Threat Map By Org ID</li>
<li>Get Malware Threat Map</li>
<li>Get Malware Threat Map By Org ID</li>
<li>Get Threat Actors List</li>
<li>Get Threat Actors Categories</li>
<li>Get Malware Categories</li>
<li>Get Third Party Risk Alert By Alert ID</li>
<li>Get Bulk Third Party Risk Alerts</li>
<li>Get Identity Novel Exposures Alert By Alert ID</li>
<li>Get Bulk Identity Novel Exposures Alerts</li>
<li>Create User List</li>
<li>Get User Lists</li>
<li>Get User List By List ID</li>
<li>Get User List Status By List ID</li>
<li>Retrieves entities on the list by list ID</li>
<li>Add Entity To User List</li>
<li>Remove Entity From User List</li>
<li>Add IOC To Recorded Future Intelligence Cloud</li>
</ul></li>
</ul>

## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-recorded-future</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Recorded Future server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Recorded Future server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Recorded Future</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>URL of the Recorded Future server from where the connector gets notifications
</td>
</tr><tr><td>API Key</td><td>API Key that is configured for you to authenticate your Recorded Future account
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Domain Reputation</td><td>Looks up the intel threat context for a domain and retrieves its reputation from Recorded future, based on the domain name you have specified</td><td>get_domain_reputation <br/>Investigation</td></tr>
<tr><td>Get Domain Risk List</td><td>Retrieves the risk list information for the domain(s) from Recorded Future, based on the risk rule list you have specified</td><td>get_risk_list <br/>Investigation</td></tr>
<tr><td>Search Domain</td><td>Searches for and retrieves information about intel threat context for all domains or specific domain(s) (based on the filter criteria you have specified) from Recorded Future</td><td>search_domain <br/>Investigation</td></tr>
<tr><td>Get IP Reputation</td><td>Looks up the intel threat context for an IP address and retrieves its reputation from Recorded Future, based on the IP address you have specified</td><td>get_ip_reputation <br/>Investigation</td></tr>
<tr><td>Get IP Risk List</td><td>Retrieves the risk list information for the IP address(es) from Recorded Future, based on the risk rule list you have specified</td><td>get_risk_list <br/>Investigation</td></tr>
<tr><td>Search IP</td><td>Searches for and retrieves information about intel threat context for all IP addresses or specific IP address(es) (based on the filter criteria you have specified) from Recorded Future</td><td>search_ip <br/>Investigation</td></tr>
<tr><td>Get File Reputation</td><td>Looks up the intel threat context for a file identity hash (MD5, SHA-1 or SHA-256) and retrieves its reputation from Recorded future, based on the file hash you have specified</td><td>get_file_reputation <br/>Investigation</td></tr>
<tr><td>Get File Risk List</td><td>Retrieves the risk list information for the file(s) from Recorded Future, based on the risk rule list you have specified</td><td>get_risk_list <br/>Investigation</td></tr>
<tr><td>Search Filehash</td><td>Searches for and retrieves information about intel threat context for all filehashes or specific filehash(es) (based on the filter criteria you have specified) from Recorded Future</td><td>search_filehash <br/>Investigation</td></tr>
<tr><td>Lookup Vulnerability</td><td>Looks up the intel threat context for a vulnerability and retrieves its information from Recorded future, based on the CVE Identifier ID or Recorded Future ID you have specified</td><td>get_vulnerability <br/>Investigation</td></tr>
<tr><td>Get vulnerability Risk List</td><td>Retrieves the risk list information for the vulnerability(ies) from Recorded Future, based on the risk rule list you have specified</td><td>get_risk_list <br/>Investigation</td></tr>
<tr><td>Search Vulnerabilities</td><td>Searches for and retrieves information about intel threat context for all vulnerabilities or specific vulnerabilities(ies) (based on the filter criteria you have specified) from Recorded Futures</td><td>search_vulnerability <br/>Investigation</td></tr>
<tr><td>Lookup URL</td><td>Looks up the intel threat context for a URL and retrieves its information from Recorded future, based on the URL you have specified</td><td>get_url_reputation <br/>Investigation</td></tr>
<tr><td>Get URL Risk List</td><td>Retrieves the risk list information for the URL(s) from Recorded Future, based on the risk rule list you have specified</td><td>get_risk_list <br/>Investigation</td></tr>
<tr><td>Search URL</td><td>Searches for and retrieves information about intel threat context for all URLs or specific URL(s) (based on the filter criteria you have specified) from Recorded Future</td><td>search_url <br/>Investigation</td></tr>
<tr><td>Lookup Malware</td><td>Looks up the intel threat context for a Malware and retrieves its information from Recorded future, based on the Malware ID you have specified</td><td> <br/></td></tr>
<tr><td>Search Malware</td><td>Searches for and retrieves information about intel threat context for all Malwares or specific Malware(s) (based on the filter criteria you have specified) from Recorded Future</td><td> <br/></td></tr>
<tr><td>Get Alert</td><td>Retrieves details for an alert which is generated in Recorded Future, based on the alert ID you have specified</td><td>get_alert <br/>Investigation</td></tr>
<tr><td>Search Alerts</td><td>Searches for and retrieves notification information for all alerts or specific alert(s) (based on the filter criteria you have specified) generated on Recorded Future</td><td> <br/></td></tr>
<tr><td>Search Alert Rules</td><td>Searches for and retrieves information about all alert rules or specific alert rule(s) (based on the filter criteria you have specified) from Recorded Future</td><td> <br/></td></tr>
<tr><td>Get Risk Rules</td><td>Retrieves the risk rules for IP, Domain, URL, File or Vulnerability from Recorded Future, based on the filter criteria you have specified</td><td> <br/></td></tr>
<tr><td>Get Maps List</td><td>Retrieves information about the maps available for the user.</td><td>get_maps_list <br/>Investigation</td></tr>
<tr><td>Get Threat Map</td><td>Retrieves threat map data for the enterprise's primary organization with filters specified.</td><td>get_threat_map <br/>Investigation</td></tr>
<tr><td>Get Threat Map By Org ID</td><td>Retrieves threat map data for a specific organization with filters specified.</td><td>get_threat_map_by_org_id <br/>Investigation</td></tr>
<tr><td>Get Malware Threat Map</td><td>Retrieves malware threat map data for the enterprise's primary organization with filters specified.</td><td>get_malware_threat_map <br/>Investigation</td></tr>
<tr><td>Get Malware Threat Map By Org ID</td><td>Retrieves malware threat map data for a specific organization with filters specified.</td><td>get_malware_threat_map_by_org_id <br/>Investigation</td></tr>
<tr><td>Get Threat Actors List</td><td>Retrieve a list of threat actors.</td><td>get_threat_actors_list <br/>Investigation</td></tr>
<tr><td>Get Threat Actors Categories</td><td>Retrieve threat actors categories, which can be used to filter threat map data.</td><td>get_threat_actors_categories <br/>Investigation</td></tr>
<tr><td>Get Malware Categories</td><td>Retrieve malware categories, which can be used to filter malware threat map data.</td><td>get_malware_categories <br/>Investigation</td></tr>
<tr><td>Get Third Party Risk Alert By Alert ID</td><td>Retrieve detailed information about a Third Party Risk Playbook Alert with data grouped into UI-ready panels.</td><td>get_third_party_risk_alert_by_alert_id <br/>Investigation</td></tr>
<tr><td>Get Bulk Third Party Risk Alerts</td><td>Retrieves a detailed lookup of data panels for several alerts at once.</td><td>get_bulk_third_party_risk_alerts <br/>Investigation</td></tr>
<tr><td>Get Identity Novel Exposures Alert By Alert ID</td><td>Retrieve detailed information about a Identity Novel Exposures Playbook Alert with data grouped into UI-ready panels.</td><td>get_identity_novel_exposures_alert_by_alert_id <br/>Investigation</td></tr>
<tr><td>Get Bulk Identity Novel Exposures Alerts</td><td>Perform a detailed lookup of data panels for several Identity Novel Exposures alerts at once.</td><td>get_bulk_identity_novel_exposures_alerts <br/>Investigation</td></tr>
<tr><td>Create User List</td><td>Creates a user list based on the parameters specified.</td><td>create_user_list <br/>Investigation</td></tr>
<tr><td>Get User Lists</td><td>Retrieves lists based on a query specified.</td><td>get_user_lists <br/>Investigation</td></tr>
<tr><td>Get User List By List ID</td><td>Retrieves basic information about a specified list ID</td><td>get_user_list_by_list_id <br/>Investigation</td></tr>
<tr><td>Get User List Status By List ID</td><td>Retrieves status information about a specified list ID</td><td>get_user_list_status_by_list_id <br/>Investigation</td></tr>
<tr><td>Get Entities By List ID</td><td>Retrieves entities on the list by list ID</td><td>get_entities_by_list_id <br/>Investigation</td></tr>
<tr><td>Add Entity To User List</td><td>Add an entity to the user list.</td><td>add_entity_to_user_list <br/>Investigation</td></tr>
<tr><td>Remove Entity From User List</td><td>Remove an entity from the user list.</td><td>remove_entity_from_user_list <br/>Investigation</td></tr>
<tr><td>Add IOC To Recorded Future Intelligence Cloud</td><td>Add detected IOCs to the Recorded Future Intelligence Cloud.</td><td>add_ioc_to_recorded_future_intelligence_cloud <br/>Investigation</td></tr>
</tbody></table>

### operation: Get Domain Reputation
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Domain</td><td>Name of the domain for which you want to retrieve reputation from Recorded Future.
</td></tr><tr><td>Fields</td><td>(Optional) Fields that you want to include in the output. You can choose from the following options: Analysis Notes, Entity, Counts, Intel Card URL, Metrics, Related Entities, Risk, Sightings, Threat Lists, and Event Timestamps. By default, this option is set as Entity. you can choose one or more from Analyst Notes, Entity, Counts, Intel Card URL, Metrics, Related Entities, Risk, Sightings, Threat Lists and Event Timestamps
</td></tr><tr><td>Metadata</td><td>(Optional) Select this option to annotate the response with additional metadata explaining the response data elements. By default, this option is set as True.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "intelCard": "",
        "metrics": [
            {
                "type": "",
                "value": ""
            }
        ],
        "analystNotes": [],
        "timestamps": {
            "lastSeen": "",
            "firstSeen": ""
        },
        "sightings": [
            {
                "published": "",
                "fragment": "",
                "title": "",
                "type": "",
                "url": "",
                "source": ""
            }
        ],
        "entity": {
            "type": "",
            "id": "",
            "name": ""
        },
        "risk": {
            "score": "",
            "riskSummary": "",
            "criticality": "",
            "riskString": "",
            "evidenceDetails": [
                {
                    "criticality": "",
                    "rule": "",
                    "mitigationString": "",
                    "criticalityLabel": "",
                    "timestamp": "",
                    "evidenceString": ""
                }
            ],
            "criticalityLabel": "",
            "rules": ""
        },
        "relatedEntities": [
            {
                "type": "",
                "entities": [
                    {
                        "entity": {
                            "type": "",
                            "id": "",
                            "name": ""
                        },
                        "count": ""
                    }
                ]
            }
        ],
        "counts": [
            {
                "count": "",
                "date": ""
            }
        ],
        "threatLists": []
    },
    "metadata": {
        "entries": []
    }
}</pre>
### operation: Get Domain Risk List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Risk Rule List</td><td>(Optional) Risk Rule List based on which you want to retrieve risk list information for domain (s) from Recorded Future.
You can choose from the following options: Historically Reported by Insikt Group, C&C Nameserver, C&C DNS Name, C&C URL, Compromised URL, Recently Resolved to Host of Many DDNS Names, Historically Reported as a Defanged DNS Names, Recent Fast Flux DNS Name, Historically Reported in Threat List, Historically Linked to Cyber Attack, Historical Malware Analysis DNS Name, Blacklisted DNS Name, Active Phishing URL, Ransomware Distribution URL, Ransomware Payment DNS Name, Recently Reported by Insikt Group, Recently Reported as a Defanged DNS Names, Recently Linked to Cyber Attack, Recent Malware Analysis DNS Name, Recent Threat Researcher, Recent Typosquat Similarity - DNS Sandwich, Recent Typosquat Similarity - Typo or Homograph, Recently Resolved to Malicious IP, Recently Resolved to Suspicious IP, Recently Resolved to Unusual IP, Recently Resolved to Very Malicious IP, Trending in Recorded Future Analyst Community, Historical Threat Researcher, Historical Typosquat Similarity - DNS Sandwich, or Historical Typosquat Similarity - Typo or Homograph.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "stix:STIX_Package": {
        "@id": "",
        "@timestamp": "",
        "@version": "",
        "@xmlns": "",
        "@xmlns:DomainNameObj": "",
        "@xmlns:RF": "",
        "@xmlns:cybox": "",
        "@xmlns:indicator": "",
        "@xmlns:stix": "",
        "@xmlns:stixCommon": "",
        "@xmlns:stixVocabs": "",
        "@xmlns:ttp": "",
        "stix:STIX_Header": {
            "stix:Description": ""
        },
        "stix:Indicators": {
            "stix:Indicator": [
                {
                    "@id": "",
                    "@timestamp": "",
                    "@xmlns:xsi": "",
                    "@xsi:type": "",
                    "indicator:Title": "",
                    "indicator:Type": {
                        "@xsi:type": "",
                        "#text": ""
                    },
                    "indicator:Description": "",
                    "indicator:Valid_Time_Position": {
                        "indicator:Start_Time": {
                            "@precision": "",
                            "#text": ""
                        },
                        "indicator:End_Time": {
                            "@precision": "",
                            "#text": ""
                        }
                    },
                    "indicator:Observable": {
                        "@id": "",
                        "cybox:Object": {
                            "@id": "",
                            "cybox:Properties": {
                                "@type": "",
                                "@xsi:type": "",
                                "DomainNameObj:Value": {
                                    "@condition": "",
                                    "#text": ""
                                }
                            }
                        }
                    },
                    "indicator:Indicated_TTP": [
                        {
                            "stixCommon:Confidence": {
                                "stixCommon:Value": {
                                    "@xsi:type": "",
                                    "#text": ""
                                }
                            },
                            "stixCommon:TTP": {
                                "@id": "",
                                "@timestamp": "",
                                "@xsi:type": "",
                                "ttp:Title": "",
                                "ttp:Description": ""
                            }
                        }
                    ],
                    "indicator:Confidence": {
                        "stixCommon:Value": "",
                        "stixCommon:Description": ""
                    },
                    "indicator:Producer": {
                        "stixCommon:Description": "",
                        "stixCommon:References": {
                            "stixCommon:Reference": ""
                        }
                    }
                }
            ]
        }
    }
}</pre>
### operation: Search Domain
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Fields</td><td>(Optional) Fields that you want to include in the output. You can choose from the following options: Analysis Notes, Entity, Counts, Intel Card URL, Metrics, Related Entities, Risk, Sightings, Threat Lists, and Event Timestamps. By default, this option is set as Entity. you can choose one or more from Analyst Notes, Entity, Counts, Intel Card URL, Metrics, Related Entities, Risk, Sightings, Threat Lists and Event Timestamps
</td></tr><tr><td>Metadata</td><td>(Optional) Select this option to annotate the response with additional metadata explaining the response data elements. By default, this option is set as True.
</td></tr><tr><td>Limit</td><td>(Optional) Maximum number of results that this operation should return. By default, this option is set as 10.
</td></tr><tr><td>From</td><td>(Optional) Index of the first item to return from the search result.
</td></tr><tr><td>Risk Score</td><td>(Optional) Filter the search results by the risk score, which are integer values from 0 to 100.For example, Risk Score=[20,90] // same as 20 <= Risk Score <= 90
Risk Score=(20,90) // same as 20 <= Risk Score <= 90
Risk Score=[20,90) // same as 20 <= Risk Score <= 90
Risk Score=[20,) // same as 20 <= Risk Score
Risk Score=[,90) // same as Risk Score < 90
</td></tr><tr><td>First Seen</td><td>(Optional) Filter the search results by the first see date (all ElasticSearch compatible date formats are valid). For example, 2017-03-14T18:01:18.750Z, 2017-01-01, 2017/01/01
</td></tr><tr><td>Last Seen</td><td>(Optional) Filter the search results by the last see date (all ElasticSearch compatible date formats are valid).For example, 2017-03-14T18:01:18.750Z, 2017-01-01, 2017/01/01
</td></tr><tr><td>List ID</td><td>(Optional) Vulnerability ID from Recorded Future. For example, idn:ddobnajanu.club
</td></tr><tr><td>Risk Rule</td><td>(Optional) Risk Rule List based on which you want to retrieve risk list information for domain (s) from Recorded Future.
You can choose from the following options: Historically Reported by Insikt Group, C&C Nameserver, C&C DNS Name, C&C URL, Compromised URL, Recently Resolved to Host of Many DDNS Names, Historically Reported as a Defanged DNS Names, Recent Fast Flux DNS Name, Historically Reported in Threat List, Large, Historically Linked to Cyber Attack, Historical Malware Analysis DNS Name, Blacklisted DNS Name, Active Phishing URL, Ransomware Distribution URL, Ransomware Payment DNS Name, Recently Reported by Insikt Group, Recently Reported as a Defanged DNS Names, Recently Linked to Cyber Attack, Recent Malware Analysis DNS Name, Recent Threat Researcher, Recent Typosquat Similarity - DNS Sandwich, Recent Typosquat Similarity - Typo or Homograph, Recently Resolved to Malicious IP, Recently Resolved to Suspicious IP, Recently Resolved to Unusual IP, Recently Resolved to Very Malicious IP, Trending in Recorded Future Analyst Community, Historical Threat Researcher, Historical Typosquat Similarity - DNS Sandwich, or Historical Typosquat Similarity - Typo or Homograph.
</td></tr><tr><td>Parent</td><td>(Optional) Filter domains (including FQDNs) in a parent domain or a subdomain.
</td></tr><tr><td>Order By</td><td>(Optional) Order the search results by this filter criteria. You can choose from the following options: Created, Criticality, First Seen, Last Seen, Modified, Risk Score, Rules, Seven Days Hits, Sixty Days Hits, or Total Hits.
</td></tr><tr><td>Direction</td><td>(Optional) Arrange the search results either in the Ascending order or Descending order based on the risk score.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "results": [
            {
                "risk": {
                    "riskString": "",
                    "evidenceDetails": [
                        {
                            "timestamp": "",
                            "evidenceString": "",
                            "mitigationString": "",
                            "criticality": "",
                            "rule": "",
                            "criticalityLabel": ""
                        }
                    ],
                    "criticalityLabel": "",
                    "score": "",
                    "rules": "",
                    "criticality": "",
                    "riskSummary": ""
                },
                "relatedEntities": [
                    {
                        "type": "",
                        "entities": [
                            {
                                "count": "",
                                "entity": {
                                    "name": "",
                                    "id": "",
                                    "type": ""
                                }
                            }
                        ]
                    }
                ],
                "intelCard": "",
                "threatLists": [
                    {
                        "name": "",
                        "id": "",
                        "description": "",
                        "type": ""
                    }
                ],
                "metrics": [
                    {
                        "value": "",
                        "type": ""
                    }
                ],
                "analystNotes": [],
                "sightings": [
                    {
                        "title": "",
                        "published": "",
                        "type": "",
                        "url": "",
                        "fragment": "",
                        "source": ""
                    }
                ],
                "timestamps": {
                    "lastSeen": "",
                    "firstSeen": ""
                },
                "entity": {
                    "name": "",
                    "id": "",
                    "type": ""
                }
            }
        ]
    },
    "counts": {
        "returned": "",
        "total": ""
    },
    "metadata": {
        "entries": []
    }
}</pre>
### operation: Get IP Reputation
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>IP Address</td><td>IP address for which you want to retrieve reputation from Recorded Future.
</td></tr><tr><td>Fields</td><td>(Optional) Fields that you want to include in the output. You can choose from the following options: Analysis Notes, Entity, Counts, Intel Card URL, Metrics, Related Entities, Risk, Sightings, Threat Lists, and Event Timestamps. By default, this option is set as Entity. you can choose one or more from Analyst Notes, Entity, Location, Counts, Intel Card URL, Metrics, Related Entities, Risk, Sightings, Threat Lists and Event Timestamps
</td></tr><tr><td>Metadata</td><td>(Optional) Select this option to annotate the response with additional metadata explaining the response data elements. By default, this option is set as True.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "intelCard": "",
        "metrics": [
            {
                "type": "",
                "value": ""
            }
        ],
        "analystNotes": [],
        "timestamps": {
            "lastSeen": "",
            "firstSeen": ""
        },
        "sightings": [
            {
                "published": "",
                "fragment": "",
                "title": "",
                "type": "",
                "url": "",
                "source": ""
            }
        ],
        "entity": {
            "type": "",
            "id": "",
            "name": ""
        },
        "risk": {
            "score": "",
            "riskSummary": "",
            "criticality": "",
            "riskString": "",
            "evidenceDetails": [
                {
                    "criticality": "",
                    "rule": "",
                    "mitigationString": "",
                    "criticalityLabel": "",
                    "timestamp": "",
                    "evidenceString": ""
                }
            ],
            "criticalityLabel": "",
            "rules": ""
        },
        "relatedEntities": [
            {
                "type": "",
                "entities": [
                    {
                        "entity": {
                            "type": "",
                            "id": "",
                            "name": ""
                        },
                        "count": ""
                    }
                ]
            }
        ],
        "counts": [
            {
                "count": "",
                "date": ""
            }
        ],
        "threatLists": [],
        "location": {
            "cidr": {
                "type": "",
                "id": "",
                "name": ""
            },
            "organization": "",
            "asn": "",
            "location": {
                "continent": "",
                "country": "",
                "city": ""
            }
        }
    },
    "metadata": {
        "entries": []
    }
}</pre>
### operation: Get IP Risk List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Risk Rule List</td><td>(Optional) Risk Rule List based on which you want to retrieve risk list information for IP address(es) from Recorded Future.
You can choose from the following options: Historically Reported by Insikt Group, Inside Possible Bogus BGP Route, Historical Botnet Traffic, Nameserver for C&C Server, Historical C&C Server, Cyber Exploit Signal: Important, Cyber Exploit Signal: Medium, Recent Host of Many DDNS Names, Historically Reported as a Defanged IP, Resolution of Fast Flux DNS Name, Historically Reported in Threat List, Historical Honeypot Sighting, Honeypot Host, Recent C&C Server, Historically Linked to Intrusion Method, Historically Linked to APT, Historically Linked to Cyber Attack, Malicious Packet Source, Malware Delivery, Historical Multicategory Blacklist, Historical Open Proxies, Phishing Host, Historical Positive Malware Verdict, Recently Reported by Insikt Group, Recent Botnet Traffic, Current C&C Server, Recently Reported as Defanged IP, Recent Honeypot Sighting, Recently Linked to Intrusion Method, Recently Linked to APT, Recently Linked to Cyber Attack, Recent Multicategory Blacklist, Recent Open Proxies, Recent Positive Malware Verdict, Recent Spam Source, Recent SSH/Dictionary Attacker, Recent Bad SSL Association, Recent Threat Researcher, Trending in Recorded Future Analyst Community, Historical Spam Source, Historical SSH/Dictionary Attacker, Historical Bad SSL Association, Historical Threat Researcher, Tor Node, Unusual IP, or Vulnerable Host.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "stix:STIX_Package": {
        "@id": "",
        "@timestamp": "",
        "@version": "",
        "@xmlns": "",
        "@xmlns:AddressObj": "",
        "@xmlns:RF": "",
        "@xmlns:cybox": "",
        "@xmlns:indicator": "",
        "@xmlns:stix": "",
        "@xmlns:stixCommon": "",
        "@xmlns:stixVocabs": "",
        "@xmlns:ttp": "",
        "stix:STIX_Header": {
            "stix:Description": ""
        },
        "stix:Indicators": {
            "stix:Indicator": [
                {
                    "@id": "",
                    "@timestamp": "",
                    "@xmlns:xsi": "",
                    "@xsi:type": "",
                    "indicator:Title": "",
                    "indicator:Type": {
                        "@xsi:type": "",
                        "#text": ""
                    },
                    "indicator:Description": "",
                    "indicator:Valid_Time_Position": {
                        "indicator:Start_Time": {
                            "@precision": "",
                            "#text": ""
                        },
                        "indicator:End_Time": {
                            "@precision": "",
                            "#text": ""
                        }
                    },
                    "indicator:Observable": {
                        "@id": "",
                        "cybox:Object": {
                            "@id": "",
                            "cybox:Properties": {
                                "@category": "",
                                "@xsi:type": "",
                                "AddressObj:Address_Value": {
                                    "@condition": "",
                                    "#text": ""
                                }
                            }
                        }
                    },
                    "indicator:Indicated_TTP": [
                        {
                            "stixCommon:Confidence": {
                                "stixCommon:Value": {
                                    "@xsi:type": "",
                                    "#text": ""
                                }
                            },
                            "stixCommon:TTP": {
                                "@id": "",
                                "@timestamp": "",
                                "@xsi:type": "",
                                "ttp:Title": "",
                                "ttp:Description": ""
                            }
                        }
                    ],
                    "indicator:Confidence": {
                        "stixCommon:Value": "",
                        "stixCommon:Description": ""
                    },
                    "indicator:Producer": {
                        "stixCommon:Description": "",
                        "stixCommon:References": {
                            "stixCommon:Reference": ""
                        }
                    }
                }
            ]
        }
    }
}</pre>
### operation: Search IP
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Fields</td><td>(Optional) Fields that you want to include in the output. You can choose from the following options: Analysis Notes, Entity, Counts, Intel Card URL, Metrics, Related Entities, Risk, Sightings, Threat Lists, and Event Timestamps. By default, this option is set as Entity. you can choose one or more from Analyst Notes, Entity, Counts, Location, Intel Card URL, Metrics, Related Entities, Risk, Sightings, Threat Lists and Event Timestamps
</td></tr><tr><td>Metadata</td><td>(Optional) Select this option to annotate the response with additional metadata explaining the response data elements. By default, this option is set as True.
</td></tr><tr><td>Limit</td><td>(Optional) Maximum number of results that this operation should return. By default, this option is set as 10.
</td></tr><tr><td>From</td><td>(Optional) Records from offset.
</td></tr><tr><td>Range</td><td>(Optional) Range of IP addresses from starting IP address to ending IP address or CIDR.For example, 1.2.3.4/24 or 1.2.3.4-5.6.7.8.
</td></tr><tr><td>Risk Score</td><td>(Optional) Filter the search results by the risk score, which are integer values from 0 to 100.
For example, Risk Score=[20,90] // same as 20 <= Risk Score <= 90
Risk Score=(20,90) // same as 20 <= Risk Score <= 90
Risk Score=[20,90) // same as 20 <= Risk Score <= 90
Risk Score=[20,) // same as 20 <= Risk Score
Risk Score=[,90) // same as Risk Score < 90
</td></tr><tr><td>First Seen</td><td>(Optional) Filter the search results by the first see date (all ElasticSearch compatible date formats are valid).For example, 2017-03-14T18:01:18.750Z, 2017-01-01, 2017/01/01
</td></tr><tr><td>Last Seen</td><td>(Optional) Filter the search results by the last see date (all ElasticSearch compatible date formats are valid).For example, 2017-03-14T18:01:18.750Z, 2017-01-01, 2017/01/01
</td></tr><tr><td>List ID</td><td>(Optional) Vulnerability ID from Recorded Future.For example, ip:199.173.128.0/20
</td></tr><tr><td>Risk Rule</td><td>(Optional) Risk Rule List based on which you want to retrieve risk list information for IP address(es) from Recorded Future.
You can choose from the following options: Historically Reported by Insikt Group, Inside Possible Bogus BGP Route, Historical Botnet Traffic, Nameserver for C&C Server, Historical C&C Server, Cyber Exploit Signal: Important, Cyber Exploit Signal: Medium, Recent Host of Many DDNS Names, Historically Reported as a Defanged IP, Resolution of Fast Flux DNS Name, Historically Reported in Threat List, Historical Honeypot Sighting, Honeypot Host, Recent C&C Server, Large, Historically Linked to Intrusion Method, Historically Linked to APT, Historically Linked to Cyber Attack, Malicious Packet Source, Malware Delivery, Historical Multicategory Blacklist, Historical Open Proxies, Phishing Host, Historical Positive Malware Verdict, Recently Reported by Insikt Group, Recent Botnet Traffic, Current C&C Server, Recently Reported as Defanged IP, Recent Honeypot Sighting, Recently Linked to Intrusion Method, Recently Linked to APT, Recently Linked to Cyber Attack, Recent Multicategory Blacklist, Recent Open Proxies, Recent Positive Malware Verdict, Recent Spam Source, Recent SSH/Dictionary Attacker, Recent Bad SSL Association, Recent Threat Researcher, Trending in Recorded Future Analyst Community, Historical Spam Source, Historical SSH/Dictionary Attacker, Historical Bad SSL Association, Historical Threat Researcher, Tor Node, Unusual IP, or Vulnerable Host. you can choose from Historically Reported by Insikt Group, Inside Possible Bogus BGP Route, Historical Botnet Traffic, Nameserver for C&C Server, Historical C&C Server, Cyber Exploit Signal: Important, Cyber Exploit Signal: Medium, Recent Host of Many DDNS Names, Historically Reported as a Defanged IP, Resolution of Fast Flux DNS Name, Historically Reported in Threat List, Historical Honeypot Sighting, Honeypot Host, Recent C&C Server, Large, Historically Linked to Intrusion Method, Historically Linked to ATP, Historically Linked to Cyber Attack, Malicious Packet Source, Malware Delivery, Historical Multicategory Blacklist, Historical Open Proxies, Phishing Host, Historical Positive Malware Verdict, Recently Reported by Insikt Group, Recent Botnet Traffic, Current C&C Server, Recently Reported as Defanged IP, Recent Honeypot Sighting, Recently Linked to Intrusion Method, Recently Linked to APT, Recently Linked to Cyber Attack, Recent Multicategory Blacklist, Recent Open Proxies, Recent Positive Malware Verdict, Recent Spam Source, Recent SSH/Dictionary Attacker, Recent Bad SSL Association, Recent Threat Researcher, Trending in Recorded Future Analyst Community, Historical Spam Source, Historical SSH/Dictionary Attacker, Historical Bad SSL Association, Historical Threat Researcher, Tor Node, Unusual IP and Vulnerable Host
</td></tr><tr><td>Order By</td><td>(Optional) Order the search results by this filter criteria. You can choose from the following options: Created, Criticality, First Seen, Last Seen, Modified, Risk Score, Rules, Seven Days Hits, Sixty Days Hits, or Total Hits.
</td></tr><tr><td>Direction</td><td>(Optional) Arrange the search results either in the Ascending order or Descending order based on the risk score.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "counts": {
        "total": "",
        "returned": ""
    },
    "metadata": {
        "entries": []
    },
    "data": {
        "results": [
            {
                "metrics": [
                    {
                        "type": "",
                        "value": ""
                    }
                ],
                "location": {
                    "cidr": {
                        "id": "",
                        "type": "",
                        "name": ""
                    },
                    "asn": "",
                    "organization": "",
                    "location": {
                        "country": "",
                        "continent": ""
                    }
                },
                "intelCard": "",
                "sightings": [
                    {
                        "source": "",
                        "type": "",
                        "url": "",
                        "fragment": "",
                        "published": "",
                        "title": ""
                    }
                ],
                "timestamps": {
                    "lastSeen": "",
                    "firstSeen": ""
                },
                "counts": [
                    {
                        "count": "",
                        "date": ""
                    }
                ],
                "entity": {
                    "id": "",
                    "type": "",
                    "name": ""
                },
                "risk": {
                    "score": "",
                    "criticalityLabel": "",
                    "rules": "",
                    "evidenceDetails": [
                        {
                            "criticalityLabel": "",
                            "evidenceString": "",
                            "mitigationString": "",
                            "criticality": "",
                            "rule": "",
                            "timestamp": ""
                        }
                    ],
                    "riskString": "",
                    "criticality": "",
                    "riskSummary": ""
                },
                "analystNotes": [],
                "threatLists": [
                    {
                        "id": "",
                        "type": "",
                        "name": "",
                        "description": ""
                    }
                ],
                "relatedEntities": [
                    {
                        "type": "",
                        "entities": [
                            {
                                "count": "",
                                "entity": {
                                    "id": "",
                                    "type": "",
                                    "name": ""
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }
}</pre>
### operation: Get File Reputation
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Filehash</td><td>Filehash (MD5, SHA-1 or SHA-256) whose reputation you want to retrieve from Recorded Future.
</td></tr><tr><td>Fields</td><td>(Optional) Fields that you want to include in the output. You can choose from the following options: Analysis Notes, Entity, Counts, Intel Card URL, Metrics, Related Entities, Risk, Sightings, Threat Lists, and Event Timestamps. By default, this option is set as Entity. you can choose one or more from Analyst Notes, Entity, Counts, Hash Algorithm, Intel Card URL, Metrics, Related Entities, Risk, Sightings, Threat Lists and Event Timestamps
</td></tr><tr><td>Metadata</td><td>(Optional) Select this option to annotate the response with additional metadata explaining the response data elements.By default, this option is set as True.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "metadata": {
        "entries": []
    },
    "data": {
        "timestamps": {
            "firstSeen": "",
            "lastSeen": ""
        },
        "entity": {
            "type": "",
            "id": "",
            "name": ""
        },
        "analystNotes": [],
        "sightings": [
            {
                "published": "",
                "fragment": "",
                "title": "",
                "type": "",
                "url": "",
                "source": ""
            }
        ],
        "risk": {
            "score": "",
            "riskSummary": "",
            "criticality": "",
            "riskString": "",
            "evidenceDetails": [
                {
                    "criticality": "",
                    "rule": "",
                    "mitigationString": "",
                    "criticalityLabel": "",
                    "timestamp": "",
                    "evidenceString": ""
                }
            ],
            "criticalityLabel": "",
            "rules": ""
        },
        "threatLists": [],
        "hashAlgorithm": "",
        "intelCard": "",
        "relatedEntities": [
            {
                "type": "",
                "entities": [
                    {
                        "entity": {
                            "type": "",
                            "id": "",
                            "name": ""
                        },
                        "count": ""
                    }
                ]
            }
        ],
        "counts": [
            {
                "count": "",
                "date": ""
            }
        ],
        "metrics": [
            {
                "type": "",
                "value": ""
            }
        ]
    }
}</pre>
### operation: Get File Risk List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Risk Rule List</td><td>(Optional) Risk Rule List based on which you want to retrieve risk list information for file(s) from Recorded Future.
You can choose from the following options: Reported by Insikt Group, Historically Reported in Threat List, Linked to Cyber Attack, Linked to Malware, Linked to Attack Vector, Linked to Vulnerability, Malware SSL Certificate Fingerprint, Positive Malware Verdict, Trending in Recorded Future Analyst Community, or Threat Researcher.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "stix:STIX_Package": {
        "@id": "",
        "@timestamp": "",
        "@version": "",
        "@xmlns": "",
        "@xmlns:FileObj": "",
        "@xmlns:RF": "",
        "@xmlns:cybox": "",
        "@xmlns:cyboxCommon": "",
        "@xmlns:cyboxVocabs": "",
        "@xmlns:indicator": "",
        "@xmlns:stix": "",
        "@xmlns:stixCommon": "",
        "@xmlns:stixVocabs": "",
        "@xmlns:ttp": "",
        "stix:STIX_Header": {
            "stix:Description": ""
        },
        "stix:Indicators": {
            "stix:Indicator": [
                {
                    "@id": "",
                    "@timestamp": "",
                    "@xmlns:xsi": "",
                    "@xsi:type": "",
                    "indicator:Title": "",
                    "indicator:Type": {
                        "@xsi:type": "",
                        "#text": ""
                    },
                    "indicator:Description": "",
                    "indicator:Valid_Time_Position": {
                        "indicator:Start_Time": {
                            "@precision": "",
                            "#text": ""
                        },
                        "indicator:End_Time": {
                            "@precision": "",
                            "#text": ""
                        }
                    },
                    "indicator:Observable": {
                        "@id": "",
                        "cybox:Object": {
                            "@id": "",
                            "cybox:Properties": {
                                "@xsi:type": "",
                                "FileObj:Hashes": {
                                    "cyboxCommon:Hash": {
                                        "cyboxCommon:Type": {
                                            "@xsi:type": "",
                                            "#text": ""
                                        },
                                        "cyboxCommon:Simple_Hash_Value": {
                                            "@condition": "",
                                            "#text": ""
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "indicator:Indicated_TTP": [
                        {
                            "stixCommon:Confidence": {
                                "stixCommon:Value": {
                                    "@xsi:type": "",
                                    "#text": ""
                                }
                            },
                            "stixCommon:TTP": {
                                "@id": "",
                                "@timestamp": "",
                                "@xsi:type": "",
                                "ttp:Title": "",
                                "ttp:Description": ""
                            }
                        }
                    ],
                    "indicator:Confidence": {
                        "stixCommon:Value": "",
                        "stixCommon:Description": ""
                    },
                    "indicator:Producer": {
                        "stixCommon:Description": "",
                        "stixCommon:References": {
                            "stixCommon:Reference": ""
                        }
                    }
                }
            ]
        }
    }
}</pre>
### operation: Search Filehash
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Fields</td><td>(Optional) Fields that you want to include in the output. You can choose from the following options: Analysis Notes, Entity, Counts, Intel Card URL, Metrics, Related Entities, Risk, Sightings, Threat Lists, and Event Timestamps. By default, this option is set as Entity. you can choose one or more from Analyst Notes, Entity, Counts, Intel Card URL, Metrics, Related Entities, Hash Algorithm, Risk, Sightings, Threat Lists and Event Timestamps
</td></tr><tr><td>Metadata</td><td>(Optional) Select this option to annotate the response with additional metadata explaining the response data elements. By default, this option is set as True.
</td></tr><tr><td>Limit</td><td>(Optional) Maximum number of results that this operation should return. By default, this option is set as 10.
</td></tr><tr><td>From</td><td>(Optional) Records from offset.
</td></tr><tr><td>Risk Score</td><td>(Optional) Filter the search results by the risk score, which are integer values from 0 to 100.
For example, Risk Score=[20,90] // same as 20 <= Risk Score <= 90
Risk Score=(20,90) // same as 20 <= Risk Score <= 90
Risk Score=[20,90) // same as 20 <= Risk Score <= 90
Risk Score=[20,) // same as 20 <= Risk Score
Risk Score=[,90) // same as Risk Score < 90
</td></tr><tr><td>Algorithm</td><td>(Optional) Filter the search results by the hash algorithm. You can choose from the following options: CRC-32, CTPH, MD5, SHA-1, SHA-256, or SHA-512.
</td></tr><tr><td>First Seen</td><td>(Optional) Filter the search results by the first see date (all ElasticSearch compatible date formats are valid).For example, 2017-03-14T18:01:18.750Z, 2017-01-01, 2017/01/01
</td></tr><tr><td>Last Seen</td><td>(Optional) Filter the search results by the last see date (all ElasticSearch compatible date formats are valid). For example, 2017-03-14T18:01:18.750Z, 2017-01-01, 2017/01/01
</td></tr><tr><td>List ID</td><td>(Optional) Vulnerability ID from Recorded Future.For example, hash:1d724f95c61f1055f0d02c2154bbccd3
</td></tr><tr><td>Risk Rule</td><td>(Optional) Risk Rule List based on which you want to retrieve risk list information for filehash(es) from Recorded Future.
You can choose from the following options: Reported by Insikt Group, Historically Reported in Threat List, Linked to Cyber Attack, Linked to Malware, Linked to Attack Vector, Linked to Vulnerability, Malware SSL Certificate Fingerprint, Positive Malware Verdict, Trending in Recorded Future Analyst Community, or Threat Researcher.
</td></tr><tr><td>Order By</td><td>(Optional) Order the search results by this filter criteria. You can choose from the following options: Created, Criticality, First Seen, Last Seen, Modified, Risk Score, Rules, Seven Days Hits, Sixty Days Hits, or Total Hits.
</td></tr><tr><td>Direction</td><td>(Optional) Arrange the search results either in the Ascending order or Descending order based on the risk score.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "metadata": {
        "entries": [
            {
                "key": "",
                "item": {
                    "entries": [
                        {
                            "key": "",
                            "item": {
                                "entries": [
                                    {
                                        "key": "",
                                        "label": "",
                                        "type": ""
                                    }
                                ],
                                "type": ""
                            },
                            "label": "",
                            "type": ""
                        }
                    ],
                    "type": ""
                },
                "label": "",
                "type": ""
            }
        ]
    },
    "counts": {
        "total": "",
        "returned": ""
    },
    "data": {
        "results": [
            {
                "intelCard": "",
                "analystNotes": [],
                "relatedEntities": [
                    {
                        "entities": [
                            {
                                "count": "",
                                "entity": {
                                    "type": "",
                                    "name": "",
                                    "id": ""
                                }
                            }
                        ],
                        "type": ""
                    }
                ],
                "entity": {
                    "type": "",
                    "name": "",
                    "id": ""
                },
                "timestamps": {
                    "lastSeen": "",
                    "firstSeen": ""
                },
                "counts": [
                    {
                        "count": "",
                        "date": ""
                    }
                ],
                "sightings": [
                    {
                        "published": "",
                        "fragment": "",
                        "title": "",
                        "source": "",
                        "url": "",
                        "type": ""
                    }
                ],
                "threatLists": [],
                "hashAlgorithm": "",
                "risk": {
                    "rules": "",
                    "score": "",
                    "evidenceDetails": [
                        {
                            "rule": "",
                            "timestamp": "",
                            "evidenceString": "",
                            "criticality": "",
                            "criticalityLabel": ""
                        }
                    ],
                    "riskSummary": "",
                    "criticalityLabel": "",
                    "riskString": "",
                    "criticality": ""
                },
                "metrics": [
                    {
                        "value": "",
                        "type": ""
                    }
                ]
            }
        ]
    }
}</pre>
### operation: Lookup Vulnerability
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>CVE/RF ID</td><td>CVE Identifier ID or Recorded Future ID whose reputation you want to retrieve from Recorded Future. For example CVE IDs: CVE-2018-8811, CVE-2018-8810. RF ID = Vga53v
</td></tr><tr><td>Fields</td><td>(Optional) Fields that you want to include in the output.
You can choose from the following options: National Vulnerability Database description, Analyst Notes, Common Names, Entity, Counts, Common Platform Enumeration, Common Platform Enumeration 2.2 URI, Common Vulnerability Scoring System, Intel Card URL, Metrics, Related Entities, Related Links, Risk, Sightings, Threat Lists, or Event Timestamps.
</td></tr><tr><td>Metadata</td><td>(Optional) Select this option to annotate the response with additional metadata explaining the response data elements. By default, this option is set as True.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "metadata": {
        "entries": []
    },
    "data": {
        "entity": {
            "name": "",
            "type": "",
            "id": "",
            "description": ""
        },
        "threatLists": [],
        "counts": [
            {
                "count": "",
                "date": ""
            }
        ],
        "intelCard": "",
        "relatedEntities": [
            {
                "type": "",
                "entities": [
                    {
                        "entity": {
                            "name": "",
                            "type": "",
                            "id": ""
                        },
                        "count": ""
                    }
                ]
            }
        ],
        "cpe22uri": [],
        "cpe": [],
        "timestamps": {
            "firstSeen": "",
            "lastSeen": ""
        },
        "cvss": {
            "lastModified": "",
            "published": ""
        },
        "analystNotes": [],
        "nvdDescription": "",
        "sightings": [
            {
                "url": "",
                "title": "",
                "type": "",
                "published": "",
                "fragment": "",
                "source": ""
            }
        ],
        "commonNames": [],
        "risk": {
            "evidenceDetails": [
                {
                    "criticality": "",
                    "criticalityLabel": "",
                    "rule": "",
                    "evidenceString": "",
                    "timestamp": ""
                }
            ],
            "rules": "",
            "riskSummary": "",
            "score": "",
            "criticalityLabel": "",
            "criticality": "",
            "riskString": ""
        },
        "relatedLinks": [],
        "metrics": [
            {
                "type": "",
                "value": ""
            }
        ]
    }
}</pre>
### operation: Get vulnerability Risk List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Risk Rule List</td><td>(Optional) Risk Rule List based on which you want to retrieve risk list information for vulnerability(ies) from Recorded Future.
You can choose from the following options: Historically Reported by Insikt Group, Web Reporting Prior to CVSS Score, Cyber Exploit Signal: Critical, Cyber Exploit Signal: Important, Cyber Exploit Signal: Medium, Linked to Historical Cyber Exploit, Historically Linked to Exploit Kit, Historically Linked to Malware, Historically Linked to Remote Access Trojan, Historically Linked to Ransomware, Linked to Recent Cyber Exploit, Recently Linked to Exploit Kit, Recently Linked to Malware, Recently Linked to Remote Access Trojan, Recently Linked to Ransomware, NIST Severity: Critical, NIST Severity: High, NIST Severity: Low, NIST Severity: Medium, Web Reporting Prior to NVD Disclosure, Recently Reported by Insikt Group, Recently Linked to Penetration Testing Tools, or Historically Linked to Penetration Testing Tools.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "stix:STIX_Package": {
        "@id": "",
        "@timestamp": "",
        "@version": "",
        "@xmlns": "",
        "@xmlns:RF": "",
        "@xmlns:cybox": "",
        "@xmlns:et": "",
        "@xmlns:stix": "",
        "@xmlns:stixCommon": "",
        "stix:STIX_Header": {
            "stix:Description": ""
        },
        "stix:Exploit_Targets": {
            "stixCommon:Exploit_Target": [
                {
                    "@id": "",
                    "@timestamp": "",
                    "@xmlns:xsi": "",
                    "@xsi:type": "",
                    "et:Title": "",
                    "et:Description": "",
                    "et:Vulnerability": {
                        "et:CVE_ID": "",
                        "et:CVSS_Score": {
                            "et:Overall_Score": ""
                        },
                        "et:Published_DateTime": "",
                        "et:Affected_Software": {
                            "et:Affected_Software": {
                                "stixCommon:Observable": {
                                    "@id": "",
                                    "cybox:Title": ""
                                }
                            }
                        },
                        "et:References": {
                            "stixCommon:Reference": ""
                        }
                    }
                }
            ]
        }
    }
}</pre>
### operation: Search Vulnerabilities
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Free Text</td><td>(Optional) Free text (not regex) string matching which list IDs are returned as the search result.
</td></tr><tr><td>Fields</td><td>(Optional) Fields that you want to include in the output.
You can choose from the following options: National Vulnerability Database description, Analyst Notes, Common Names, Entity, Counts, Common Platform Enumeration, Common Platform Enumeration 2.2 URI, Common Vulnerability Scoring System, Intel Card URL, Metrics, Related Entities, Related Links, Risk, Sightings, Threat Lists, or Event Timestamps.
</td></tr><tr><td>Metadata</td><td>(Optional) Select this option to annotate the response with additional metadata explaining the response data elements.By default, this option is set as True.
</td></tr><tr><td>Limit</td><td>(Optional) Maximum number of results that this operation should return. By default, this option is set as 10.
</td></tr><tr><td>From</td><td>(Optional) Records from offset.
</td></tr><tr><td>Risk Score</td><td>(Optional) Filter the search results by the risk score, which are integer values from 0 to 100.
For example, Risk Score=[20,90] // same as 20 <= Risk Score <= 90
Risk Score=(20,90) // same as 20 <= Risk Score <= 90
Risk Score=[20,90) // same as 20 <= Risk Score <= 90
Risk Score=[20,) // same as 20 <= Risk Score
Risk Score=[,90) // same as Risk Score < 90
</td></tr><tr><td>CVSS Score</td><td>(Optional) Filter the search results by the common vulnerability scoring system score (CVSS score). You can enter a number between 0 to 10 as the CVSS score in the format [0,10]
For example, [2,9.3], (2,9.3), [2,3.6), (6,), (,8) . Working of the CVSS score examples is the same as the risk score examples.
</td></tr><tr><td>First Seen</td><td>(Optional) Filter the search results by the first see date (all ElasticSearch compatible date formats are valid). For example, 2017-03-14T18:01:18.750Z, 2017-01-01, 2017/01/01
</td></tr><tr><td>Last Seen</td><td>(Optional) Filter the search results by the last see date (all ElasticSearch compatible date formats are valid).For example, 2017-03-14T18:01:18.750Z, 2017-01-01, 2017/01/01
</td></tr><tr><td>List ID</td><td>(Optional) Vulnerability ID from Recorded Future.For example, PGW3XH
</td></tr><tr><td>Risk Rule</td><td>(Optional) Risk Rule List based on which you want to retrieve risk list information for vulnerability(ies) from Recorded Future.
You can choose from the following options: Historically Reported by Insikt Group, Web Reporting Prior to CVSS Score, Cyber Exploit Signal: Critical, Cyber Exploit Signal: Important, Cyber Exploit Signal: Medium, Large, Linked to Historical Cyber Exploit, Historically Linked to Exploit Kit, Historically Linked to Malware, Historically Linked to Remote Access Trojan, Historically Linked to Ransomware, Linked to Recent Cyber Exploit, Recently Linked to Exploit Kit, Recently Linked to Malware, Recently Linked to Remote Access Trojan, Recently Linked to Ransomware, NIST Severity: Critical, NIST Severity: High, NIST Severity: Low, NIST Severity: Medium, Web Reporting Prior to NVD Disclosure, Recently Reported by Insikt Group, Recently Linked to Penetration Testing Tools, or Historically Linked to Penetration Testing Tools.
</td></tr><tr><td>Order By</td><td>(Optional) Order the search results by this filter criteria. You can choose from the following options: Created, Criticality, First Seen, Last Seen, Modified, Risk Score, Rules, Seven Days Hits, Sixty Days Hits, or Total Hits.
</td></tr><tr><td>Direction</td><td>(Optional) Arrange the search results either in the Ascending order or Descending order based on the risk score.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "metadata": {
        "entries": []
    },
    "counts": {
        "total": "",
        "returned": ""
    },
    "data": {
        "results": [
            {
                "sightings": [
                    {
                        "title": "",
                        "type": "",
                        "source": "",
                        "fragment": "",
                        "published": "",
                        "url": ""
                    }
                ],
                "analystNotes": [
                    {
                        "id": "",
                        "source": "",
                        "attributes": {
                            "title": "",
                            "context_entities": [
                                {
                                    "name": "",
                                    "id": "",
                                    "type": ""
                                }
                            ],
                            "topic": {
                                "name": "",
                                "id": "",
                                "type": ""
                            },
                            "validated_on": "",
                            "validation_urls": [
                                {
                                    "name": "",
                                    "id": "",
                                    "type": ""
                                }
                            ],
                            "text": "",
                            "published": "",
                            "note_entities": [
                                {
                                    "name": "",
                                    "id": "",
                                    "description": "",
                                    "type": ""
                                }
                            ]
                        }
                    }
                ],
                "cvss": {
                    "integrity": "",
                    "accessVector": "",
                    "availability": "",
                    "confidentiality": "",
                    "score": "",
                    "lastModified": "",
                    "published": "",
                    "accessComplexity": "",
                    "authentication": ""
                },
                "cpe": [],
                "counts": [
                    {
                        "date": "",
                        "count": ""
                    }
                ],
                "commonNames": [],
                "nvdDescription": "",
                "relatedLinks": [],
                "entity": {
                    "name": "",
                    "id": "",
                    "description": "",
                    "type": ""
                },
                "timestamps": {
                    "lastSeen": "",
                    "firstSeen": ""
                },
                "threatLists": [],
                "risk": {
                    "riskSummary": "",
                    "evidenceDetails": [
                        {
                            "evidenceString": "",
                            "timestamp": "",
                            "rule": "",
                            "criticality": "",
                            "criticalityLabel": ""
                        }
                    ],
                    "rules": "",
                    "criticality": "",
                    "riskString": "",
                    "criticalityLabel": "",
                    "score": ""
                },
                "intelCard": "",
                "relatedEntities": [
                    {
                        "type": "",
                        "entities": [
                            {
                                "count": "",
                                "entity": {
                                    "name": "",
                                    "id": "",
                                    "type": ""
                                }
                            }
                        ]
                    }
                ],
                "metrics": [
                    {
                        "type": "",
                        "value": ""
                    }
                ],
                "cpe22uri": []
            }
        ]
    }
}</pre>
### operation: Lookup URL
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>URL</td><td>URL for which you want to retrieve threat information from Recorded Future.
</td></tr><tr><td>Fields</td><td>(Optional) Fields that you want to include in the output. You can choose from the following options: Analyst Notes, Entity, Counts, Metrics, Related Entities, Risk, Sightings, or Event Timestamps.
</td></tr><tr><td>Metadata</td><td>(Optional) Select this option to annotate the response with additional metadata explaining the response data elements. By default, this option is set as True.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "metadata": {
        "entries": []
    },
    "data": {
        "relatedEntities": [],
        "risk": {
            "rules": "",
            "criticalityLabel": "",
            "riskSummary": "",
            "criticality": "",
            "score": "",
            "riskString": "",
            "evidenceDetails": [
                {
                    "evidenceString": "",
                    "criticalityLabel": "",
                    "criticality": "",
                    "rule": "",
                    "timestamp": ""
                }
            ]
        },
        "analystNotes": [
            {
                "attributes": {
                    "validated_on": "",
                    "published": "",
                    "validation_urls": [
                        {
                            "type": "",
                            "id": "",
                            "name": ""
                        }
                    ],
                    "title": "",
                    "note_entities": [
                        {
                            "type": "",
                            "id": "",
                            "name": ""
                        }
                    ],
                    "text": "",
                    "topic": {
                        "type": "",
                        "id": "",
                        "name": ""
                    },
                    "tlp": ""
                },
                "source": "",
                "id": ""
            }
        ],
        "entity": {
            "type": "",
            "id": "",
            "name": ""
        },
        "timestamps": {
            "firstSeen": "",
            "lastSeen": ""
        },
        "metrics": [
            {
                "type": "",
                "value": ""
            }
        ],
        "counts": [
            {
                "date": "",
                "count": ""
            }
        ],
        "sightings": []
    }
}</pre>
### operation: Get URL Risk List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Risk Rule List</td><td>(Optional) Risk Rule List based on which you want to retrieve risk list information for URL(s) from Recorded Future. You can choose from the following options: C&C URL, Compromised URL, Historically Reported as a Defanged URL, Historically Reported in Threat List, Large, Active Phishing URL, Ransomware Distribution URL, or Recently Reported as e Defanged URL.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "stix:STIX_Package": {
        "@id": "",
        "@timestamp": "",
        "@version": "",
        "@xmlns": "",
        "@xmlns:RF": "",
        "@xmlns:URIObj": "",
        "@xmlns:cybox": "",
        "@xmlns:indicator": "",
        "@xmlns:stix": "",
        "@xmlns:stixCommon": "",
        "@xmlns:stixVocabs": "",
        "@xmlns:ttp": "",
        "stix:STIX_Header": {
            "stix:Description": ""
        },
        "stix:Indicators": {
            "stix:Indicator": [
                {
                    "@id": "",
                    "@timestamp": "",
                    "@xmlns:xsi": "",
                    "@xsi:type": "",
                    "indicator:Title": "",
                    "indicator:Type": {
                        "@xsi:type": "",
                        "#text": ""
                    },
                    "indicator:Description": "",
                    "indicator:Valid_Time_Position": {
                        "indicator:Start_Time": {
                            "@precision": "",
                            "#text": ""
                        },
                        "indicator:End_Time": {
                            "@precision": "",
                            "#text": ""
                        }
                    },
                    "indicator:Observable": {
                        "@id": "",
                        "cybox:Object": {
                            "@id": "",
                            "cybox:Properties": {
                                "@xsi:type": "",
                                "URIObj:Value": {
                                    "@condition": "",
                                    "#text": ""
                                }
                            }
                        }
                    },
                    "indicator:Indicated_TTP": [
                        {
                            "stixCommon:Confidence": {
                                "stixCommon:Value": {
                                    "@xsi:type": "",
                                    "#text": ""
                                }
                            },
                            "stixCommon:TTP": {
                                "@id": "",
                                "@timestamp": "",
                                "@xsi:type": "",
                                "ttp:Title": "",
                                "ttp:Description": ""
                            }
                        }
                    ],
                    "indicator:Confidence": {
                        "stixCommon:Value": "",
                        "stixCommon:Description": ""
                    },
                    "indicator:Producer": {
                        "stixCommon:Description": "",
                        "stixCommon:References": {
                            "stixCommon:Reference": ""
                        }
                    }
                }
            ]
        }
    }
}</pre>
### operation: Search URL
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Fields</td><td>(Optional) Fields that you want to include in the output. You can choose from the following options: Analyst Notes, Entity, Counts, Metrics, Related Entities, Risk, Sightings, or Event Timestamps.
</td></tr><tr><td>Metadata</td><td>(Optional) Select this option to annotate the response with additional metadata explaining the response data elements.By default, this option is set as True.
</td></tr><tr><td>Limit</td><td>(Optional) Maximum number of results that this operation should return. By default, this option is set as 10.
</td></tr><tr><td>From</td><td>(Optional) Records from offset.
</td></tr><tr><td>Risk Score</td><td>(Optional) Filter the search results by the risk score, which are integer values from 0 to 100.
For example, Risk Score=[20,90] // same as 20 <= Risk Score <= 90
Risk Score=(20,90) // same as 20 <= Risk Score <= 90
Risk Score=[20,90) // same as 20 <= Risk Score <= 90
Risk Score=[20,) // same as 20 <= Risk Score
Risk Score=[,90) // same as Risk Score < 90
</td></tr><tr><td>First Seen</td><td>(Optional) Filter the search results by the first see date (all ElasticSearch compatible date formats are valid). For example, 2017-03-14T18:01:18.750Z, 2017-01-01, 2017/01/01
</td></tr><tr><td>Last Seen</td><td>(Optional) Filter the search results by the last see date (all ElasticSearch compatible date formats are valid). For example, 2017-03-14T18:01:18.750Z, 2017-01-01, 2017/01/01
</td></tr><tr><td>List ID</td><td>(Optional) Vulnerability ID from Recorded Future. For example, url:http://examplendv.com/niugufvt4
</td></tr><tr><td>Risk Rule</td><td>(Optional) Risk Rule List based on which you want to retrieve risk list information for URL(s) from Recorded Future. You can choose from the following options: C&C URL, Compromised URL, Historically Reported as a Defanged URL, Historically Reported in Threat List, Active Phishing URL, Ransomware Distribution URL, or Recently Reported as e Defanged URL.
</td></tr><tr><td>Order By</td><td>(Optional) Order the search results by this filter criteria.
You can choose from the following options: Created, Criticality, First Seen, Last Seen, Modified, Risk Score, Rules, Seven Days Hits, Sixty Days Hits, or Total Hits.
</td></tr><tr><td>Direction</td><td>(Optional) Arrange the search results either in the Ascending order or Descending order based on the risk score.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "results": [
            {
                "risk": {
                    "score": "",
                    "riskString": "",
                    "criticalityLabel": "",
                    "riskSummary": "",
                    "evidenceDetails": [
                        {
                            "evidenceString": "",
                            "criticality": "",
                            "timestamp": "",
                            "criticalityLabel": "",
                            "rule": "",
                            "mitigationString": ""
                        }
                    ],
                    "rules": "",
                    "criticality": ""
                },
                "analystNotes": [],
                "entity": {
                    "name": "",
                    "type": "",
                    "id": ""
                },
                "sightings": [],
                "metrics": [
                    {
                        "value": "",
                        "type": ""
                    }
                ],
                "relatedEntities": [],
                "timestamps": {
                    "firstSeen": "",
                    "lastSeen": ""
                },
                "counts": [
                    {
                        "count": "",
                        "date": ""
                    }
                ]
            }
        ]
    },
    "metadata": {
        "entries": []
    },
    "counts": {
        "returned": "",
        "total": ""
    }
}</pre>
### operation: Lookup Malware
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>ID</td><td>ID of the Malware for which you want to retrieve threat information from Recorded Future.
</td></tr><tr><td>Fields</td><td>(Optional) Fields that you want to include in the output. You can choose from the following options: Analyst Notes, Entity, Counts, Metrics, Intel Card URL, Related Entities, Sightings, Categories, or Event Timestamps.
</td></tr><tr><td>Metadata</td><td>(Optional) Select this option to annotate the response with additional metadata explaining the response data elements. By default, this option is set as True.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "metadata": {
        "entries": []
    },
    "data": {
        "sightings": [
            {
                "fragment": "",
                "source": "",
                "published": "",
                "url": "",
                "title": "",
                "type": ""
            }
        ],
        "counts": [
            {
                "count": "",
                "date": ""
            }
        ],
        "entity": {
            "type": "",
            "id": "",
            "name": ""
        },
        "metrics": [
            {
                "value": "",
                "type": ""
            }
        ],
        "intelCard": "",
        "analystNotes": [],
        "timestamps": {
            "firstSeen": "",
            "lastSeen": ""
        },
        "categories": [
            {
                "type": "",
                "id": "",
                "name": ""
            }
        ],
        "relatedEntities": [
            {
                "type": "",
                "entities": [
                    {
                        "count": "",
                        "entity": {
                            "type": "",
                            "id": "",
                            "name": ""
                        }
                    }
                ]
            }
        ]
    }
}</pre>
### operation: Search Malware
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Free Text</td><td>(Optional) Free text (not regex) string matching which list IDs are returned as the search result.
</td></tr><tr><td>Fields</td><td>(Optional) Fields that you want to include in the output. You can choose from the following options: Analyst Notes, Entity, Counts, Metrics, Intel Card URL, Related Entities, Sightings, Categories, or Event Timestamps.
</td></tr><tr><td>Metadata</td><td>(Optional) Select this option to annotate the response with additional metadata explaining the response data elements.By default, this option is set as True.
</td></tr><tr><td>Limit</td><td>(Optional) Maximum number of results that this operation should return. By default, this option is set as 10.
</td></tr><tr><td>From</td><td>(Optional) Records from offset.
</td></tr><tr><td>First Seen</td><td>(Optional) Filter the search results by the first see date (all ElasticSearch compatible date formats are valid). For example, 2017-03-14T18:01:18.750Z, 2017-01-01, 2017/01/01
</td></tr><tr><td>Last Seen</td><td>(Optional) Filter the search results by the last see date (all ElasticSearch compatible date formats are valid).For example, 2017-03-14T18:01:18.750Z, 2017-01-01, 2017/01/01
</td></tr><tr><td>List ID</td><td>(Optional) Vulnerability ID from Recorded Future. For example, Ps4Y1A
</td></tr><tr><td>Order By</td><td>(Optional) Order the search results by this filter criteria. You can choose from the following options: Created, Criticality, First Seen, Last Seen, Modified, Risk Score, Rules, Seven Days Hits, Sixty Days Hits, or Total Hits.
</td></tr><tr><td>Direction</td><td>(Optional) Arrange the search results either in the Ascending order or Descending order based on metrics (counts of recent references and metric values for various risk rules).
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "results": [
            {
                "metrics": [
                    {
                        "value": "",
                        "type": ""
                    }
                ],
                "categories": [],
                "entity": {
                    "name": "",
                    "type": "",
                    "id": ""
                },
                "timestamps": {
                    "firstSeen": "",
                    "lastSeen": ""
                },
                "analystNotes": [],
                "counts": [],
                "intelCard": "",
                "relatedEntities": [],
                "sightings": []
            }
        ]
    },
    "counts": {
        "returned": "",
        "total": ""
    },
    "metadata": {
        "entries": []
    }
}</pre>
### operation: Get Alert
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Alert ID</td><td>ID of the alert generated on Recorded Future for which you want to retrieve information from Recorded Future.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Search Alerts
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Triggered</td><td>(Optional) DateTime when the alert was generated on Recorded Future. All Elasticsearch compatible date formats are valid. Relative time expressions are also supported, such as -2d for two days prior to today and yesterday. As with absolute time references, both ends of the range still need to be specified. For example, to search for alerts that fired within the last 24 hrs, use triggered = [-24h,].
</td></tr><tr><td>Assignee</td><td>(Optional) Filter the search results by the name of the assignee to whom the alert was assigned in Recorded Future, using the email address associated with that user account.
</td></tr><tr><td>Status</td><td>(Optional) Status of the alert. You can choose from the following options: Unassigned, Assigned, Actionable, No Action, or Tuning.
</td></tr><tr><td>Alert Rule ID</td><td>(Optional) Recorded Future's Alert Rule ID that is associated with the alert notification.
</td></tr><tr><td>Free Text</td><td>(Optional) Free text (not regex) string matching which list IDs are returned as the search result.
</td></tr><tr><td>Limit</td><td>(Optional) Maximum number of results that this operation should return.By default, this option is set as 10.
</td></tr><tr><td>From</td><td>(Optional) Records from offset.
</td></tr><tr><td>Order By</td><td>(Optional) Order the search results by this filter criteria. Currently, only the Triggered option is available.
</td></tr><tr><td>Direction</td><td>(Optional) Arrange the search results either in the Ascending order or Descending order.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Search Alert Rules
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Free Text</td><td>(Optional) Free text (not regex) string matching which list IDs are returned as the search result.
</td></tr><tr><td>Limit</td><td>(Optional) Maximum number of results that this operation should return. By default, this option is set as 10.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Risk Rules
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Risk Rules For</td><td>Risk rules have to be retrieved for the selected input from Recorded Future. You can choose from the following options: IP, Domain, URL, File, or Vulnerability.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "results": [
            {
                "description": "",
                "criticality": "",
                "criticalityLabel": "",
                "count": "",
                "name": ""
            }
        ]
    }
}</pre>
### operation: Get Maps List
#### Input parameters
None.
#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": [
        {
            "name": "",
            "type": "",
            "organization": {
                "id": "",
                "name": ""
            },
            "url": ""
        }
    ]
}</pre>
### operation: Get Threat Map
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Actors</td><td>(Optional) Specify the actors based on which you want to filter the result. You can specify multiple actors as csv.
</td></tr><tr><td>Categories</td><td>(Optional) Specify the categories based on which you want to filter the result. You can specify multiple categories as csv.
</td></tr><tr><td>Watch Lists</td><td>(Optional) Specify the watchlist based on which you want to filter the result. You can specify multiple watchlist as csv.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "threat_map": [
            {
                "id": "",
                "name": "",
                "alias": [
                    []
                ],
                "categories": [],
                "intent": "",
                "opportunity": "",
                "log_entries": [
                    {
                        "watchlist": {
                            "id": "",
                            "name": ""
                        },
                        "entity": {
                            "id": "",
                            "name": ""
                        },
                        "severity": "",
                        "axis": "",
                        "date": ""
                    }
                ]
            }
        ],
        "date": ""
    }
}</pre>
### operation: Get Threat Map By Org ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the organization ID whose threat map data to retrieve.
</td></tr><tr><td>Actors</td><td>(Optional) Specify the actors based on which you want to filter the result. You can specify multiple actors as csv.
</td></tr><tr><td>Categories</td><td>(Optional) Specify the categories based on which you want to filter the result. You can specify multiple categories as csv.
</td></tr><tr><td>Watch Lists</td><td>(Optional) Specify the watchlist based on which you want to filter the result. You can specify multiple watchlist as csv.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "threat_map": [
            {
                "id": "",
                "name": "",
                "alias": [
                    []
                ],
                "categories": [],
                "intent": "",
                "opportunity": "",
                "log_entries": [
                    {
                        "watchlist": {
                            "id": "",
                            "name": ""
                        },
                        "entity": {
                            "id": "",
                            "name": ""
                        },
                        "severity": "",
                        "axis": "",
                        "date": ""
                    }
                ]
            }
        ],
        "date": ""
    }
}</pre>
### operation: Get Malware Threat Map
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Malware</td><td>(Optional) Specify the malware based on which you want to filter the result. You can specify multiple malware as csv.
</td></tr><tr><td>Categories</td><td>(Optional) Specify the categories based on which you want to filter the result. You can specify multiple categories as csv.
</td></tr><tr><td>Watch Lists</td><td>(Optional) Specify the watchlist based on which you want to filter the result. You can specify multiple watchlist as csv.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "threat_map": [
            {
                "id": "",
                "name": "",
                "alias": [
                    []
                ],
                "categories": [],
                "prevalence": "",
                "opportunity": "",
                "log_entries": [
                    {
                        "watchlist": {
                            "id": "",
                            "name": ""
                        },
                        "entity": {
                            "id": "",
                            "name": ""
                        },
                        "severity": "",
                        "axis": "",
                        "date": ""
                    }
                ]
            }
        ],
        "date": ""
    }
}</pre>
### operation: Get Malware Threat Map By Org ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Organization ID</td><td>Specify the organization ID whose malware threat map data to retrieve.
</td></tr><tr><td>Malware</td><td>(Optional) Specify the malware based on which you want to filter the result. You can specify multiple malware as csv.
</td></tr><tr><td>Categories</td><td>(Optional) Specify the categories based on which you want to filter the result. You can specify multiple categories as csv.
</td></tr><tr><td>Watch Lists</td><td>(Optional) Specify the watchlist based on which you want to filter the result. You can specify multiple watchlist as csv.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": {
        "threat_map": [
            {
                "id": "",
                "name": "",
                "alias": [
                    []
                ],
                "categories": [],
                "prevalence": "",
                "opportunity": "",
                "log_entries": [
                    {
                        "watchlist": {
                            "id": "",
                            "name": ""
                        },
                        "entity": {
                            "id": "",
                            "name": ""
                        },
                        "severity": "",
                        "axis": "",
                        "date": ""
                    }
                ]
            }
        ],
        "date": ""
    }
}</pre>
### operation: Get Threat Actors List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Name</td><td>(Optional) Specify the list name whose details to retrieve.
</td></tr><tr><td>Limit</td><td>(Optional) Specify the number of records to retrieve.
</td></tr><tr><td>Offset</td><td>(Optional) Specify the offset value to skip the first n element.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": [
        {
            "id": "",
            "type": "",
            "attributes": {
                "name": "",
                "common_names": [
                    []
                ],
                "alias": [
                    []
                ],
                "categories": [
                    {
                        "id": "",
                        "name": ""
                    }
                ]
            }
        }
    ],
    "counts": {
        "returned": "",
        "total": ""
    },
    "next_offset": ""
}</pre>
### operation: Get Threat Actors Categories
#### Input parameters
None.
#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": [
        {
            "id": "",
            "type": "",
            "attributes": {
                "name": "",
                "alias": [
                    []
                ]
            }
        }
    ],
    "counts": {
        "returned": "",
        "total": ""
    }
}</pre>
### operation: Get Malware Categories
#### Input parameters
None.
#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": [
        {
            "id": "",
            "type": "",
            "attributes": {
                "name": "",
                "alias": [
                    []
                ]
            }
        }
    ],
    "counts": {
        "returned": "",
        "total": ""
    }
}</pre>
### operation: Get Third Party Risk Alert By Alert ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Playbook Alert ID</td><td>Specify the unique ID of a specific Playbook Alert whose details to retrieve.
</td></tr><tr><td>Panels</td><td>(Optional) Specify the panels. You can specify multiple panels as csv.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "status": {
        "status_code": "",
        "status_message": ""
    },
    "data": {
        "playbook_alert_id": "",
        "panel_status": {
            "status": "",
            "priority": "",
            "reopen": "",
            "assignee_name": "",
            "assignee_id": "",
            "created": "",
            "updated": "",
            "case_rule_id": "",
            "case_rule_label": "",
            "creator_name": "",
            "creator_id": "",
            "owner_organisation_details": {
                "organisations": [
                    {
                        "organisation_id": "",
                        "organisation_name": ""
                    }
                ],
                "enterprise_id": "",
                "enterprise_name": ""
            },
            "entity_id": "",
            "entity_name": "",
            "entity_criticality": "",
            "risk_score": "",
            "targets": [
                {
                    "name": ""
                }
            ],
            "actions_taken": []
        },
        "panel_evidence_summary": {
            "assessments": [
                {
                    "risk_rule": "",
                    "level": "",
                    "added": "",
                    "evidence": {
                        "summary": "",
                        "type": "",
                        "data": [
                            {
                                "id": "",
                                "title": "",
                                "published": "",
                                "topic": "",
                                "fragment": ""
                            }
                        ]
                    }
                }
            ]
        },
        "panel_log_v2": [
            {
                "id": "",
                "author_id": "",
                "author_name": "",
                "created": "",
                "changes": [
                    {
                        "old": {
                            "id": "",
                            "name": ""
                        },
                        "new": {
                            "id": "",
                            "name": ""
                        },
                        "type": ""
                    }
                ]
            }
        ]
    }
}</pre>
### operation: Get Bulk Third Party Risk Alerts
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Playbook Alert IDs</td><td>(Optional) Specify the playbook alert IDs whose details to retrieve. You can specify multiple playbook alert IDs as csv.
</td></tr><tr><td>Panels</td><td>(Optional) Specify the panels. You can specify multiple panels as csv.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "status": {
        "status_code": "",
        "status_message": ""
    },
    "data": [
        {
            "playbook_alert_id": "",
            "panel_status": {
                "status": "",
                "priority": "",
                "reopen": "",
                "assignee_name": "",
                "assignee_id": "",
                "created": "",
                "updated": "",
                "case_rule_id": "",
                "case_rule_label": "",
                "creator_name": "",
                "creator_id": "",
                "owner_organisation_details": {
                    "organisations": [
                        {
                            "organisation_id": "",
                            "organisation_name": ""
                        }
                    ],
                    "enterprise_id": "",
                    "enterprise_name": ""
                },
                "entity_id": "",
                "entity_name": "",
                "entity_criticality": "",
                "risk_score": "",
                "targets": [
                    {
                        "name": ""
                    }
                ],
                "actions_taken": []
            },
            "panel_evidence_summary": {
                "assessments": [
                    {
                        "risk_rule": "",
                        "level": "",
                        "added": "",
                        "evidence": {
                            "summary": "",
                            "type": "",
                            "data": [
                                {
                                    "id": "",
                                    "title": "",
                                    "published": "",
                                    "topic": "",
                                    "fragment": ""
                                }
                            ]
                        }
                    }
                ]
            },
            "panel_log_v2": [
                {
                    "id": "",
                    "author_id": "",
                    "author_name": "",
                    "created": "",
                    "changes": [
                        {
                            "old": {
                                "id": "",
                                "name": ""
                            },
                            "new": {
                                "id": "",
                                "name": ""
                            },
                            "type": ""
                        }
                    ]
                }
            ]
        }
    ]
}</pre>
### operation: Get Identity Novel Exposures Alert By Alert ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Playbook Alert ID</td><td>Specify the unique ID of a specific Playbook Alert whose details to retrieve.
</td></tr><tr><td>Panels</td><td>(Optional) Specify the panels. You can specify multiple panels as csv.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "status": {
        "status_code": "",
        "status_message": ""
    },
    "data": {
        "playbook_alert_id": "",
        "panel_status": {
            "status": "",
            "priority": "",
            "assignee_name": "",
            "assignee_id": "",
            "created": "",
            "updated": "",
            "case_rule_id": "",
            "case_rule_label": "",
            "creator_name": "",
            "creator_id": "",
            "owner_organisation_details": {
                "organisations": [
                    {
                        "organisation_id": "",
                        "organisation_name": ""
                    }
                ],
                "enterprise_id": "",
                "enterprise_name": ""
            },
            "entity_id": "",
            "entity_name": "",
            "targets": [
                {
                    "name": ""
                }
            ],
            "actions_taken": []
        },
        "panel_evidence_summary": {
            "assessments": [
                {
                    "name": "",
                    "criticality": ""
                }
            ],
            "subject": "",
            "exposed_secret": {
                "type": "",
                "effectively_clear": "",
                "hashes": [
                    {
                        "algorithm": "",
                        "hash": "",
                        "hash_prefix": ""
                    }
                ],
                "details": {
                    "properties": [],
                    "rank": "",
                    "clear_text_value": "",
                    "clear_text_hint": ""
                }
            },
            "dump": {
                "name": "",
                "description": ""
            },
            "authorization_url": "",
            "compromised_host": {
                "exfiltration_date": "",
                "os": "",
                "os_username": "",
                "malware_file": "",
                "timezone": "",
                "computer_name": "",
                "uac": "",
                "antivirus": []
            },
            "malware_family": {
                "id": "",
                "name": ""
            },
            "infrastructure": {
                "ip": ""
            },
            "technologies": [
                {
                    "name": "",
                    "id": "",
                    "category": ""
                }
            ]
        },
        "panel_log_v2": [
            {
                "id": "",
                "author_id": "",
                "author_name": "",
                "created": "",
                "changes": [
                    {
                        "old": {
                            "id": "",
                            "name": ""
                        },
                        "new": {
                            "id": "",
                            "name": ""
                        },
                        "type": ""
                    }
                ]
            }
        ]
    }
}</pre>
### operation: Get Bulk Identity Novel Exposures Alerts
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Playbook Alert IDs</td><td>(Optional) Specify the playbook alert IDs whose details to retrieve. You can specify multiple playbook alert IDs as csv.
</td></tr><tr><td>Panels</td><td>(Optional) Specify the panels. You can specify multiple panels as csv.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "status": {
        "status_code": "",
        "status_message": ""
    },
    "data": [
        {
            "playbook_alert_id": "",
            "panel_status": {
                "status": "",
                "priority": "",
                "assignee_name": "",
                "assignee_id": "",
                "created": "",
                "updated": "",
                "case_rule_id": "",
                "case_rule_label": "",
                "creator_name": "",
                "creator_id": "",
                "owner_organisation_details": {
                    "organisations": [
                        {
                            "organisation_id": "",
                            "organisation_name": ""
                        }
                    ],
                    "enterprise_id": "",
                    "enterprise_name": ""
                },
                "entity_id": "",
                "entity_name": "",
                "targets": [
                    {
                        "name": ""
                    }
                ],
                "actions_taken": []
            },
            "panel_evidence_summary": {
                "assessments": [
                    {
                        "name": "",
                        "criticality": ""
                    }
                ],
                "subject": "",
                "exposed_secret": {
                    "type": "",
                    "effectively_clear": "",
                    "hashes": [
                        {
                            "algorithm": "",
                            "hash": "",
                            "hash_prefix": ""
                        }
                    ],
                    "details": {
                        "properties": [],
                        "rank": "",
                        "clear_text_value": "",
                        "clear_text_hint": ""
                    }
                },
                "dump": {
                    "name": "",
                    "description": ""
                },
                "authorization_url": "",
                "compromised_host": {
                    "exfiltration_date": "",
                    "os": "",
                    "os_username": "",
                    "malware_file": "",
                    "timezone": "",
                    "computer_name": "",
                    "uac": "",
                    "antivirus": []
                },
                "malware_family": {
                    "id": "",
                    "name": ""
                },
                "infrastructure": {
                    "ip": ""
                },
                "technologies": [
                    {
                        "name": "",
                        "id": "",
                        "category": ""
                    }
                ]
            },
            "panel_log_v2": [
                {
                    "id": "",
                    "author_id": "",
                    "author_name": "",
                    "created": "",
                    "changes": [
                        {
                            "old": {
                                "id": "",
                                "name": ""
                            },
                            "new": {
                                "id": "",
                                "name": ""
                            },
                            "type": ""
                        }
                    ]
                }
            ]
        }
    ]
}</pre>
### operation: Create User List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Name</td><td>(Optional) Specify the name with which to create the user list.
</td></tr><tr><td>Type</td><td>(Optional) Specify the type of the user list to create.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "id": "",
    "name": "",
    "type": "",
    "created": "",
    "updated": "",
    "ownerId": "",
    "ownerName": "",
    "organisationId": "",
    "organisationName": "",
    "ownerOrganisationDetails": {
        "owner_id": "",
        "owner_name": "",
        "organisations": [
            {
                "organisation_id": "",
                "organisation_name": ""
            }
        ],
        "enterprise_id": "",
        "enterprise_name": ""
    }
}</pre>
### operation: Get User Lists
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Name</td><td>(Optional) Specify the name of the list to retrieve.
</td></tr><tr><td>Type</td><td>(Optional) Specify the type of the user list to retrieve.
</td></tr><tr><td>Limit</td><td>(Optional) Specify the number of records to retrieve.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>[
    {
        "id": "",
        "name": "",
        "type": "",
        "created": "",
        "updated": "",
        "ownerId": "",
        "ownerName": "",
        "organisationId": "",
        "organisationName": "",
        "ownerOrganisationDetails": {
            "owner_id": "",
            "owner_name": "",
            "organisations": [
                {
                    "organisation_id": "",
                    "organisation_name": ""
                }
            ],
            "enterprise_id": "",
            "enterprise_name": ""
        }
    }
]</pre>
### operation: Get User List By List ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>List ID</td><td>Specify the list ID to retrieve.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "id": "",
    "name": "",
    "type": "",
    "created": "",
    "updated": "",
    "ownerId": "",
    "ownerName": "",
    "organisationId": "",
    "organisationName": "",
    "ownerOrganisationDetails": {
        "owner_id": "",
        "owner_name": "",
        "organisations": [
            {
                "organisation_id": "",
                "organisation_name": ""
            }
        ],
        "enterprise_id": "",
        "enterprise_name": ""
    }
}</pre>
### operation: Get User List Status By List ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>List ID</td><td>Specify the list ID to retrieve.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "size": "",
    "status": ""
}</pre>
### operation: Get Entities By List ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>List ID</td><td>Specify the list ID whose entities to retrieve.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>[
    {
        "entity": {
            "id": "",
            "type": "",
            "name": ""
        },
        "context": {
            "additionalProp1": {}
        },
        "status": "",
        "added": ""
    }
]</pre>
### operation: Add Entity To User List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>List ID</td><td>Specify the list ID in which to add the entity.
</td></tr><tr><td>Entity ID</td><td>Specify the entity ID to add.
</td></tr><tr><td>Context</td><td>(Optional) Specify the context with which to add the entity.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "result": ""
}</pre>
### operation: Remove Entity From User List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>List ID</td><td>Specify the list ID from which to remove the entity.
</td></tr><tr><td>Entity ID</td><td>Specify the entity ID to remove.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "result": ""
}</pre>
### operation: Add IOC To Recorded Future Intelligence Cloud
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Options</td><td>(Optional) Specify the options with which to add IOC To Recorded Future Intelligence Cloud.
</td></tr><tr><td>Organization IDs</td><td>(Optional) Specify the organization IDs with which to add IOC To Recorded Future Intelligence Cloud. You can specify multiple organization IDs as csv.
</td></tr><tr><td>Timestamp</td><td>(Optional) Specify the timestamp with which to add IOC To Recorded Future Intelligence Cloud.
</td></tr><tr><td>IOC</td><td>(Optional) Specify the IOC to add To Recorded Future Intelligence Cloud.
</td></tr><tr><td>Incident</td><td>(Optional) Specify the incident details to add To Recorded Future Intelligence Cloud.
</td></tr><tr><td>Detection</td><td>(Optional) Specify the detection details to add To Recorded Future Intelligence Cloud.
</td></tr><tr><td>Mitre codes</td><td>(Optional) Specify the mitre codes details to add To Recorded Future Intelligence Cloud. You can specify multiple mitre codes as csv.
</td></tr><tr><td>Malware's</td><td>(Optional) Specify the malware's to add To Recorded Future Intelligence Cloud. You can specify multiple malware's as csv.
</td></tr></tbody></table>
#### Output
The output contains the following populated JSON schema:

<pre>{
    "result": {
        "status": "",
        "debug": "",
        "summary": {
            "processed": {
                "ip": "",
                "domain": "",
                "hash": "",
                "vulnerability": "",
                "url": ""
            }
        }
    }
}</pre>
## Included playbooks
The `Sample - recorded-future - 2.0.0` playbook collection comes bundled with the Recorded Future connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Recorded Future connector.

- Add Entity To User List
- Add IOC To Recorded Future Intelligence Cloud
- Alert: Get Alert
- Alert: Search Alert Rules
- Alert: Search Alerts
- Create User List
- Domain : Get Domain Reputation
- Domain : Get Domain Risk List
- Domain : Search Domain
- File : Get File Reputation
- File : Get File Risk List
- File : Search Filehash
- Get Bulk Identity Novel Exposures Alerts
- Get Bulk Third Party Risk Alerts
- Get Entities By List ID
- Get Identity Novel Exposures Alert By Alert ID
- Get Malware Categories
- Get Malware Threat Map
- Get Malware Threat Map By Org ID
- Get Maps List
- Get Risk Rules
- Get Third Party Risk Alert By Alert ID
- Get Threat Actors Categories
- Get Threat Actors List
- Get Threat Map
- Get Threat Map By Org ID
- Get User List By List ID
- Get User List Status By List ID
- Get User Lists
- IP : Get IP Reputation
- IP : Get IP Risk List
- IP : Search IP Addresses
- Malware : Lookup Malware
- Malware : Search Malware
- Remove Entity From User List
- URL : Get URL Risk List
- URL : Lookup URL
- URL : Search URL
- Vulnerability : Get Vulnerability Risk List
- Vulnerability : Lookup Vulnerability
- Vulnerability : Search Vulnerabilities

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
