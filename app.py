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
        'years_experience': '6+ Years',
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
                'Operate enterprise-scale NOC managing 12+ microservices across multi-region AWS (220M+ users)',
                'Implemented real-time observability infrastructure using Grafana, LogicMonitor, Auvik',
                'Achieved 30-50% alert noise reduction through intelligent event correlation & tuning',
                'Executed P1/P2/P3 incident triage with SLA compliance (30-min to 4-24 hrs MTTR)',
                'Designed business service-level monitoring for crypto workflows (on/off ramps, staking, swaps)',
                'Automated critical event detection via Crypto Events Bot for network upgrades & security threats'
            ]
        },
        {
            'role': 'System Engineer (NOC)',
            'company': 'IT By Design',
            'period': 'Feb 2024 - May 2025',
            'highlights': [
                'Monitored and optimized network performance using Auvik, Meraki, NinjaOne, ConnectWise',
                'Troubleshot LAN/WAN/VPN/firewall issues across enterprise infrastructure',
                'Managed Windows Servers (2008-2022) and Azure cloud services',
                'Administered ITSM tools: ServiceNow, ConnectWise, AutoTask, Kaseya'
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

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=False, host='0.0.0.0', port=port)
