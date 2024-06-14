"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""


fields_options = {
    'National Vulnerability Database description': 'nvdDescription',
    'Analyst Notes': 'analystNotes',
    'Common Names': 'commonNames',
    'Entity': 'entity',
    'Counts': 'counts',
    'Common Platform Enumeration': 'cpe',
    'Common Platform Enumeration 2.2 URI': 'cpe22uri',
    'Common Vulnerability Scoring System': 'cvss',
    'Hash Algorithm': 'hashAlgorithm',
    'Intel Card URL': 'intelCard',
    'Metrics': 'metrics',
    'Related Entities': 'relatedEntities',
    'Related Links': 'relatedLinks',
    'Risk': 'risk',
    'Sightings': 'sightings',
    'Threat Lists': 'threatLists',
    'Event Timestamps': 'timestamps',
    'Categories': 'categories',
    'Location': 'location'
}

risk_list = {
            'Historically Reported by Insikt Group': 'analystNote',
            'C&C Nameserver': 'cncNameserver',
            'C&C DNS Name': 'cncSite',
            'C&C URL': 'cncUrl',
            'Compromised URL': 'compromisedUrl',
            'Recently Resolved to Host of Many DDNS Names': 'ddns',
            'Historically Reported as a Defanged DNS Names': 'defanged',
            'Recent Fast Flux DNS Name': 'fastFlux',
            'Historically Reported in Threat List': 'historicalThreatListMembership',
            'Large': 'large',
            'Historically Linked to Cyber Attack': 'linkedToCyberAttack',
            'Historical Malware Analysis DNS Name': 'malwareAnalysis',
            'Blacklisted DNS Name': 'multiBlacklist',
            'Active Phishing URL': 'phishingUrl',
            'Ransomware Distribution URL': 'ransomwareDistribution',
            'Ransomware Payment DNS Name': 'ransomwarePayment',
            'Recently Reported by Insikt Group': 'recentAnalystNote',
            'Recently Reported as a Defanged DNS Names': 'recentDefanged',
            'Recently Linked to Cyber Attack': 'recentLinkedToCyberAttack',
            'Recent Malware Analysis DNS Name': 'recentMalwareAnalysis',
            'Recent Threat Researcher': 'recentThreatResearcher',
            'Recent Typosquat Similarity - DNS Sandwich': 'recentTyposquatSandwich',
            'Recent Typosquat Similarity - Typo or Homograph': 'recentTyposquatTypo',
            'Recently Resolved to Malicious IP': 'resolvedMaliciousIp',
            'Recently Resolved to Suspicious IP': 'resolvedSuspiciousIp',
            'Recently Resolved to Unusual IP': 'resolvedUnusualIp',
            'Recently Resolved to Very Malicious IP': 'resolvedVeryMaliciousIp',
            'Trending in Recorded Future Analyst Community': 'rfTrending',
            'Historical Threat Researcher': 'threatResearcher',
            'Historical Typosquat Similarity - DNS Sandwich': 'typosquatSandwich',
            'Historical Typosquat Similarity - Typo or Homograph': 'typosquatTypo',
            'Reported by Insikt Group': 'analystNote',
            'Linked to Cyber Attack': 'linkedToCyberAttack',
            'Linked to Malware': 'linkedToMalware',
            'Linked to Attack Vector': 'linkedToVector',
            'Linked to Vulnerability': 'linkedToVuln',
            'Malware SSL Certificate Fingerprint': 'malwareSsl',
            'Positive Malware Verdict': 'positiveMalwareVerdict',
            'Threat Researcher': 'threatResearcher',
            'Inside Possible Bogus BGP Route': 'bogusBgp',
            'Historical Botnet Traffic': 'botnet',
            'Nameserver for C&C Server': 'cncNameserver',
            'Historical C&C Server': 'cncServer',
            'Cyber Exploit Signal: Important': 'cyberSignalHigh',
            'Cyber Exploit Signal: Medium': 'cyberSignalMedium',
            'Recent Host of Many DDNS Names': 'ddnsHost',
            'Historically Reported as a Defanged IP': 'defanged',
            'Resolution of Fast Flux DNS Name': 'fastFluxResolution',
            'Historical Honeypot Sighting': 'honeypot',
            'Honeypot Host': 'honeypotHost',
            'Recent C&C Server': 'intermediateCncServer',
            'Historically Linked to Intrusion Method': 'linkedIntrusion',
            'Historically Linked to APT': 'linkedIntrusion',
            'Malicious Packet Source': 'maliciousPacketSource',
            'Malware Delivery': 'malwareDelivery',
            'Historical Multicategory Blacklist': 'multiBlacklist',
            'Historical Open Proxies': 'openProxies',
            'Phishing Host': 'phishingHost',
            'Historical Positive Malware Verdict': 'positiveMalwareVerdict',
            'Recent Botnet Traffic': 'recentBotnet',
            'Current C&C Server': 'recentCncServer',
            'Recently Reported as Defanged IP': 'recentDefanged',
            'Recent Honeypot Sighting': 'recentHoneypot',
            'Recently Linked to Intrusion Method': 'recentLinkedIntrusion',
            'Recently Linked to APT': 'recentLinkedToAPT',
            'Recent Multicategory Blacklist': 'recentMultiBlacklist',
            'Recent Open Proxies': 'recentOpenProxies',
            'Recent Positive Malware Verdict': 'recentPositiveMalwareVerdict',
            'Recent Spam Source': 'recentSpam',
            'Recent SSH/Dictionary Attacker': 'recentSshDictAttacker',
            'Recent Bad SSL Association': 'recentSsl',
            'Historical Spam Source': 'spam',
            'Historical SSH/Dictionary Attacker': 'sshDictAttacker',
            'Historical Bad SSL Association': 'ssl',
            'Tor Node': 'tor',
            'Unusual IP': 'unusualIP',
            'Vulnerable Host': 'vulnerableHost',
            'Historically Reported as a Defanged URL': 'defangedURL',
            'Recently Reported as e Defanged URL': 'recentDefangedURL',
            'Web Reporting Prior to CVSS Score': 'awaitingCvssScore',
            'Cyber Exploit Signal: Critical': 'cyberSignalCritical',
            'Linked to Historical Cyber Exploit': 'linkedToCyberExploit',
            'Historically Linked to Exploit Kit': 'linkedToExploitKit',
            'Historically Linked to Malware': 'linkedToIntrusionMethod',
            'Historically Linked to Remote Access Trojan': 'linkedToRAT',
            'Historically Linked to Ransomware': 'linkedToRansomware',
            'Linked to Recent Cyber Exploit': 'linkedToRecentCyberExploit',
            'Recently Linked to Exploit Kit': 'linkedToRecentExploitKit',
            'Recently Linked to Malware': 'linkedToRecentIntrusionMethod',
            'Recently Linked to Remote Access Trojan': 'linkedToRecentRAT',
            'Recently Linked to Ransomware': 'linkedToRecentRansomware',
            'NIST Severity: Critical': 'nistCritical',
            'NIST Severity: High': 'nistHigh',
            'NIST Severity: Low': 'nistLow',
            'NIST Severity: Medium': 'nistMedium',
            'Web Reporting Prior to NVD Disclosure': 'noCvssScore',
            'Recently Linked to Penetration Testing Tools': 'recentScannerUptake',
            'Historically Linked to Penetration Testing Tools': 'scannerUptake'
}


order_by_dict = {
    'Created': 'created',
    'Criticality': 'criticality',
    'First Seen': 'firstseen',
    'Last Seen': 'lastseen',
    'Modified': 'modified',
    'Risk Score': 'riskscore',
    'Rules': 'rules',
    'Seven Days Hits': 'sevendayshits',
    'Sixty Days Hits': 'sixtydayshits',
    'Total Hits': 'totalhits',
    'Triggered': 'triggered'
}

type_list = {
    'IP': 'ip',
    'Domain': 'domain',
    'URL': 'url',
    'File': 'hash',
    'Vulnerability': 'vulnerability'
}

status_dict = {
    'Unassigned': 'unassigned',
    'Assigned': 'assigned',
    'actionable': 'actionable',
    'No Action': 'no-action',
    'Tuning': 'tuning'
}

direction_list = {
    'Ascending': 'asc',
    'Descending': 'desc'
}

PARA_LIST = ['malware', 'categories', 'watchlists', 'actors', 'panels', 'playbook_alert_ids', 'organization_ids', 'mitre_codes', 'malwares']
