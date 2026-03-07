from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='static', static_url_path='/static')

# Portfolio data
PORTFOLIO_DATA = {
    'name': 'John Mark Lorejo',
    'title': 'NOC Engineer',
    'subtitle': 'Network Operations Center Engineer',
    'email': 'jmlorejo013@gmail.com',
    'phone': '+63 951 146 1981',
    'location': 'Rizal, Philippines',
    'hero_title': 'Architecting Resilience at Scale',
    'hero_desc': 'Enterprise infrastructure specialist managing 220M+ user-facing systems across multi-region AWS deployments. Obsessed with observability, incident excellence, and operational resilience.',

    'socials': {
        'github': 'https://github.com/Jmlorejo',
        'linkedin': 'https://www.linkedin.com/in/jmlorejo/',
        'facebook': 'https://www.facebook.com/johnmark.013'
    },

    'about': {
        'years_experience': '8+ Years',
        'noc_focus': '2+ Years',
        'education': 'BS Computer Engineering',
        'description': 'Enterprise-scale Network Operations Center engineer with 6+ years of IT and 2 years in network operations, specializing in serviceability, observability, incident management, and operational excellence.',
        'full_description': 'Proven expertise managing 220M+ user-facing systems across multi-region AWS environments. Skilled in real-time infrastructure monitoring, P1/P2/P3 incident triage with SLA compliance, and event correlation achieving 30-50% alert noise reduction. Strong advocate for MTTD/MTTR optimization and data-driven postmortem practices.'
    },

    'achievements': [
        {'metric': '220M+', 'label': 'Users Served', 'icon': '👥'},
        {'metric': '30-50%', 'label': 'Alert Noise Reduction', 'icon': '📉'},
        {'metric': '99%+', 'label': 'System Uptime', 'icon': '⬆️'},
        {'metric': '12+', 'label': 'Microservices Managed', 'icon': '⚙️'},
    ],

    'experience': [
        {
            'role': 'NOC Engineer',
            'company': 'Trust Wallet',
            'period': 'May 2025 - Present',
            'highlights': [
                'Operated enterprise-scale Network Operations Center (NOC) managing 12+ microservices with 10+ components each across multi-region AWS infrastructure serving 220M+ users',
                'Implemented real-time observability and monitoring infrastructure using Grafana and API calls to maintain business-critical dashboards tracking service health, error rates, and availability KPIs',
                'Achieved 30% alert noise reduction through in-depth investigation, collaboration and event correlation, alert tuning, and false-positive validation; collaborated with cross-functional resolver teams on anomaly detection and root cause analysis',
                'Executed P0/P1/P2/P3 incident triage and escalation with SLA compliance',
                'Led post-incident reviews and postmortems; drove resilience and availability initiatives with MTTD/MTTR optimization reporting to senior management on weekly basis',
                'Focusing business service-level monitoring (BSM) for mission-critical crypto transaction workflows including on/off ramps, staking, swaps, transfers, deposits, and withdrawals with full telemetry visibility',
                'Automated critical event detection via AI-powered Crypto Events Bot by fetching and delivering real-time intelligence on hardforks, network upgrades, and security threats to organization-wide messaging platform',
                'As one of the pioneer NOC engineers, acted as first-line engineering support by replicating, triaging, and analyzing logs for CS-escalated issues, escalating confirmed bugs with detailed findings to the appropriate engineering teams, and authoring runbooks for newly identified issues to standardize resolution processes.',
                'Served as part of the on-call rotation, responding to after-hours critical incidents and ensuring continuous 24/7 client infrastructure coverage with minimal disruption to operations'
            ]
        },
        {
            'role': 'System/NOC Engineer',
            'company': 'IT By Design',
            'period': 'Feb 2024 - May 2025',
            'highlights': [
                'Monitored network and system performance in real-time across multiple client environments using Auvik, Meraki, NinjaOne, ConnectWise Automate, N-able, LogicMonitor, and Datto RMM, proactively identifying and resolving issues before client impact',
                'Managed and maintained Windows Server environments spanning versions 2008 through 2022, performing routine administration, patch management, and performance tuning across multiple client infrastructures',
                'Managed, and maintained virtual machines on VMware, vSphere, and Hyper-V platforms, handling provisioning, snapshots, resource allocation, and VM-level troubleshooting',
                'Administered ITSM platforms including ServiceNow, ConnectWise Manage, Autotask, Kaseya, and HALO for end-to-end incident lifecycle management, service request handling, change tracking, and SLA compliance',
                'Managed and monitored client backup solutions using Veeam, Datto Backup, and Acronis, ensuring backup integrity, scheduling, and successful recovery testing',
                'Administrated Active Directory, Microsoft Exchange, and Microsoft 365 environments including user provisioning, group policy management, mailbox administration, and license assignments',
                'Provided IT helpdesk support across multiple client accounts, handling hardware diagnostics and replacements, network connectivity issues, and peripheral setup including printers and workstations',
                'Managed user onboarding and offboarding workflows including account creation and deactivation, access management, email setup, and equipment provisioning',
                'Coordinated with client-facing teams and third-party vendors to communicate incident status, resolution timelines, and post-incident summaries to ensure client satisfaction and transparency'
            ]
        },
        {
            'role': 'IT Helpdesk Technician / Command Centre Operations',
            'company': 'ProbeCx',
            'period': 'Jun 2022 - Feb 2024',
            'highlights': [
                'First-line technical support & incident triage via ServiceNow integration',
                'Diagnosed and remediated infrastructure issues across servers, endpoints, networks',
                'Managed Active Directory, Azure AD, Okta for identity & access management',
                'Executed SOPs for time-sensitive production incidents with comprehensive runbooks'
            ]
        }
    ],

    'skills': [
        {
            'category': 'Observability & Monitoring',
            'icon': '📊',
            'items': ['Grafana', 'LogicMonitor', 'Auvik', 'APM', 'Telemetry & Analytics']
        },
        {
            'category': 'Incident Management',
            'icon': '🚨',
            'items': ['P1/P2/P3 Triage', 'SLA Management', 'MTTD/MTTR Optimization', 'Alert Tuning', 'Event Correlation']
        },
        {
            'category': 'AIOps & Automation',
            'icon': '🤖',
            'items': ['AI-Powered Automation', 'Crypto Events Bot', 'Critical Event Detection', 'Alert Filtering']
        },
        {
            'category': 'Infrastructure & Cloud',
            'icon': '☁️',
            'items': ['AWS Multi-Region', 'Windows Server', 'Azure AD', 'Infrastructure Monitoring', 'Application Performance']
        },
        {
            'category': 'Identity & Access',
            'icon': '🔐',
            'items': ['Active Directory', 'Azure AD', 'Okta', 'MFA Systems', 'Access Control']
        },
        {
            'category': 'ITSM & Tools',
            'icon': '🔧',
            'items': ['ServiceNow', 'Incident Management', 'Runbook Creation', 'SOP Documentation']
        }
    ],

    'certifications': [
        'Google Cybersecurity Professional Certificate',
        'Google IT Support Professional Certificate',
        'ISC2: Certified in Cyber Security',
        'Cisco Network Essentials',
        'Fortinet: Technical Introduction to Cybersecurity',
        'CompTIA: Introduction to Cybersecurity'
    ]
}

@app.route('/')
def index():
    return render_template('index.html', data=PORTFOLIO_DATA)

@app.route('/section/<section>')
def get_section(section):
    sections = {
        'about': render_template('sections/about.html', data=PORTFOLIO_DATA),
        'experience': render_template('sections/experience.html', data=PORTFOLIO_DATA),
        'skills': render_template('sections/skills.html', data=PORTFOLIO_DATA),
        'achievements': render_template('sections/achievements.html', data=PORTFOLIO_DATA),
    }
    return sections.get(section, 'Not found')

@app.route('/test-image')
def test_image():
    return send_from_directory('static', 'profile.jpg')

@app.route('/resume')
def resume():
    return send_from_directory('static', 'Porfolio.pdf')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=False, host='0.0.0.0', port=port)
