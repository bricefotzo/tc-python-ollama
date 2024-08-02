from json import loads
from requests import post

system_template = """
You are an internal assistant for a company. Your primary role is to direct inquiries to the appropriate contact based on the topic. Respond concisely and directly, providing only the necessary information.
When redirecting an inquiry, use this format:
Contact: [Name]
Email: [email]
Responsible for: [brief description of topics]

Here's the contact list:

Project Management
Contact: Marie Dupont
Email: marie.dupont@innosoft.com
Responsible for: Task tracking, deadlines, project updates
---
Technical Support
Contact: Thomas Leroy
Email: thomas.leroy@innosoft.com
Responsible for: IT issues, software access, technical troubleshooting
---
Payment and Invoicing
Contact: Sophie Martin
Email: sophie.martin@innosoft.com
Responsible for: Invoice submission, payment schedules, payment issues
---
Security Protocols
Contact: Julien Bernard
Email: julien.bernard@innosoft.com
Responsible for: VPN access, data protection guidelines, security measures
---
Documentation and Resources
Contact: Claire Moreau
Email: claire.moreau@innosoft.com
Responsible for: Project documentation, resource access, Confluence issues

If an inquiry doesn't clearly match any of these categories, ask for clarification before redirecting.
"""

questions_and_expected = [
    ("Who should I contact for an update on my project's deadlines?", "Marie Dupont"),
    ("I am experiencing issues with my VPN connection. Who can assist me?", "Julien Bernard"),
    ("Where to submit my invoice for this month?", "Sophie Martin"),
    ("What are the security protocols I need to follow?", "Julien Bernard"),
    ("I need access to the latest project documentation.", "Claire Moreau")
]

def split_by_line(generator):
    data = b''
    for each_item in generator:
        for line in each_item.splitlines(True):
            data += line
            if data.endswith((b'\r\r', b'\n\n', b'\r\n\r\n', b'\n')):
                yield from data.splitlines()
                data = b''
    if data:
        yield from data.splitlines()

def get_response_content(endpoint, model, system_template, user_question):
    response = ""
    for chunk in split_by_line(
        post(url=f"{endpoint}/api/chat", stream=True, json={
            "model": model,
            "messages": [
                {"role": "system", "content": system_template},
                {"role": "user", "content": user_question}
            ]
        })
    ):
        response += loads(chunk)["message"]["content"]
    return response
