id: ssp_v1
format: markdown
title:  'SSP'
...
<!DOCTYPE html><meta charset="UTF-8">
<style type="text/css" scoped>
body { font-family: serif; }
p {font-family: serif; }
h1 { font-size:1.5em; color:#000000; font-family: sans-serif; margin-top: 3em; margin-bottom: 3em;}
h2 { font-size:1.4em; border-bottom:1px solid #000000; margin-top: 3em; color: #000000; font-family: sans-serif;}
h3 { font-size:1.3em; border-bottom: 0.5px solid #000000; color: #000000; font-weight: bold; margin-top: 2em; font-family: sans-serif;}
h4 { font-size:1.2em; font-weight: bold; color: #000000; font-family: sans-serif;}
h6 { display:none;}
table { border: 1px solid #000000; border-collapse: collapse; width:85%; margin-left:auto; margin-right:auto; margin-top:1em; margin-bottom:4em; font-size:.9em; font-family: sans-serif;}
tr {page-break-inside:avoid; page-break-after:auto;}
th { padding:1em; border:1px solid #000000; page-break-inside:avoid; page-break-after:auto; background: #F2F2F2;}
td { padding:1em; border:1px solid #000000; page-break-inside:avoid; page-break-after:auto;}
.th-header, thead {font-size:.9em; padding:.5em; background-color:#F2F2F2; }
.table-caption { font-size:.9em; font-family:sans-serif; padding-top: 1.5em;}
.bold { font-style:bold; font-weight:300; }
.box-w-border { border:1px solid #000000; padding:.5em; display:block; width:85%; margin-left:auto; margin-right:auto; margin-top:2em; margin-bottom:2em;}
.disclaimer p { text-align:center; font-family:sans-serif; font-size:1em; }
@media print { h2 { font-size: 1.3em; } }
</style>
<body>
<!-- System Information -->

<span style="margin-left:auto; margin-right:auto; display:table; text-align:center; font-size:2.5em; font-family: sans-serif; ">SSP: {{project.system_info.system_name}}</span>
<br />
<span style="margin-left:auto; margin-right:auto; display:table; text-align:center; font-size:1.5em; font-family: sans-serif;">LIMITED OFFICIAL USE</span>

<table>
<tbody><tr><td>
<p style="font-size:1em;">This document contains Sensitive Material
and is exempted from release under the Freedom of Information Act
by Exemption b(2).</p>
<p>Staff reviewing this document must hold a minimum of Public Trust
Level 1c clearance.</p>
</td></tr>
</tbody></table>

<div style="page-break-after: always;">
	<h6>&nbsp;</h6>
</div>

<section>
<h2>1. System Information</h2>

{{project.system_info.output_documents.system_info}}

<!-- /System Information -->
</section>

<section>
<h2>1.  INFORMATION SYSTEM NAME/TITLE</h2>

This System Security Plan provides an overview of the security requirements for the Information System Name (Enter Information System Abbreviation) and describes the controls in place or planned for implementation to provide a level of security appropriate for the information to be transmitted, processed or stored by the system.  Information security is vital to our critical infrastructure and its effective performance and protection is a key component of our national security program.  Proper management of information technology systems is essential to ensure the confidentiality, integrity and availability of the data transmitted, processed or stored by the Enter Information System Abbreviation information system.

The security safeguards implemented for the Enter Information System Abbreviation system meet the policy and control requirements set forth in this System Security Plan.  All systems are subject to monitoring consistent with applicable laws, regulations, agency policies, procedures and practices.

<span class="table-caption">Table 1-1. Information System Name and Title</div>

<!-- Information System Table goes -->
<table>
    <tr>
      <th>Unique Identifier</th>
      <th>Information System Name</th>
      <th>Information System Abbreviation</th>
    </tr>
    <tr>
      <td>{{project.fisma_level.application_number}}</td>
      <td>{{project.system_info.system_name}}</td>
      <td>{{project.system_info.system_short_name}}</td>
    </tr>
</table>
</section>
<section>
<h2>2.  INFORMATION SYSTEM CATEGORIZATION</h2>

The overall information system sensitivity categorization is recorded in Table 2 1. Security Categorization that follows.  Directions for attaching the FIPS 199 document may be found in the following section: Attachment 10, FIPS 199.

<span class="table-caption">Table 2-1. Security Categorization</div>

<!-- security categorization table goes here -->
<table>
    <tr><th>System Sensitivity Level</th></tr>
    <tr><td>{{project.fisma_level.fisma_level}}</td></tr>
</table>

</section>

<section>
<h3>2.1 Information Types</h3>

This section describes how the information types used by the information system are categorized for confidentiality, integrity and availability sensitivity levels.

The following tables identify the information types that are input, stored, processed and/or output from Enter Information System Abbreviation.  The selection of the information types is based on guidance provided by Office of Management and Budget (OMB) Federal Enterprise Architecture Program Management Office Business Reference Model 2.0 and FIPS Pub 199, Standards for Security Categorization of Federal Information and Information Systems which is based on NIST Special Publication (SP) 800-60, Guide for Mapping Types of Information and Information Systems to Security Categories.

The tables also identify the security impact levels for confidentiality, integrity and availability for each of the information types expressed as low, moderate, or high.  The security impact levels are based on the potential impact definitions for each of the security objectives (i.e., confidentiality, integrity and availability) discussed in NIST SP 800-60 and FIPS Pub 199.

The potential impact is low if—

* The loss of confidentiality, integrity, or availability could be expected to have a limited adverse effect on organizational operations, organizational assets, or individuals.
* A limited adverse effect means that, for example, the loss of confidentiality, integrity, or availability might: (i) cause a degradation in mission capability to an extent and duration that the organization is able to perform its primary functions, but the effectiveness of the functions is noticeably reduced; (ii) result in minor damage to organizational assets; (iii) result in minor financial loss; or (iv) result in minor harm to individuals.

The potential impact is moderate if—

* The loss of confidentiality, integrity, or availability could be expected to have a serious adverse effect on organizational operations, organizational assets, or individuals.
* A serious adverse effect means that, for example, the loss of confidentiality, integrity, or availability might: (i) cause a significant degradation in mission capability to an extent and duration that the organization is able to perform its primary functions, but the effectiveness of the functions is significantly reduced; (ii) result in significant damage to organizational assets; (iii) result in significant financial loss; or (iv) result in significant harm to individuals that does not involve loss of life or serious life threatening injuries.

The potential impact is high if—

* The loss of confidentiality, integrity, or availability could be expected to have a severe or catastrophic adverse effect on organizational operations, organizational assets, or individuals.
* A severe or catastrophic adverse effect means that, for example, the loss of confidentiality, integrity, or availability might: (i) cause a severe degradation in or loss of mission capability to an extent and duration that the organization is not able to perform one or more of its primary functions; (ii) result in major damage to organizational assets; (iii) result in major financial loss; or (iv) result in severe or catastrophic harm to individuals involving loss of life or serious life threatening injuries.

<span class="table-caption">Table 2-2. Sensitivity Categorization of Information Types</span>
<!-- Sensitivity Categorization of Information Types Table goes -->
{{project.technical_information.info_type_table_01}}
</section>
<section>
<h2>2.2 Security Objectives Categorization</h2>

Based on the information provided in Table 2 2. Sensitivity Categorization of Information Types, for the Enter Information System Abbreviation, default to the high-water mark for the Information Types as identified in Table 2 3. Security Impact Level below.

<span class="table-caption">Table 2-3. Security Impact Level</span>

{{project.technical_information.security_impact_level}}

Through review and analysis, it has been determined that the baseline security categorization for the Enter Information System Abbreviation system is listed in the Table 2 4. Baseline Security Configuration that follows.

<span class="table-caption">Table 2-4. Baseline Security Configuration</div>

<!-- Security Impact Level Table goes here -->
<table>
    <tr>
      <td class="td-row-title">Information System Abbreviation Security Categorization</td>
      <td>[[LOW_MODERATE_HIGH]]</td>
    </tr>
</table>

Using this categorization, in conjunction with the risk assessment and any unique security requirements, we have established the security controls for this system, as detailed in this SSP.

</section>

<section>
<h2>3.  INFORMATION SYSTEM OWNER</h2>

The following individual is identified as the system owner or functional proponent/advocate for this system.

<span class="table-caption">Table 3-1. Information System Owner</div>

<table >
    <tr>
      <th>Information System Owner Information</th><th></th>
    </tr>
    <tr>
      <td class="td-row-title">Name</td>
      <td>{{project.system_info.system_owner}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Title</td>
      <td>{{project.system_info_poc.system_owner_title}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Company / Organization</td>
      <td>{{project.system_info.system_org}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Phone Number</td>
      <td>{{project.system_info_poc.system_owner_phone}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Email Address</td>
      <td>{{project.system_info_poc.system_owner_email}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Address</td>
      <td>{{project.system_info_poc.system_owner_address}}</td>
    </tr>
</table>
</section>
<section>
<h2>4.  AUTHORIZING OFFICIAL</h2>

The Authorizing Official (AO) or Designated Approving Authority (DAA) for this information system is:

<span class="table-caption">Table 4-1. Information System Authorizing Official</div>

<table >
    <tr>
      <th>Information System Authorizing Official</th><th></th>
    </tr>
    <tr>
      <td class="td-row-title">Name</td>
      <td>{{project.system_info_poc.system_ao_name}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Title</td>
      <td>{{project.system_info_poc.system_ao_title}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Company / Organization</td>
      <td>{{project.system_info_poc.system_ao_org}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Phone Number</td>
      <td>{{project.system_info_poc.system_ao_phone}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Email Address</td>
      <td>{{project.system_info_poc.system_ao_email}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Address</td>
      <td>{{project.system_info_poc.system_ao_address}}</td>
    </tr>
</table>
</section>
<section>
<h2>5.  OTHER DESIGNATED CONTACTS</h2>

<span class="table-caption">Table 5-1. Information System Management Point of Contact</div>

<table >
    <tr>
      <th>Information System Management Point of Contact</th><th></th>
    </tr>
    <tr>
      <td class="td-row-title">Name</td>
      <td>{{project.system_info.system_pm}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Title</td>
      <td>{{project.system_info_poc.system_manager_title}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Company / Organization</td>
      <td>{{project.system_info.system_org}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Phone Number</td>
      <td>{{project.system_info_poc.system_manager_phone}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Email Address</td>
      <td>{{project.system_info_poc.system_manager_email}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Address</td>
      <td>{{project.system_info_poc.system_manager_address}}</td>
    </tr>
</table>

<span class="table-caption">Table 5-2. Information System Technical Point of Contact</div>

<table>
    <tr>
      <th>Information System Technical Point of Contact</th><th></th>
    </tr>
    <tr>
      <td class="td-row-title">Name</td>
      <td>{{project.system_info_poc.system_tech_name}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Title</td>
      <td>{{project.system_info_poc.system_tech_title}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Company / Organization</td>
      <td>{{project.system_info.system_admin_team}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Phone Number</td>
      <td>{{project.system_info_poc.system_tech_phone}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Email Address</td>
      <td>{{project.system_info_poc.system_tech_email}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Address</td>
      <td>{{project.system_info_poc.system_tech_address}}</td>
    </tr>
</table>
</section>
<section>
<h2>6.  ASSIGNMENT OF SECURITY RESPONSIBILITY</h2>

<span class="table-caption">Table 6-1. CSP name Internal ISSO (or Equivalent) Point of Contact</div>

<table >
    <tr>
      <th>CSP name Internal ISSO (or Equivalent) Point of Contact</th><th></th>
    </tr>
    <tr>
      <td class="td-row-title">Name</td>
      <td>{{project.system_info_poc.system_security_name}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Title</td>
      <td>{{project.system_info_poc.system_security_title}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Company / Organization</td>
      <td>{{project.system_info_poc.system_security_org}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Phone Number</td>
      <td>{{project.system_info_poc.system_security_phone}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Email Address</td>
      <td>{{project.system_info_poc.system_security_email}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Address</td>
      <td>{{project.system_info_poc.system_security_address}}</td>
    </tr>
</table>


<span class="table-caption">Table 6-2. AO Point of Contact</div>

<table >
    <tr>
      <th>AO Point of Contact</th><th></th>
    </tr>
    <tr>
      <td class="td-row-title">Name</td>
      <td>{{project.system_info_poc.system_ao_poc_name}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Title</td>
      <td>{{project.system_info_poc.system_ao_poc_title}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Company / Organization</td>
      <td>{{project.system_info_poc.system_ao_poc_org}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Phone Number</td>
      <td>{{project.system_info_poc.system_ao_poc_phone}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Email Address</td>
      <td>{{project.system_info_poc.system_ao_poc_email}}</td>
    </tr>
    <tr>
      <td class="td-row-title">Address</td>
      <td>{{project.system_info_poc.system_ao_poc_address}}</td>
    </tr>
</table>
</section>
<section>
<h2>7.  INFORMATION SYSTEM OPERATIONAL STATUS</h2>

The system is currently in the life-cycle phase shown in Table 7 1. System Status that follows.  (Only operational systems can be granted an ATO).

<span class="table-caption">Table 7-1. System Status</div>

<table>
    <tr>
      <th>System Status</th>
    </tr>
    <tr>
      <td>{{ project.system_info_technical.system_status.text }}</td>
    </tr>
</table>
</section>
<section>
<h2>8.  INFORMATION SYSTEM TYPE</h2>

Information systems, particularly those based on cloud architecture models, are made up of different service layers.  Below are some questions that help the system owner determine if their system is a cloud followed by specific questions to help the system owner determine the type of cloud.

<span class="table-caption">Table 8-1. Service Layers Represented in this SSP</div>

<table >
    <tr>
      <th>System Status</th>
    </tr>
    <tr>
      <td>{{project.system_info_technical.cloud_service_model.text}}
      {% if project.system_info_technical.cloud_service_model == "other" %}
    {{project.system_info_technical.cloud_service_model_other.text}}{% endif %} </td>
    </tr>
</table>

Note: Refer to NIST SP 800-145 for information on cloud computing architecture models.
</section>
<section>
<h3>8.2.  Cloud Deployment Models</h3>

Information systems are made up of different deployment models.  The deployment models of the Enter Information System Abbreviation that are defined in this SSP and are not leveraged by any other FedRAMP Authorizations, are indicated in Table 8 2. Cloud Deployment Model Represented in this SSP that follows.

<span class="table-caption">Table 8-2. Cloud Deployment Model Represented in this SSP</div>

<table>
    <tr>
      <th>System Status</th>
    </tr>
    <tr>
      <td>{{project.system_info_technical.cloud_model.text}}
      {% if project.system_info_technical.cloud_model == "hybrid" %} {{project.system_info_technical.choice_hybrid.text}}{% endif %} </td>
    </tr>
</table>
</section>
<section>
<h3>8.3. Leveraged Authorizations</h3>

The {{project.system_info.system_name}} Choose an item leverages a pre-existing FedRAMP Authorization.  FedRAMP Authorizations leveraged by this Enter Information System Abbreviation are listed in Table 8 3. Leveraged Authorizations that follows.

<span class="table-caption">Table 8-3. Leveraged Authorizations</div>

{{project.system_info_technical.leveraged_authorizations}}
</section>
<section>
<h2>9.  GENERAL SYSTEM DESCRIPTION</h2>
</section>
<section>
<h3>9.1.  System Function or Purpose</h3>
</section>
<section>
{{project.system_info.system_description}}
</section>
<section>
<h3>9.2.  Information System Components and Boundaries</h3>

[[TBD]]

A detailed and explicit definition of the system authorization boundary diagram is represented in Figure 9-1. Authorization Boundary Diagram below.

</section>
<section>
<h3>9.3.  Types of Users</h3>

All personnel have their status categorized with a sensitivity level in accordance with PS-2.  Personnel (employees or contractors) of service providers are considered Internal Users.  All other users are considered External Users.  User privileges (authorization permission after authentication takes place) are described in Table 9 1. Personnel Roles and Privileges that follows.

<span class="table-caption">Table 9-1. Personnel Roles and Privileges</div>

{{project.system_info_technical.security_impact_users}}
</section>
<section>
<h3>9.4.  Network Architecture</h3>

The logical network topology is shown in Figure 9 2. Network Diagram mapping the data flow between components.

The following Figure 9 2. Network Diagram(s) provides a visual depiction of the system network components that constitute Enter Information System Abbreviation.
</section>
<section>
<h2>10. SYSTEM ENVIRONMENT AND INVENTORY</h2>
Directions for attaching the FedRAMP Inventory Workbook may be found in the following section: Attachment 13, FedRAMP Inventory Workbook.
</section>
<section>
<h3>10.1. Data Flow</h3>
The data flow in and out of the system boundaries is represented in Figure 10 1. Data Flow Diagram below.
</section>
<section>
<h3>10.2. Ports, Protocols and Services</h3>

The Table 10 1. Ports, Protocols and Services below lists the ports, protocols and services enabled in this information system.

<span class="table-caption">Table 10-1. Ports, Protocols and Services</div>

{{project.system_info_technical.ports_protocols_services}}
</section>
<section>
<h3>11. SYSTEM INTERCONNECTIONS</h3>

<span class="table-caption">Table 11-1. System Interconnections</div>

{{project.system_info_technical.system_interconnections}}

</section>
<section>
<h2>12. LAWS, REGULATIONS, STANDARDS AND GUIDANCE</h2>
A summary of FedRAMP Laws and Regulations is included in Attachment 12, FedRAMP Laws and Regulations.
</section>
<section>
<h3>12.1. Applicable Laws and Regulations</h3>
The FedRAMP Laws and Regulations can be found on this web page: Templates.
Table 12 1. Information System Name Laws and Regulations includes additional laws and regulations specific to Information System Name.

<span class="table-caption">Table 12-1. Information System Name Laws and Regulations</div>

{{project.system_info_technical.laws_regulations}}
</section>
<section>
<h3>12.2. Applicable Standards and Guidance</h3>
The FedRAMP Standards and Guidance be found on this web page: Templates
Table 12 2. Information System Name Standards and Guidance includes in this section any additional standards and guidance specific to Information System Name.

<span class="table-caption">Table 12-2. Information System Name Standards and Guidance</div>

{{project.system_info_technical.standards_guidance}}



<!-- Testing links -->
<a id="controls" name="controls"></a>

</section>
<section>
<h2>13. MINIMUM SECURITY CONTROLS</h2>

Security controls must meet minimum security control baseline requirements.  Upon categorizing a system as Low, Moderate, or High sensitivity in accordance with FIPS 199, the corresponding security control baseline standards apply.  Some of the control baselines have enhanced controls which are indicated in parentheses.

Security controls that are representative of the sensitivity of Enter Information System Abbreviation are described in the sections that follow.  Security controls that are designated as “Not Selected” or “Withdrawn by NIST” are not described unless they have additional FedRAMP controls.  Guidance on how to describe the implemented standard can be found in NIST 800-53, Rev 4.  Control enhancements are marked in parentheses in the sensitivity columns.

Systems that are categorized as FIPS 199 Low use the controls designated as Low, systems categorized as FIPS 199 Moderate use the controls designated as Moderate and systems categorized as FIPS 199 High use the controls designated as High.

<!--Control catalog here-->

{% set meta = {"current_family_title": "", "current_control": "", "current_control_part": "", "control_count": 0, "current_parts": []} %}

{% for control in system.root_element.selected_controls_oscal_ctl_ids %}
  {% set var_ignore = meta.update({"control_count": meta['control_count'] + 1}) %}

  {% if meta['current_family_title'] != control_catalog[control.lower()]['family_title'] %}
    {# When current current control family changes print the new control family and update the current control family #}
    <h2>{{control_catalog[control.lower()]['family_id']|upper}} - {{control_catalog[control.lower()]['family_title']}}</h2>
    {% set var_ignore = meta.update({"current_family_title": control_catalog[control.lower()]['family_title']}) %}
  {% endif %}
  <div>
    {% if control.lower() in control_catalog %}
    <div>{{control|upper}} - {{control_catalog[control.lower()]['title']}}</div>
    <div style="white-space: pre-wrap;">{{control_catalog[control.lower()]['description']}}</div>
    <div>
      <h4>What is the solution and how is it implemented?</h4>
        {% if control in system.control_implementation_as_dict %}
          <div style="white-space: pre-line; word-break: keep-all;">{{ system.control_implementation_as_dict[control]['combined_smt']|safe }}</div>
        {% else %}
          <div style="white-space: pre-line; word-break: keep-all;">No statement available.</div>
        {% endif %}
    </div>
    {% endif %}
  </div>
{% endfor %}

{% if system.root_element.selected_controls_oscal_ctl_ids|length == 0 %}
<i>Control requirements have not yet been assigned to this system.</i>
{% endif %}

</section>
<section>
<!-- /13. MINIMUM SECURITY CONTROLS -->
